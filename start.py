# © @AravindXD

from pyrogram import *
from pyrogram.types import *
from bot import *

#---------------------------------------------------------

START_TEXT = "Hey ! I'm Adavance Start Bot !"

START_BUTTON = [
    InlineKeyboardButton(
        text='Support',
        url='https://t.me/TheSupportXChat'
    )
]

#---------------------------------------------------------

@ALONE.on_message(filters.private & filters.command("start"))
async def start(bot, message):
        await message.reply_text(
        text=START_TEXT,
        reply_markup=InlineKeyboardMarkup(START_BUTTON]),
        disable_web_page_preview=True,
        quote=True
        )
