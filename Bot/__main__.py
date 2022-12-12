# © @AravindXD

from pyrogram import *
from config import *

ALONE = Client(
    "ALONE",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins={"root": "Bot.Plugins"},
)
