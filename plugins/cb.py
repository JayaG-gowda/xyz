#Coded by the @legend580 💛❤️

import pyrogram
from bot import Bot
import time
import asyncio
from config import *
from Script import script
from datetime import datetime, timedelta
from pyrogram.types import Message, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

    elif data == "home":
        await query.message.edit_text(
            text=script.START_MSG.format(query.from_user.mention),
            reply_markup=script.START_BUTTONS,
            disable_web_page_preview=True
        )

    elif data == "help":
        await query.message.edit_text(
            text=script.HELP_TEXT,
            reply_markup=script.HELP_BUTTONS,
            disable_web_page_preview=True
        )

    elif data == "about":
        await query.message.edit_text(
            text=script.ABOUT_TXT,
            reply_markup=script.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        pass
