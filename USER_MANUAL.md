# SamVLC Manager - User Manual

**FTP Video Management Made Easy for SamOnline and VLC**

## 📖 Table of Contents

1. [Getting Started](#getting-started)
2. [Step-by-Step Guide](#step-by-step-guide)
3. [Using the Link Extractor](#using-the-link-extractor)
4. [Using the Web Player](#using-the-web-player)
5. [Managing Shows](#managing-shows)
6. [Troubleshooting](#troubleshooting)
7. [Advanced Usage](#advanced-usage)

## 🚀 Getting Started

### What You Need

- **Python 3.7 or higher** installed on your computer
- **VLC Media Player** installed and accessible
- **Access to a SamOnline FTP server** with video content
- **Basic knowledge of file paths** on your operating system

### First-Time Setup

1. **Download and Install Python**
   - Visit [python.org](https://python.org)
   - Download Python 3.7+ for your operating system
   - During installation, check "Add Python to PATH"

2. **Install VLC Media Player**
   - Visit [videolan.org](https://videolan.org)
   - Download and install VLC for your operating system
   - Note the installation path (usually `C:\Program Files\VLC\vlc.exe` on Windows)

3. **Install Project Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📋 Step-by-Step Guide

### Phase 1: Extract Links from SamOnline FTP

#### Step 1: Run the Link Extractor
1. Open Command Prompt or Terminal
2. Navigate to your project folder:
   ```bash
   cd "D:\User\Desktop\VLC"
   ```
3. Run the link extractor:
   ```bash
   python samvlc-extractor.py
   ```

#### Step 2: Provide Required Information
When prompted, enter:

1. **Webpage URL**: The SamOnline FTP page containing video links
   - Example: `http://172.16.50.123/series/attack-on-titan/`
   - This should be the page that lists all episodes

2. **Server Prefix**: The base URL of your SamOnline FTP server
   - Example: `http://172.16.50.123`
   - This is used to create complete video URLs

#### Step 3: Verify Extraction
- The script will show: `✅ Extracted X links and saved to [path]`
- Check that `extracted_links.txt` was created in `D:\User\Desktop\`

### Phase 2: Set Up Your Show

#### Step 1: Create Show Folder
1. Navigate to `D:\User\Desktop\VLC\shows\`
2. Create a new folder with your show name
   - Example: `Attack on Titan`
   - Use clear, descriptive names

#### Step 2: Move Links File
1. Copy `extracted_links.txt` from `D:\User\Desktop\`
2. Paste it into your show folder
3. Rename if needed to `extracted_links.txt`

### Phase 3: Launch the Web Player

#### Step 1: Start the Web Server
1. Open Command Prompt or Terminal
2. Navigate to the web-player folder:
   ```bash
   cd "D:\User\Desktop\VLC\web-player"
   ```
3. Start the web server:
   ```bash
   python app.py
   ```

#### Step 2: Access the Interface
1. Open your web browser
2. Go to: `http://127.0.0.1:5000`
3. You should see the "SamVLC Manager" interface

## 🎬 Using the Web Player

### Main Interface

The web player has a clean, simple interface with:

- **Show Selector**: Dropdown menu to choose your show
- **Episode List**: All episodes displayed with controls
- **Progress Tracking**: Visual indicators for watched episodes

### Episode Controls

Each episode shows:

1. **Episode Number**: "Episode 1", "Episode 2", etc.
2. **Play Button (▶ Play)**: Opens the episode in VLC
3. **Done/Undo Button**: Marks episode as watched/unwatched

### Watching Episodes

1. **Select Your Show**: Choose from the dropdown menu
2. **Click Play**: Click the "▶ Play" button for any episode
3. **VLC Opens**: The episode will open in VLC Media Player
4. **Mark as Done**: Click "Done" when you finish watching
5. **Track Progress**: Watched episodes appear crossed out

### Managing Progress

- **Mark as Watched**: Click "Done" button
- **Mark as Unwatched**: Click "Undo" button
- **Progress Persists**: Your progress is automatically saved
- **Visual Feedback**: Watched episodes are crossed out and dimmed

## 📁 Managing Shows

### Adding New Shows

1. **Extract Links**: Use `samvlc-extractor.py` for the new show
2. **Create Folder**: Make a new folder in `shows/`
3. **Move Links**: Copy `extracted_links.txt` to the new folder
4. **Refresh Browser**: The new show will appear in the dropdown

### Organizing Multiple Shows

```
shows/
├── Attack on Titan/
│   ├── extracted_links.txt
│   └── data.json
├── One Piece/
│   ├── extracted_links.txt
│   └── data.json
└── Naruto/
    ├── extracted_links.txt
    └── data.json
```

### Backup Your Progress

- **Progress Data**: Stored in `data.json` files
- **Backup Method**: Copy the entire `shows` folder
- **Restore Method**: Replace the `shows` folder with your backup

## 🔧 Troubleshooting

### Common Problems and Solutions

#### Problem: "No links file found"
**Solution:**
- Check that `extracted_links.txt` exists in your show folder
- Verify the file name is exactly `extracted_links.txt`
- Ensure the file is not empty

#### Problem: VLC doesn't open
**Solution:**
- Check VLC installation path in `app.py` (line 84)
- Verify VLC is properly installed
- Try opening VLC manually to test

#### Problem: Links don't work
**Solution:**
- Verify the SamOnline FTP server is accessible
- Check that the prefix URL is correct
- Ensure the original webpage had working video links

#### Problem: Progress not saving
**Solution:**
- Check write permissions for the `shows` folder
- Verify the `data.json` file is not corrupted
- Try refreshing the browser page

#### Problem: Web server won't start
**Solution:**
- Check that port 5000 is not in use
- Verify all dependencies are installed
- Check for Python syntax errors

### Error Messages

| Error Message | What It Means | How to Fix |
|---------------|---------------|------------|
| "Error fetching page" | Network connection issue | Check internet connection and URL |
| "No links file found" | Missing links file | Create or move `extracted_links.txt` |
| "VLC not found" | VLC path incorrect | Update VLC path in `app.py` |
| "Port already in use" | Another app using port 5000 | Close other apps or change port |

## 🚀 Advanced Usage

### Customizing Paths

#### Change VLC Path
Edit `web-player/app.py` line 84:
```python
vlc_path = r"C:\Your\Custom\Path\To\VLC\vlc.exe"
```

#### Change Storage Directory
Edit `web-player/app.py` line 10:
```python
BASE_DIR = Path(r"C:\Your\Custom\Path\To\shows")
```

#### Change Link Output Directory
Edit `samvlc-extractor.py` line 31:
```python
save_dir = Path("C:/Your/Custom/Path")
```

### Running on Different Ports

Edit `web-player/app.py` line 94:
```python
app.run(host="127.0.0.1", port=8080, debug=True, use_reloader=False)
```

### Network Access

To access from other devices on your network:
```python
app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
```

### Batch Processing

For multiple shows, create a batch script:

```batch
@echo off
python samvlc-extractor.py
echo Press any key to continue...
pause
```

## 💡 Tips and Best Practices

### Organization Tips

1. **Use Clear Names**: Name show folders descriptively
2. **Keep Backups**: Regularly backup your `shows` folder
3. **Check Links**: Verify extracted links work before organizing
4. **Update Regularly**: Re-extract links if content changes

### Performance Tips

1. **Close Unused Tabs**: Keep browser tabs minimal
2. **Restart Server**: Restart the web server if it becomes slow
3. **Check Disk Space**: Ensure adequate storage for progress data

### Security Tips

1. **Local Use Only**: This tool is designed for local network use
2. **Respect Terms**: Follow SamOnline FTP terms of service
3. **Authorized Access**: Only use with proper authorization

## 📞 Getting Help

### Before Asking for Help

1. **Check This Manual**: Review the troubleshooting section
2. **Check Error Messages**: Note exact error messages
3. **Verify Setup**: Ensure all prerequisites are met
4. **Test Components**: Try each component separately

### When You Need Help

1. **Describe the Problem**: What exactly is happening?
2. **Include Error Messages**: Copy exact error text
3. **Describe Your Setup**: What OS, Python version, etc.?
4. **Show Your Steps**: What did you do before the problem?

---

**Happy Watching! 🎬**

*This manual covers the most common usage scenarios. For advanced customization or specific issues, refer to the code comments or create an issue on the project repository.*
