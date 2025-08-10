import yt_dlp

# Path to your YouTube cookies (export with browser extension)
COOKIE_FILE = "cookie.txt"

# Optional: Use a proxy to bypass geo-restrictions
# PROXY = "socks5://127.0.0.1:10808"

YDL_OPTS = {
    "cookiefile": COOKIE_FILE,   # Required to avoid YouTube's robot test
    # "proxy": PROXY,            # Uncomment to enable proxy
    "quiet": True
}

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # rick roll warning!

# First, fetch all formats (names stored, not used here)
with yt_dlp.YoutubeDL({**YDL_OPTS, "skip_download": True, "dump_single_json": True}) as ydl:
    info = ydl.extract_info(url, download=False)
    formats_list = [f["format_note"] for f in info["formats"]]  # We won't use this variable

# Now download best video + best audio (requires ffmpeg installed)
with yt_dlp.YoutubeDL({**YDL_OPTS, "format": "bestvideo+bestaudio"}) as ydl:
    info = ydl.extract_info(url, download=True)
    filename = ydl.prepare_filename(info)
