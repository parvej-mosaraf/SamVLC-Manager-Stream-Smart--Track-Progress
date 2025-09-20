import requests
from bs4 import BeautifulSoup
from pathlib import Path


def fetch_and_extract(url, prefix, output_file="extracted_links.txt"):
    try:
        # Fetch HTML
        prefix = prefix.rstrip("/")  # Ensure no trailing slash
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching page: {e}")
        return

    html_content = response.text

    # Parse HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract all links
    links = []
    for tag in soup.find_all("a", href=True):
        links.append(tag["href"])

    # (Optional) Keep only video-like links
    video_ext = (".m3u8", ".mp4", ".mkv", ".avi")
    filtered_links = [l for l in links if l.endswith(video_ext) or "m3u8" in l]

    # Force save to custom folder
    save_dir = Path("D:/User/Desktop")  # ✅ your preferred folder
    save_dir.mkdir(parents=True, exist_ok=True)  # auto-create if missing
    output_path = save_dir / output_file

    # Write links to file
    with open(output_path, "w", encoding="utf-8") as f:
        for link in filtered_links:
            f.write(prefix + link + "\n")

    print(
        f"✅ Extracted {len(filtered_links)} links and saved to {output_path.resolve()}"
    )


if __name__ == "__main__":
    url = input("🔗 Enter the webpage URL: ").strip()
    prefix = input("🔗 Enter the prefix (e.g., http://172.16.50.xx): ").strip()
    fetch_and_extract(url, prefix=prefix)
