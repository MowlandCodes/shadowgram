from telegram import Update
from telegram.ext import ContextTypes

from config import BOT_USERNAME


def handle_text_message(text) -> str:
    message = text.lower()

    match message:
        case "are you online?":
            return "I'm Online!"
        case _:
            return "I don't understand what you're trying to say."

async def message_handlers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_type = update.message.chat.type
    text = update.message.text
    sender_id = update.message.chat.id

    print(f"User: ({sender_id}) in {message_type}: '{text}'")

    if message_type == "group" or message_type == "supergroup":
        if BOT_USERNAME in text:
            response = text.replace(BOT_USERNAME, "").strip()
            response = handle_text_message(response)
        else:
            return
    else:
        response = handle_text_message(text)

    # Bot response
    print(f"Bot: '{response}'")
    await update.message.reply_text(response)
