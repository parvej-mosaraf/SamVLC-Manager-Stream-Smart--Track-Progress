# 🎬 SamVLC Manager

SamVLC Manager is a simple web-based video playlist manager designed to extract video links from FTP/web directories, organize them by show or season, track watched episodes, and play episodes directly using VLC Media Player.

## Features

* Extract video links from an FTP/web directory
* Create playlists for different shows or seasons
* Track watched/unwatched episodes
* Play episodes directly in VLC
* Simple web interface
* Save episode progress locally
* Run the application using a `.bat` file

---

# Requirements

Before running SamVLC Manager, make sure you have:

* Windows
* Python 3.x
* VLC Media Player
* Internet/network access to the video server
* Required Python packages

---

# 1. Configure VLC Location

Before running the application, open:

```text
app.py
```

Find the VLC path inside the `/play` function:

```python
vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
```

Change it if VLC is installed in a different location.

For example:

```python
vlc_path = r"D:\Program Files\VideoLAN\VLC\vlc.exe"
```

The path must point to the actual `vlc.exe` file.

You can usually find VLC here:

```text
C:\Program Files\VideoLAN\VLC\vlc.exe
```

or:

```text
C:\Program Files (x86)\VideoLAN\VLC\vlc.exe
```

---

# 2. Install Required Python Packages

Open Command Prompt or PowerShell in the project folder.

Run:

```bash
pip install -r requirements.txt
```

If the project does not contain a `requirements.txt` file, install the required packages manually:

```bash
pip install flask requests beautifulsoup4
```

---

# 3. Run SamVLC Manager

The easiest way to start the application is using the provided `.bat` file.

Double-click the `.bat` file in the project folder.

For example:

```text
run.bat
```

The batch file starts the Flask server.

A successful startup should show something similar to:

```text
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

Keep the Command Prompt window open while using SamVLC Manager.

---

# 4. Open the Web Interface

After starting the `.bat` file, open a web browser and go to:

```text
http://127.0.0.1:5000
```

The SamVLC Manager interface will appear.

---

# 5. Create a Playlist

In the **Create Playlist** section:

1. Enter the FTP/web directory URL.
2. Enter a playlist name.
3. Click **Extract Playlist**.

The application will extract available video links and save them locally.

The playlist data is stored inside:

```text
playlists/
```

Each show/season has its own folder.

---

# 6. Select a Playlist

Under **Playlists**, select a previously created playlist.

The application will display the available episodes.

For example:

```text
Episode 1    ▶ Play    Done
Episode 2    ▶ Play    Done
Episode 3    ▶ Play    Done
```

---

# 7. Play an Episode

Click:

```text
▶ Play
```

SamVLC Manager sends the video link to VLC Media Player.

VLC must be installed and the correct `vlc.exe` path must be configured in `app.py`.

---

# 8. Track Episode Progress

Click:

```text
Done
```

when an episode has been watched.

The button will change to:

```text
Undo
```

and the episode will be marked as completed.

The progress is saved in:

```text
data.json
```

inside the corresponding playlist folder.

---

# Project Structure

A typical project structure looks like:

```text
SamVLC-Manager/
│
├── app.py
├── run.bat
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── playlists/
    └── Show Name/
        ├── extracted_links.txt
        └── data.json
```

---

# Troubleshooting

## VLC does not open

Check the VLC path in:

```text
app.py
```

Make sure it points to:

```text
vlc.exe
```

For example:

```python
vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
```

Also make sure VLC is installed.

---

## The browser cannot connect

Make sure the `.bat` file is running and the terminal shows:

```text
Running on http://127.0.0.1:5000
```

Then open:

```text
http://127.0.0.1:5000
```

---

## Playlist extraction fails

Check that:

* The FTP/web URL is accessible.
* The computer is connected to the required network.
* The URL contains accessible video files.
* The video server is available.

---

# Stopping the Application

To stop SamVLC Manager, return to the Command Prompt window running the application and press:

```text
Ctrl + C
```

---

# License

This project is intended for personal and educational use.
