# SamVLC Manager

**FTP Video Management Made Easy for SamOnline and VLC**

A Python-based web application for extracting video links from SamOnline FTP servers and managing episode watching progress through a local web interface with VLC integration.

## 🎯 Project Overview

This project provides a complete workflow for:
1. **Link Extraction**: Extract video links from SamOnline FTP web pages
2. **Web Player Interface**: Display episodes in a clean, organized web interface
3. **Progress Tracking**: Mark episodes as watched/unwatched with persistent storage
4. **VLC Integration**: Direct playback through VLC media player

## 🏗️ Project Structure

```
samvlc-manager/
├── samvlc-extractor.py      # Link extraction script
├── web-player/              # Web application
│   ├── app.py              # Flask web server
│   └── templates/
│       └── index.html      # Web interface
├── shows/                   # Storage for show data
│   └── [Show Folders]/     # Individual show directories
│       ├── extracted_links.txt  # Video links
│       └── data.json       # Watch progress data
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- VLC Media Player installed
- Access to SamOnline FTP server

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd samvlc-manager
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure VLC path** (if needed)
   - Edit `web-player/app.py` line 84
   - Update the VLC executable path to match your installation

4. **Set up storage directory**
   - The application uses `D:\User\Desktop\VLC\shows` by default
   - Create this directory or modify the path in `app.py`

### Usage

#### Step 1: Extract Links
```bash
python samvlc-extractor.py
```
- Enter the SamOnline FTP webpage URL
- Enter the server prefix (e.g., `http://172.16.50.xx`)
- Links will be saved to `D:\User\Desktop\extracted_links.txt`

#### Step 2: Organize Content
1. Create a folder in `shows/` for your show
2. Move `extracted_links.txt` to the show folder
3. Rename it to `extracted_links.txt` if needed

#### Step 3: Launch Web Player
```bash
cd web-player
python app.py
```
- Open your browser to `http://127.0.0.1:5000`
- Select your show from the dropdown
- Start watching and tracking progress!

## 📋 Features

### Link Extractor (`samvlc-extractor.py`)
- **Web Scraping**: Extracts all video links from SamOnline FTP pages
- **Filtering**: Automatically filters for video files (.m3u8, .mp4, .mkv, .avi)
- **Prefix Handling**: Adds server prefix to relative links
- **Error Handling**: Robust error handling for network issues

### Web Player (`web-player/`)
- **Show Management**: Browse multiple shows from a dropdown
- **Episode Listing**: Clean, organized episode display
- **Progress Tracking**: Mark episodes as watched/unwatched
- **VLC Integration**: Direct playback through VLC media player
- **Persistent Storage**: Progress saved in JSON format
- **Responsive UI**: Clean, modern interface

## 🔧 Configuration

### Customizing Paths

**VLC Path** (in `web-player/app.py`):
```python
vlc_path = r"D:\Program Files\VLC\vlc.exe"  # Update this path
```

**Storage Directory** (in `web-player/app.py`):
```python
BASE_DIR = Path(r"D:\User\Desktop\VLC\shows")  # Update this path
```

**Link Output** (in `samvlc-extractor.py`):
```python
save_dir = Path("D:/User/Desktop")  # Update this path
```

### Server Configuration

The web server runs on:
- **Host**: 127.0.0.1 (localhost)
- **Port**: 5000
- **Debug Mode**: Enabled (for development)

## 📁 Data Structure

### Show Folder Structure
```
shows/
└── [Show Name]/
    ├── extracted_links.txt    # One link per line
    └── data.json             # Progress tracking
```

### Progress Data Format
```json
{
  "0": true,    // Episode 1 watched
  "1": false,   // Episode 2 not watched
  "2": true     // Episode 3 watched
}
```

## 🛠️ API Endpoints

- `GET /` - Main interface
- `GET /load_show/<show_name>` - Load show data
- `POST /mark_done/<show_name>` - Update watch progress
- `POST /play/<show_name>` - Launch VLC with selected link

## 🐛 Troubleshooting

### Common Issues

1. **VLC not opening**
   - Check VLC installation path in `app.py`
   - Ensure VLC is properly installed

2. **Links not loading**
   - Verify `extracted_links.txt` exists in show folder
   - Check file encoding (should be UTF-8)

3. **Progress not saving**
   - Check write permissions for `shows` directory
   - Verify JSON file format

4. **Network errors during extraction**
   - Check internet connection
   - Verify SamOnline FTP server accessibility
   - Check if URL and prefix are correct

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Please check the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for educational and personal use only. Please respect the terms of service of any FTP servers you access and ensure you have proper authorization to use the content.

## 📞 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the code comments
3. Open an issue on GitHub

---

**Happy Watching! 🎬**
