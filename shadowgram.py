import logging

from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from config import BOT_TOKEN, log_gram
from handlers import (help_command, interact_command, list_command,
                      message_handlers, shell_command, start_command)

if __name__ == "__main__":
    # Initializing the Bot
    log_gram.debug("Initializing Shadowgram Bot...")
    bot = ApplicationBuilder().token(BOT_TOKEN).build()

    # Command Handlers
    bot.add_handler(CommandHandler("start", start_command))
    bot.add_handler(CommandHandler("help", help_command))
    bot.add_handler(CommandHandler("interact", interact_command))
    bot.add_handler(CommandHandler("shell", shell_command))
    bot.add_handler(CommandHandler("list", list_command))

    # Message Handlers
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handlers))

    log_gram.info("Bot is Online!")
    bot.run_polling(poll_interval=2, allowed_updates=Update.ALL_TYPES)
