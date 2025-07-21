from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from config import BOT_TOKEN, LOG_GREEN, LOG_YELLOW
from handlers import message_handlers, start_command

if __name__ == "__main__":
    # Initializing the Bot
    print(f"{LOG_YELLOW('INIT INFO')} Initializing Shadowgram Bot...")
    bot = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    bot.add_handler(CommandHandler("start", start_command))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handlers))

    print(f"{LOG_GREEN('SUCCESS')} Running Shadowgram Bot...")
    bot.run_polling(poll_interval=3, allowed_updates=Update.ALL_TYPES)
