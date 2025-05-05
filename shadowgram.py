from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from config.config import *
from handlers import *

# Features


if __name__ == "__main__":
    # Initializing the Bot
    print("Initializing Shadowgram Bot...")
    bot = ApplicationBuilder().token(BOT_TOKEN).build()

    # Bot Commands
    bot.add_handler(CommandHandler("start", start))

    print("Running Shadowgram Bot...")
    bot.run_polling()
