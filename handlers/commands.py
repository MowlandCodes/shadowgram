from telegram import Update
from telegram.ext import ContextTypes

from config import *


async def start_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_markdown_v2(
        f"""{BANNER_TEXT}\n *SHADOWGRAM v0\\.1* \n\nHi, *Shadowgram is online*\\.✅\nYou can use /help to get started\\."""
    )


async def help_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_markdown_v2(f"{BANNER_TEXT}{HELP_TEXT}")


async def list_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def interact_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    pass


async def shell_command(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    pass
