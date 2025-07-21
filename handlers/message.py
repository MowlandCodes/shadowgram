from telegram import Update
from telegram.ext import ContextTypes

from config import BOT_USERNAME, log_gram


def handle_text_message(text) -> str:
    message = text.lower()

    match message:
        case "are you online?":
            return "I'm Online!"
        case _:
            return "I don't understand what you're trying to say."


async def message_handlers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_type: str = update.message.chat.type
    text: str = update.message.text
    sender_id = update.message.from_user.id
    message_title = update.message.chat.title

    if message_type == "group" or message_type == "supergroup":
        if BOT_USERNAME in text:
            response = text.replace(BOT_USERNAME, "").strip()
            response = handle_text_message(response)
        else:
            response = handle_text_message(text)
    else:
        response = handle_text_message(text)

    # Bot response
    log_gram.info(f"User: ({sender_id}) in Chat({message_title}): '{text}'")
    log_gram.info(f"Bot: '{response}'")
    await update.message.reply_text(response)
