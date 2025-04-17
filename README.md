# TeraBox Video Downloader Telegram Bot

Download any TeraBox video directly via Telegram with compression support!

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?style=flat-square)
![Deployed on Koyeb](https://img.shields.io/badge/Deploy-Koyeb-success?style=flat-square)

---

## Features

- ✅ Accepts any `terabox.com` or `1024tera.com` video link
- ✅ Uses Apify API to extract direct download link
- ✅ Auto-compresses large videos to fit within Telegram's size limit (50MB)
- ✅ Sends video directly in chat
- ✅ Deployed and tested on [Koyeb](https://www.koyeb.com)

---

## Demo Screenshot

<p align="center">
  <img src="https://your-screenshot-url.com/demo.png" width="500" />
</p>

---

## How It Works

1. User sends a TeraBox video link to the bot.
2. Bot uses [Apify Actor](https://apify.com/easyapi/terabox-video-file-downloader) to fetch the direct video URL.
3. If the video size is large, it's downloaded, compressed with MoviePy, and re-uploaded.
4. User receives the compressed or original video directly in chat.

---

## Deployment (Koyeb with Docker)

### 1. Clone This Repo

```bash
git clone https://github.com/yourusername/terabox-downloader-bot.git
cd terabox-downloader-bot
