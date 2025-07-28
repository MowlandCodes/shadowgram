import os

from dotenv import load_dotenv

# Loading the Environment Variables
load_dotenv()

# Helper for getting the Environment Variable
get = lambda name: str(os.environ.get(name))

# Database Config
DB_TYPE = get("DB_TYPE")
DB_NAME = get("DB_NAME")
DB_USER = get("DB_USER")
DB_PASSWORD = get("DB_PASSWORD")
DB_HOST = get("DB_HOST")
DB_PORT = get("DB_PORT")

# Main Bot
BOT_TOKEN = get("BOT_TOKEN")
BOT_USERNAME = get("BOT_USERNAME")
CHAT_ID = get("CHAT_ID")

# Victim Bot (To interact with victim)
ALPHA_BOT_TOKEN = get("ALPHA_BOT_TOKEN")
ALPHA_BOT_USERNAME = get("ALPHA_BOT_USERNAME")

# Channel for Bot Comms
CHANNEL_ID = get("CHANNEL_ID")
CHAT_ID = get("CHAT_ID")

BANNER_TEXT = """```
__| |_______________________________________________________________________________________________________________| |__
__   _______________________________________________________________________________________________________________   __
  | |                                                                                                               | |  
  | |       █████████ █████                  █████                                                                  | |  
  | |      ███░░░░░██░░███                  ░░███                                                                   | |  
  | |     ░███    ░░░ ░███████   ██████   ███████  ██████ █████ ███ ████████████████████ ██████ █████████████       | |  
  | |     ░░█████████ ░███░░███ ░░░░░███ ███░░███ ███░░██░░███ ░███░░██████░░██░░███░░██░░░░░██░░███░░███░░███      | |  
  | |      ░░░░░░░░███░███ ░███  ███████░███ ░███░███ ░███░███ ░███ ░██░███ ░███░███ ░░░ ███████░███ ░███ ░███      | |  
  | |      ███    ░███░███ ░███ ███░░███░███ ░███░███ ░███░░███████████░███ ░███░███    ███░░███░███ ░███ ░███      | |  
  | |     ░░█████████ ████ ████░░███████░░███████░░██████  ░░████░████ ░░████████████  ░░████████████░███ █████     | |  
  | |      ░░░░░░░░░ ░░░░ ░░░░░ ░░░░░░░░ ░░░░░░░░ ░░░░░░    ░░░░ ░░░░   ░░░░░██░░░░░    ░░░░░░░░░░░░ ░░░ ░░░░░      | |  
  | |                                                                   ███ ░███ Author: MowlandCodes               | |  
  | |                                                                  ░░██████                                     | |  
  | |                                                                   ░░░░░░                                      | |  
__| |_______________________________________________________________________________________________________________| |__
__   _______________________________________________________________________________________________________________   __
  | |                                                                                                               | |  
```"""
HELP_TEXT = r"""
 *SHADOWGRAM v0\.1* 

*List of Commands*:

/start \- Starts the Shadowgram Bot
/help \- Show this help message
/list \- List all connected Agents
/interact `victim_id` \- Connect \& Interact with the given *Victim ID*
/shell `commands` \- Send *shell command* to the connected Victim
"""
