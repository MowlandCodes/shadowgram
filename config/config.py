import os

from dotenv import load_dotenv

# Loading the Environment Variables
load_dotenv()

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
CHAT_ID = str(os.environ.get("CHAT_ID"))
OP_ID = str(os.environ.get("OP_ID"))
