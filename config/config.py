import os

from colorama import Back, Fore, Style, init
from dotenv import load_dotenv

# Loading the Environment Variables
load_dotenv()

init()  # Initializing Colorama

# Main Bot
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
BOT_USERNAME = str(os.environ.get("BOT_USERNAME"))
CHAT_ID = str(os.environ.get("CHAT_ID"))

# Victim Bot (To interact with victim)
ALPHA_BOT_TOKEN = str(os.environ.get("ALPHA_BOT_TOKEN"))
ALPHA_BOT_USERNAME = str(os.environ.get("ALPHA_BOT_USERNAME"))


LOG_RED = lambda x: f"{Back.RED}{Fore.BLACK}{Style.BRIGHT} {x} {Style.RESET_ALL}"
LOG_YELLOW = lambda x: f"{Back.YELLOW}{Fore.BLACK}{Style.BRIGHT} {x} {Style.RESET_ALL}"
LOG_GREEN = lambda x: f"{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} {x} {Style.RESET_ALL}"

HELP_TEXT = r"""*🤖 Shadowgram Bot 1\.0 🤖*

*List of Commands*:
/start \- Starts the Shadowgram Bot
/help \- Show this help message
"""
