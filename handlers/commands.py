from telegram import Update
from telegram.ext import ContextTypes

from config import *


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_markdown_v2(
        r"""Hi, Shadowgram is *online*\. You can use /help to get started\."""
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_markdown_v2(HELP_TEXT)
