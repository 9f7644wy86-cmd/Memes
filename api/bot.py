import os
import logging
import random
from fastapi import FastAPI, Request
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler

# Telegram configurations
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
app = FastAPI()

# Logger
logging.basicConfig(level=logging.INFO)

# Meme list
MEME_LIST = [
    "https://i.imgflip.com/1bij.jpg",
    "https://i.imgflip.com/26am.jpg",
]

# Define command handlers
async def start(update: Update, context):
    """Handle /start command."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome! Use /meme to get a random meme."
    )

async def meme(update: Update, context):
    """Handle /meme command."""
    meme_url = random.choice(MEME_LIST)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=meme_url)

# Add handlers to Dispatchers
application = Application.builder().token(TELEGRAM_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("meme", meme))

# Define the webhook route on FastAPI
@app.post("/")
async def webhook(request: Request):
    """Handle incoming requests from Telegram."""
    json_data = await request.json()
    update = Update.de_json(json_data, bot)
    await application.update_queue.put(update)
    return "ok"