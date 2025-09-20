# SamVLC Manager - Project Structure

**FTP Video Management Made Easy for SamOnline and VLC**

## 📁 Directory Hierarchy

```
samvlc-manager/                         # Project root directory
├── 📄 README.md                        # Main project documentation
├── 📄 USER_MANUAL.md                   # Detailed user guide
├── 📄 PROJECT_STRUCTURE.md             # This file - project structure documentation
├── 📄 requirements.txt                 # Python dependencies
├── 📄 .gitignore                       # Git ignore rules
├── 📄 LICENSE                          # Project license
├── 🐍 samvlc-extractor.py              # Link extraction script
├── 📁 web-player/                      # Web application directory
│   ├── 🐍 app.py                      # Flask web server (main application)
│   └── 📁 templates/                  # HTML templates directory
│       └── 📄 index.html              # Main web interface template
└── 📁 shows/                           # Data storage directory
    └── 📁 [Show Folders]/             # Individual show directories (created dynamically)
        ├── 📄 extracted_links.txt     # Video links file (one per show)
        └── 📄 data.json              # Watch progress data (one per show)
```

## 🔍 File Descriptions

### Core Application Files

#### `samvlc-extractor.py`
- **Purpose**: Extracts video links from SamOnline FTP web pages
- **Dependencies**: `requests`, `beautifulsoup4`, `pathlib`
- **Input**: Webpage URL and server prefix
- **Output**: `extracted_links.txt` file with video links
- **Key Functions**:
  - `fetch_and_extract()`: Main extraction function
  - Filters for video file extensions (.m3u8, .mp4, .mkv, .avi)
  - Adds server prefix to relative links

#### `web-player/app.py`
- **Purpose**: Flask web server for the player interface
- **Dependencies**: `Flask`, `pathlib`, `json`, `subprocess`
- **Features**:
  - Show management and loading
  - Progress tracking with JSON persistence
  - VLC integration for video playback
  - RESTful API endpoints
- **Key Functions**:
  - `get_show_folders()`: Lists available shows
  - `get_files()`: Gets file paths for a show
  - `load_show()`: Loads show data and progress
  - `mark_done()`: Updates watch progress
  - `play()`: Launches VLC with selected link

#### `web-player/templates/index.html`
- **Purpose**: Web interface template
- **Features**:
  - Responsive design with modern CSS
  - JavaScript for dynamic content loading
  - Episode listing with play/done controls
  - Progress tracking UI
- **Key Elements**:
  - Show selector dropdown
  - Episode list container
  - Play/Done/Undo buttons
  - Progress persistence

### Data Storage Files

#### `shows/[Show Name]/extracted_links.txt`
- **Purpose**: Stores video links for a specific show
- **Format**: One link per line, UTF-8 encoding
- **Content**: Complete URLs with server prefix
- **Example**:
  ```
  http://172.16.50.123/series/attack-on-titan/episode1.m3u8
  http://172.16.50.123/series/attack-on-titan/episode2.m3u8
  ```

#### `shows/[Show Name]/data.json`
- **Purpose**: Tracks watch progress for episodes
- **Format**: JSON object with episode indices as keys
- **Content**: Boolean values indicating watched status
- **Example**:
  ```json
  {
    "0": true,
    "1": false,
    "2": true,
    "3": false
  }
  ```

### Documentation Files

#### `README.md`
- **Purpose**: Main project documentation
- **Content**: Overview, installation, usage, features
- **Target**: GitHub visitors and new users

#### `USER_MANUAL.md`
- **Purpose**: Detailed user guide
- **Content**: Step-by-step instructions, troubleshooting
- **Target**: End users and support

#### `PROJECT_STRUCTURE.md`
- **Purpose**: Technical documentation
- **Content**: File descriptions, architecture, data flow
- **Target**: Developers and contributors

### Configuration Files

#### `requirements.txt`
- **Purpose**: Python package dependencies
- **Content**: Package names and version constraints
- **Usage**: `pip install -r requirements.txt`

#### `.gitignore`
- **Purpose**: Git ignore rules
- **Content**: Files and directories to exclude from version control
- **Includes**: Python cache, data files, temporary files

#### `LICENSE`
- **Purpose**: Project license information
- **Content**: Legal terms for use and distribution

## 🔄 Data Flow

### Link Extraction Workflow

```
1. User runs samvlc-extractor.py
2. Script prompts for URL and prefix
3. Requests webpage content
4. Parses HTML with BeautifulSoup
5. Extracts all <a> tags with href attributes
6. Filters for video file extensions
7. Adds server prefix to relative links
8. Saves to extracted_links.txt
```

### Web Player Workflow

```
1. User starts Flask server (app.py)
2. Browser loads index.html
3. JavaScript requests show list
4. User selects show from dropdown
5. JavaScript requests show data (links + progress)
6. Server loads extracted_links.txt and data.json
7. UI renders episode list with controls
8. User clicks play → VLC opens with video
9. User clicks done → progress saved to data.json
```

## 🏗️ Architecture Overview

### Component Relationships

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ samvlc-extractor│───▶│  extracted_links │───▶│   Web Player    │
│     .py         │    │      .txt        │    │     (Flask)     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
                                ▼                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │   Show Folders   │    │   VLC Player    │
                       │    (shows/)      │    │   (External)    │
                       └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │    data.json     │
                       │  (Progress)      │
                       └──────────────────┘
```

### Technology Stack

- **Backend**: Python 3.7+
- **Web Framework**: Flask 2.2+
- **Web Scraping**: requests + BeautifulSoup4
- **Frontend**: HTML5 + CSS3 + Vanilla JavaScript
- **Media Player**: VLC (external)
- **Data Storage**: JSON files + text files
- **Path Handling**: pathlib

## 🔧 Configuration Points

### Hardcoded Paths (Need Customization)

1. **VLC Executable Path** (`web-player/app.py:84`)
   ```python
   vlc_path = r"D:\Program Files\VLC\vlc.exe"
   ```

2. **Storage Directory** (`web-player/app.py:10`)
   ```python
   BASE_DIR = Path(r"D:\User\Desktop\VLC\shows")
   ```

3. **Link Output Directory** (`samvlc-extractor.py:31`)
   ```python
   save_dir = Path("D:/User/Desktop")
   ```

### Server Configuration

- **Host**: 127.0.0.1 (localhost)
- **Port**: 5000
- **Debug Mode**: Enabled
- **Reloader**: Disabled

## 📊 Data Models

### Show Data Structure
```python
{
    "name": "Show Name",
    "folder": "path/to/show/folder",
    "links_file": "extracted_links.txt",
    "progress_file": "data.json"
}
```

### Episode Data Structure
```python
{
    "index": 0,           # Episode number (0-based)
    "link": "http://...", # Video URL
    "watched": False      # Watch status
}
```

### Progress Data Structure
```python
{
    "0": True,   # Episode 1 watched
    "1": False,  # Episode 2 not watched
    "2": True    # Episode 3 watched
}
```

## 🚀 Deployment Considerations

### Development Environment
- Local Flask server
- File-based storage
- Single-user access

### Production Considerations
- Database integration for multi-user support
- Authentication and authorization
- HTTPS for secure connections
- Process management (systemd, PM2, etc.)
- Load balancing for multiple instances

### Scalability Limitations
- File-based storage not suitable for high concurrency
- No user management or authentication
- Single VLC instance limitation
- Local file system dependency

---

*This structure documentation provides a complete technical overview of the SamVLC Manager project. For user-facing documentation, see README.md and USER_MANUAL.md.*
