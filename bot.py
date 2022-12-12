# © @AravindXD

from config import *

ALONE = Client(":memory:",
              api_id=API_ID,
              api_hash=API_HASH,
              bot_token=BOT_TOKEN)

if __name__ == "__main__":
    ALONE.run()
