from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome! Just send me a TeraBox video link and I\'ll download it for you.')

# Function to handle any message (assuming it’s a TeraBox link)
def handle_link(update: Update, context: CallbackContext):
    text = update.message.text
    if "terabox.com" in text or "1024tera.com" in text:
        update.message.reply_text("Processing your link...")
        video_url = get_terabox_video_url(text)
        if video_url:
            try:
                context.bot.send_video(chat_id=update.message.chat_id, video=video_url)
            except:
                update.message.reply_text(f"Download ready: {video_url}")
        else:
            update.message.reply_text("Sorry, couldn't retrieve video.")
    else:
        update.message.reply_text("Please send a valid TeraBox video link.")

# Dummy video extractor (replace this logic)
def get_terabox_video_url(link):
    # Actual scraping ya API logic yahan aayega
    # Abhi ke liye test ke liye dummy URL
    return "https://example.com/dummy_video.mp4"

# Main bot runner
def main():
    token = "YOUR_BOT_API_TOKEN"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_link))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
