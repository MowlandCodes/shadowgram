import os

from colorama import Back, Fore, Style, init
from dotenv import load_dotenv

# Loading the Environment Variables
load_dotenv()

init()

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
CHAT_ID = str(os.environ.get("CHAT_ID"))
OP_ID = str(os.environ.get("OP_ID"))


LOG_RED = lambda x: f"{Back.RED}{Fore.BLACK}{Style.BRIGHT} {x} {Style.RESET_ALL}"
LOG_YELLOW = lambda x: f"{Back.YELLOW}{Fore.BLACK}{Style.BRIGHT} {x} {Style.RESET_ALL}"
LOG_GREEN = lambda x: f"{Back.GREEN}{Fore.BLACK}{Style.BRIGHT} {x} {Style.RESET_ALL}"
