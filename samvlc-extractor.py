import requests
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urlsplit, unquote
import os
import re


def sanitize_name(name: str) -> str:
    """Remove/replace invalid characters for Windows filenames."""
    return re.sub(r'[<>:"/\\|?*]', "-", name).strip()


def extract_season_name(url: str):
    """Return the last folder name from the URL as the season name."""
    decoded = unquote(url)
    path = urlsplit(decoded).path.rstrip("/")
    parts = path.split("/")
    if len(parts) < 1:
        return None
    season_name = parts[-1]
    return season_name


def fetch_and_extract(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching page: {e}")
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract all links
    links = [tag["href"] for tag in soup.find_all("a", href=True)]

    # Filter video links
    video_ext = (".m3u8", ".mp4", ".mkv", ".avi")
    filtered_links = [l for l in links if l.endswith(video_ext) or "m3u8" in l]

    # Get season name
    season_name = extract_season_name(url)
    if not season_name:
        print("⚠️ Could not extract season name.")
        return

    # Sanitize for Windows
    safe_season = sanitize_name(season_name)

    # Build folder structure
    base_dir = Path("D:/User/Desktop/VLC/shows")
    season_folder = base_dir / safe_season
    season_folder.mkdir(parents=True, exist_ok=True)

    # Output file
    output_file = season_folder / "extracted_links.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for link in filtered_links:
            # Ensure full URL
            if link.startswith("http"):
                f.write(link + "\n")
            else:
                prefix = f"{urlsplit(url).scheme}://{urlsplit(url).netloc}/"
                f.write(prefix + link.lstrip("/") + "\n")

    print(f"✅ Saved {len(filtered_links)} links to {output_file.resolve()}")


if __name__ == "__main__":
    url = input("🔗 Enter the webpage URL: ").strip()
    fetch_and_extract(url)
