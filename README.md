# 💎 Mirror Nexus Bot

> The most powerful Mirror & Leech Telegram Bot. Free. Fast. Feature-rich.

**Developer:** [@Venuboyy](https://t.me/Venuboyy)  
**Channel 1:** [@zerodev2](https://t.me/zerodev2)  
**Channel 2:** [@mvxyoffcail](https://t.me/mvxyoffcail)

---

## ✨ Features

### 📥 Download
- Direct links, Torrents, Magnets (via aria2c)
- YouTube & 1000+ sites (via yt-dlp)
- Mega.nz, Google Drive, NZB/Usenet
- Telegram files direct download

### ☁️ Upload
- Telegram (File or Media mode)
- Google Drive (OAuth / Service Account)
- RClone (any cloud)
- GoFile · PixelDrain · BuzzHeavier
- YouTube

### 🎬 Video Tools (auto-menu on video send)
1. Audio & Subtitles Remover
2. Audio & Subtitles Extractor
3. Caption & Buttons Editor
4. Video Trimmer
5. Video Merger
6. Mute Audio
7. Video + Audio Merger
8. Video + Subtitle Merger (hardsub / softsub)
9. Video → GIF Converter
10. Video Splitter
11. Screenshot Generator
12. Manual Screenshot Generator
13. Video Sample Generator
14. Video → Audio Converter (mp3, wav, flac, aac, opus, ogg, m4a, wma, ac3)
15. Video Optimizer
16. Video Converter (MKV, MP4, AVI, WebM, M4V)
17. Video Renamer
18. Media Info
19. Make Archive (ZIP, RAR, 7Z, optional password)

### 🎵 Audio Tools (auto-menu on audio send)
1. Caption & Buttons Editor
2. Slowed & Reverb Maker
3. Audio Converter (mp3, wav, flac, aac, opus, ogg, m4a, wma, ac3)
4. Make Archive
5. Audio Merger
6. 8D Audio Converter
7. Music Equalizer (Volume, Bass, Treble, Speed)
8. Bass Booster (range -20 to +20)
9. Treble Booster (range -20 to +20)
10. Audio Trimmer (start → end)
11. Auto Audio Trimmer (start + duration)
12. Audio Renamer
13. Audio Tag Editor (Album Art)
14. Audio Speed Changer (50–200%)
15. Volume Changer (10–200%)
16. Media Info
17. Compress Audio

### 📄 Document Tools (auto-menu on document send)
1. File Renamer
2. Archive Creator (ZIP)
3. Archive Extractor
4. Caption & Buttons Editor
5. Forward Tag Remover
6. Subtitle Converter (srt, vtt, ass, sbv)
7. JSON Formatter (indent 1–4)

### 🔗 URL Tools (auto-menu on link send)
1. Mirror (as file)
2. Leech (as media)
3. YouTube Download
4. Google Drive Downloader
5. Mega.nz Download
6. URL Uploader (link → Telegram file)
7. Extract Archive via Direct Link
8. URL Shortener & Unshortener
9. Bulk Links Downloader (`/bulk_url`)

### ⚙️ Settings (`/settings`)
- Upload Mode: File / Media
- Rename Prefix & Suffix
- Custom Thumbnail
- Caption Mode

### 🔐 Session String (`/session`)
- Generate Pyrogram session string in-bot
- Enables **4 GB** uploads via your account
- Stored securely in MongoDB

---

## 🚀 Deployment

### Prerequisites
- Python 3.11+
- MongoDB (local or Atlas)
- aria2c (for downloads)
- ffmpeg
- Bot Token from [@BotFather](https://t.me/BotFather)
- API ID & Hash from [my.telegram.org](https://my.telegram.org)

### Quick Start (Docker)

```bash
git clone <your-repo>
cd MirrorNexusBot
cp .env.example .env
# Edit .env with your credentials
docker-compose up -d
```

### Manual Start

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env
python main.py
```

### .env Configuration

| Variable | Description |
|---|---|
| `BOT_TOKEN` | Your bot token from BotFather |
| `API_ID` | Telegram API ID from my.telegram.org |
| `API_HASH` | Telegram API Hash |
| `OWNER_ID` | Your Telegram user ID |
| `SUDO_USERS` | Comma-separated extra admin IDs |
| `FORCE_SUB_CHANNEL_1` | Channel ID for force subscribe |
| `FORCE_SUB_CHANNEL_2` | Second channel ID |
| `MONGO_URI` | MongoDB connection URI |
| `DOWNLOAD_DIR` | Local download path (default: /tmp/downloads) |
| `MAX_SPLIT_SIZE` | Max file chunk size in bytes (default: 2GB) |
| `WORKERS` | Pyrogram workers count (default: 500) |
| `ARIA2C_HOST` | aria2c RPC host |
| `ARIA2C_PORT` | aria2c RPC port (default: 6800) |
| `ARIA2C_SECRET` | aria2c RPC secret |
| `GDRIVE_FOLDER_ID` | Google Drive folder ID for uploads |

---

## 📋 Commands

| Command | Description |
|---|---|
| `/start` | Start the bot |
| `/help` | Show all commands |
| `/about` | About the bot |
| `/info` | Your profile details |
| `/session` | Manage session string (4GB uploads) |
| `/settings` | Personal settings panel |
| `/mirror` / `/m` | Mirror a link (upload as file) |
| `/leech` / `/l` | Leech a link (upload as media) |
| `/ytdl` | Download from YouTube/sites |
| `/torrent` | Download torrent/magnet |
| `/bulk_url` | Bulk links downloader |
| `/upload` | Upload replied file to cloud |
| `/status` | Check active tasks |
| `/cancel` | Cancel active task |
| `/stats` | Bot statistics *(admin)* |
| `/broadcast` | Broadcast message *(admin)* |
| `/ban` | Ban a user *(admin)* |
| `/unban` | Unban a user *(admin)* |

---

## 🏗 Project Structure

```
MirrorNexusBot/
├── main.py                 # Entry point
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── config/
│   └── config.py           # All configuration
├── bot/
│   ├── client.py           # Pyrogram client + helpers
│   ├── database.py         # MongoDB interface
│   └── script.py           # All message texts
├── handlers/
│   ├── start.py            # /start, /help, /about + force-sub
│   ├── info.py             # /info with profile photo
│   ├── admin.py            # /stats, /broadcast, /ban, /unban
│   ├── session.py          # Session string generator
│   ├── settings.py         # /settings panel
│   ├── video.py            # Video tools menu
│   ├── audio.py            # Audio tools menu
│   ├── document.py         # Document tools menu
│   ├── url.py              # URL/link handler
│   ├── mirror.py           # /mirror, /leech, /ytdl, /torrent
│   └── upload.py           # Upload to cloud commands
└── utils/
    ├── helpers.py          # FFmpeg, progress, archive utils
    ├── aria2_manager.py    # aria2c RPC wrapper
    ├── ytdl_manager.py     # yt-dlp wrapper
    ├── tg_uploader.py      # Telegram uploader (4GB session)
    ├── gdrive.py           # Google Drive helper
    ├── rclone.py           # RClone helper
    └── third_party.py      # GoFile, PixelDrain, BuzzHeavier
```

---

## 👨‍💻 Developer

Built with ❤️ by [@Venuboyy](https://t.me/Venuboyy)
