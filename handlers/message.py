from telegram import Update
from telegram.ext import ContextTypes

from config import ALPHA_BOT_USERNAME, BOT_USERNAME, log_gram


def handle_text_message(text) -> str:
    message = text.lower()

    match message:
        case "are you online?":
            return "I'm Online!"
        case _:
            return "I don't understand what you're trying to say."


async def message_handlers(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    message_type = update.effective_message.chat.type

    match message_type:
        case "group" | "supergroup":
            message_text: str = update.effective_message.text
            sender_id = update.effective_message.from_user.id

            if BOT_USERNAME in message_text:
                response = message_text.replace(BOT_USERNAME, "").strip()
                response = handle_text_message(response)
            else:
                response = handle_text_message(message_text)

            log_gram.info(f"User ({sender_id}) in Group: '{message_text}'")
            log_gram.info(f"Bot: '{response}'")
            await update.effective_message.reply_text(response)

        case "channel":
            message_text: str = update.effective_message.text

            if BOT_USERNAME in message_text or ALPHA_BOT_USERNAME in message_text:
                response = (
                    message_text.replace(BOT_USERNAME, "")
                    .replace(ALPHA_BOT_USERNAME, "")
                    .strip()
                )
                response = handle_text_message(response)
            else:
                response = handle_text_message(message_text)

            log_gram.info(
                f"Channel ({update.effective_message.chat.title}) posted: '{message_text}'"
            )
            log_gram.info(f"Bot: '{response}'")
            await update.effective_message.reply_text(response)

        case _:
            pass  # Don't handle message outside of the group or channel
