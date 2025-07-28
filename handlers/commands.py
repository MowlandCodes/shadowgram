import json
import traceback

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from config import *


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log error and send it to the Developer"""

    # Send warning to user
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text="""⚠️ *An error has Occurred\\!* ⚠️
        
Report this problem to *@xhadow21 in Telegram*

> For more information about the error, *check the logs*\\.
> 
> Log file: *shadowgram\\.log*
>
> _*Do not reply to this message*_""",
        parse_mode=ParseMode.MARKDOWN_V2,
    )
    log_gram.error("An error has occurred!", exc_info=context.error)

    # Get all the errors and convert it into a sendable format
    tb_error = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb_error = "".join(tb_error)
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    update_str = str(json.dumps(update_str, indent=4, ensure_ascii=False))
    ctx_user = str(context.user_data)
    ctx_chat = str(context.chat_data)

    log_gram.error(
        f"Update: {update_str}\nContext (User): {ctx_user}\nContext (Chat): {ctx_chat}\nTraceback: {tb_error}",
    )


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
