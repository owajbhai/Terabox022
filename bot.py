from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# === CONFIG ===
BOT_TOKEN = "YOUR_BOT_TOKEN"
APIFY_TOKEN = "YOUR_APIFY_TOKEN"

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Bas mujhe TeraBox ka video link bhejo, main uska download link ya video bhej dunga.")

# TeraBox link handle karne wala function
def handle_link(update: Update, context: CallbackContext):
    text = update.message.text
    if "terabox.com" in text or "1024tera.com" in text:
        update.message.reply_text("Link process kiya ja raha hai... thoda ruk jao.")

        # Call kar rahe hain Apify API
        video_url = get_terabox_video_url(text, APIFY_TOKEN)

        if video_url:
            try:
                # Try sending video directly
                context.bot.send_video(chat_id=update.effective_chat.id, video=video_url)
            except:
                # Agar video bhejna fail ho toh download link bhej do
                update.message.reply_text(f"Video ready hai, lekin size zyada ho sakta hai:\n{video_url}")
        else:
            update.message.reply_text("Sorry, video link extract nahi ho paya.")
    else:
        update.message.reply_text("Valid TeraBox video link bhejo (jaise: 1024terabox.com).")

# TeraBox video download link extract karne wala function (via Apify API)
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

# Main function to run the bot
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_link))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
