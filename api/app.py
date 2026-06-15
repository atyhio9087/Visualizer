"""
Funky Monkey Project — Flask backend for Vercel
------------------------------------------------
Handles YouTube only. /api/vibe is handled by api/vibe.js — do not add it here.

Endpoints:
  GET /api/info?url=   → JSON metadata (video or playlist)
  GET /api/stream?id=  → 302 redirect to YouTube CDN audio URL
  GET /api/health      → health check
"""

import re
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def _ydl(extra_opts: dict):
    try:
        import yt_dlp
    except ImportError:
        return None, "yt-dlp not installed"
    base = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "socket_timeout": 20,
    }
    base.update(extra_opts)
    return yt_dlp.YoutubeDL(base), None


def _thumb(info: dict) -> str:
    t = info.get("thumbnail") or ""
    if not t:
        thumbs = info.get("thumbnails") or []
        t = thumbs[-1].get("url", "") if thumbs else ""
    return t


def _fmt(e: dict) -> dict:
    return {
        "id":        e.get("id", ""),
        "title":     e.get("title", "Unknown"),
        "uploader":  e.get("uploader") or e.get("channel") or "",
        "duration":  e.get("duration") or 0,
        "thumbnail": _thumb(e),
    }


@app.route("/api/info")
def api_info():
    url = request.args.get("url", "").strip()
    if not url:
        return jsonify({"error": "url parameter required"}), 400

    ydl, err = _ydl({"extract_flat": False, "playlistend": 200, "noplaylist": False})
    if err:
        return jsonify({"error": err}), 500

    try:
        with ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return jsonify({"error": str(e)}), 422

    if not info:
        return jsonify({"error": "Could not fetch info"}), 422

    if info.get("_type") == "playlist" or info.get("entries"):
        entries = [_fmt(e) for e in (info.get("entries") or []) if e]
        return jsonify({
            "type":      "playlist",
            "title":     info.get("title", "Playlist"),
            "uploader":  info.get("uploader") or info.get("channel") or "",
            "thumbnail": _thumb(info),
            "entries":   entries,
        })

    return jsonify(_fmt(info) | {"type": "video"})


@app.route("/api/stream")
def api_stream():
    vid = request.args.get("id", "").strip()
    if not vid or not re.match(r"^[A-Za-z0-9_-]{11}$", vid):
        return jsonify({"error": "valid 11-char video id required"}), 400

    ydl, err = _ydl({"format": "bestaudio[ext=webm]/bestaudio[ext=m4a]/bestaudio"})
    if err:
        return jsonify({"error": err}), 500

    try:
        with ydl:
            info = ydl.extract_info(
                f"https://www.youtube.com/watch?v={vid}",
                download=False,
            )
    except Exception as e:
        return jsonify({"error": str(e)}), 422

    if not info:
        return jsonify({"error": "Could not extract stream"}), 422

    audio_url = None
    for fmt in sorted(info.get("formats") or [], key=lambda f: f.get("abr") or 0, reverse=True):
        if fmt.get("acodec") != "none" and fmt.get("vcodec") in (None, "none", ""):
            audio_url = fmt.get("url")
            if audio_url:
                break

    audio_url = audio_url or info.get("url")
    if not audio_url:
        return jsonify({"error": "No streamable URL found"}), 422

    return redirect(audio_url, code=302)


@app.route("/api/health")
def api_health():
    try:
        import yt_dlp
        ok = True
    except ImportError:
        ok = False
    return jsonify({"ok": True, "yt_dlp": ok})
