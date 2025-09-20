import os
import subprocess
import json
from pathlib import Path
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Base folder where all shows are kept
BASE_DIR = Path(r"D:\User\Desktop\VLC\shows")


def get_show_folders():
    """Return all folders inside BASE_DIR."""
    return [f.name for f in BASE_DIR.iterdir() if f.is_dir()]


def get_files(show_name):
    """Return paths for links + data.json inside selected show folder."""
    folder = BASE_DIR / show_name
    links_file = folder / "extracted_links.txt"
    data_file = folder / "data.json"
    return folder, links_file, data_file


@app.route("/")
def index():
    shows = get_show_folders()
    return render_template("index.html", shows=shows)


@app.route("/load_show/<show_name>")
def load_show(show_name):
    _, links_file, data_file = get_files(show_name)

    if not links_file.exists():
        return jsonify({"error": "No links file found"}), 404

    # Load links
    with open(links_file, "r", encoding="utf-8") as f:
        links = [line.strip() for line in f if line.strip()]

    # Load progress data (episode index → true/false)
    if data_file.exists():
        with open(data_file, "r", encoding="utf-8") as f:
            try:
                progress = json.load(f)
            except json.JSONDecodeError:
                progress = {}
    else:
        progress = {}

    # Make sure every episode index exists in progress
    for i in range(len(links)):
        if str(i) not in progress:
            progress[str(i)] = False

    return jsonify({"links": links, "progress": progress})


@app.route("/mark_done/<show_name>", methods=["POST"])
def mark_done(show_name):
    _, _, data_file = get_files(show_name)
    data = request.json  # expects {"progress": {...}}

    progress = data.get("progress", {})

    # Save exactly in {"0": true, "1": false, ...} format
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    return jsonify({"status": "ok"})


@app.route("/play/<show_name>", methods=["POST"])
def play(show_name):
    """Open VLC with the selected link."""
    req = request.json
    link = req.get("link")

    if not link:
        return jsonify({"error": "No link provided"}), 400

    vlc_path = r"D:\Program Files\VLC\vlc.exe"

    try:
        subprocess.Popen([vlc_path, link])
        return jsonify({"status": "playing"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
