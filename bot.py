from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import os

# === CONFIG ===
BOT_TOKEN = "8064037408:AAHsfyG0jCJ1fOjW9SNuPGqrgvCQPQtANGI"
APIFY_TOKEN = "apify_api_qdxMztR4cuxXj00ohSMTpZjWbYM3IM2cQEtP"

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)
dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Bas mujhe TeraBox ka video link bhejo, main uska download link ya video bhej dunga.")

# Handle TeraBox links
def handle_link(update: Update, context: CallbackContext):
    if not update.message or not update.message.text:
        return

    text = update.message.text
    if "terafileshare.com" in text or "1024tera.com" in text:
        update.message.reply_text("Link process kiya ja raha hai... thoda ruk jao.")
        video_url = get_terabox_video_url(text, APIFY_TOKEN)
        if video_url:
            try:
                context.bot.send_video(chat_id=update.effective_chat.id, video=video_url)
            except:
                update.message.reply_text(f"Video ready hai, lekin size zyada ho sakta hai:\n{video_url}")
        else:
            update.message.reply_text("Sorry, video link extract nahi ho paya.")
    else:
        update.message.reply_text("Valid TeraBox video link bhejo (jaise: 1024terabox.com).")

# Apify API se download link lena
def get_terabox_video_url(link, apify_token):
    api_url = f"https://api.apify.com/v2/acts/easyapi~terabox-video-file-downloader/run-sync-get-dataset-items?token={apify_token}"
    payload = {"url": link}
    headers = {"Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0].get("downloadUrl")
    return None

# Handlers register karna
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_link))

# Webhook receive karne ke liye endpoint
@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# Health check route
@app.route("/", methods=["GET"])
def index():
    return "Bot is running!"

# Flask run for Koyeb
if __name__ == "__main__":
    # Bot webhook set karo (one-time, or move to setup script)
    webhook_url = f"https://corporate-tommi-botbhaisona-f667374c.koyeb.app/{BOT_TOKEN}"
    bot.set_webhook(webhook_url)

    app.run(host="0.0.0.0", port=8000)
