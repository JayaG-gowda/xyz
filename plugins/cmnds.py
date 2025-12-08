#Coded by the @legend580 💛❤️

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os, time
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, CallbackQuery
from bot import Bot
from config import *
from Script import script
from plugins.database.database import db

@Client.on_message(filters.command('get') & filters.private & filters.user(Config.AUTH_USERS))
async def add_auth(bot, update):
    id = update.from_user.id
    cmd = update.command
    if len(cmd) == 1:
        await update.reply(text = "Invalid Syntax, send the command properly.\nExample: <code>/get ABC1234</code> \nABC1234 - unique code which is on the paper and it should be case sensitive")
    elif len(cmd) == 2:
        try:
            global code_id
            code_id = str(cmd[1].strip())
            
            o_code_id = 

          
            await update.reply_text(text = f"<b>Do You Want To Add The Given [User](tg://user?id={auth_id}) To An Auth User.\nClick Below Button Confirm 👇</b>",
                                      disable_web_page_preview=True, reply_markup=Config.AUTH_ADD_BUTTONS, quote=True)
        except:
            await update.reply(text = "Invalid Code, it may be case sensitive or wrong, please chech again and resend.")
