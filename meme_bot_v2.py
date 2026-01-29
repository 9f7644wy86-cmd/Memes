import logging
import random
from telegram import Update, Bot, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(  
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# List of meme URLs
MEME_LIST = [
    "https://i.imgflip.com/1bij.jpg",  # Meme example 1
    "https://i.imgflip.com/26am.jpg",  # Meme example 2
    "https://i.imgflip.com/3fsds.jpg"   # Add more memes easily here
]

def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message with basic instructions."""
    await update.message.reply_text("Welcome to Meme Bot! Use /meme to get fresh memes!")

async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a random meme."""
    meme_url = random.choice(MEME_LIST)
    await update.message.reply_photo(photo=meme_url)

if __name__ == "__main__":
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"

    # Initialize the bot application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("meme", meme))

    # Start polling for updates
    print("Meme Bot is running! Press Ctrl+C to stop.")
    application.run_polling()