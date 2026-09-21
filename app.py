import json
import re
import subprocess
import webbrowser
from pathlib import Path
from urllib.parse import urlsplit, unquote

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

BASE_DIR = Path("playlists")
BASE_DIR.mkdir(exist_ok=True)


def sanitize_name(name):
    return re.sub(r'[<>:"/\\|?*]', "-", name).strip()


def create_playlist(url, playlist_name):
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = [tag["href"] for tag in soup.find_all("a", href=True)]

    video_ext = (".m3u8", ".mp4", ".mkv", ".avi")

    filtered_links = [
        link for link in links if link.endswith(video_ext) or "m3u8" in link
    ]

    playlist_name = sanitize_name(playlist_name)

    folder = BASE_DIR / playlist_name
    folder.mkdir(parents=True, exist_ok=True)

    links_file = folder / "extracted_links.txt"
    progress_file = folder / "data.json"

    with open(links_file, "w", encoding="utf-8") as f:
        for link in filtered_links:
            if link.startswith("http"):
                f.write(link + "\n")
            else:
                prefix = f"{urlsplit(url).scheme}://{urlsplit(url).netloc}/"
                f.write(prefix + link.lstrip("/") + "\n")

    if not progress_file.exists():
        with open(progress_file, "w", encoding="utf-8") as f:
            json.dump({}, f)

    return len(filtered_links)


def get_shows():
    return sorted([folder.name for folder in BASE_DIR.iterdir() if folder.is_dir()])


def get_files(show):
    folder = BASE_DIR / show
    return (
        folder,
        folder / "extracted_links.txt",
        folder / "data.json",
    )


@app.route("/")
def index():
    return render_template("index.html", shows=get_shows())


@app.route("/extract", methods=["POST"])
def extract():
    data = request.json

    url = data.get("url", "").strip()
    playlist_name = data.get("playlist_name", "").strip()

    if not url or not playlist_name:
        return jsonify({"error": "URL and playlist name required"}), 400

    try:
        count = create_playlist(url, playlist_name)

        return jsonify(
            {
                "status": "success",
                "episodes": count,
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/shows")
def shows():
    return jsonify(get_shows())


@app.route("/load_show/<show>")
def load_show(show):

    _, links_file, data_file = get_files(show)

    if not links_file.exists():
        return jsonify({"error": "No playlist found"}), 404

    with open(links_file, "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip()]

    if data_file.exists():
        with open(data_file, "r", encoding="utf-8") as f:
            try:
                progress = json.load(f)
            except:
                progress = {}
    else:
        progress = {}

    for i in range(len(links)):
        progress.setdefault(str(i), False)

    return jsonify(
        {
            "links": links,
            "progress": progress,
        }
    )


@app.route("/mark_done/<show>", methods=["POST"])
def mark_done(show):

    _, _, data_file = get_files(show)

    progress = request.json.get("progress", {})

    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    return jsonify({"status": "saved"})


@app.route("/play", methods=["POST"])
def play():
    link = request.json.get("link")

    print("PLAY REQUEST:", link)

    vlc_path = r"D:\Program Files\VLC\vlc.exe"

    subprocess.Popen([vlc_path, link])

    return jsonify({"status": "playing"})


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        use_reloader=False,
    )
