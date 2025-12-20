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
ps={
  'CS01':'',
  'CS02':'',
  'CS03':'',
  'CS04':'',
  'CS05':'',
  'CS06':'',
  'CS07':'',
  'CS08':'',
  'CS09':'',
  'CS010':'',
  'CS011':'',
}
ids={
    5092726834:['CS05','Sumathi'],
    5393136828:['CS09','VIVEK'],
    5049943931:['CS03','Manjula'],
    1827457712:['CS01','Veda'],
    721778236:['CS06','Kush'],
    2069783555:['CS03','Sukk'],
    5163091853:['CS02','Govinda'],
    1431838576:['CS10','Aman'],
    1428060350:['CS04','Srusti'],
    5068888843:['CS09','Rekha'],
    7601081539:['CS08','Keerthi'],
    1187985752:['CS01','Athishay'],
    1335490342:['CS07','Sharath'],
    5864451133:['CS08','Harshitha'],
    1061576483:['CS01','CS02','CS03','CS04','CS05','CS06','CS07','CS08','CS09','CS10','Jay']
 }

@Client.on_message(filters.command('get') & filters.private & filters.user(Config.AUTH_USERS))
async def add_auth(bot, update):
    id = update.from_user.id
    cmd = update.command
    if len(cmd) == 1:
        await update.reply(text = "Invalid Syntax, send the command properly.\nExample: <code>/get ABC1234</code> \nABC1234 - unique code which is on the paper and it should be case sensitive")
    elif len(cmd) == 2:
        for i in range(len(ids)):
            if(id==list(ids.keys())[i]):
                key=ids[list(ids.keys())[i]][0]
                name=ids[list(ids.keys())[i]][-1]
                break;
                
        code_id = str(cmd[1].strip())
        user = db.get_code(key)
        output='0'
        p=user['id']
        for i in range(len(ps)):
            if(p==list(ids.keys())[i]):
                pl=ps[list(ps.keys())[i]]
              
        for i in range(len(user['hints'])):
            if(code_id==list(user['hints'].keys())[i]):
                output=user["hints"][list(user["hints"].keys())[i]][0]
                break;
            else:
                output='0'
        if(output!='0'): 
            await update.reply_text(text = f"Output string is <b><i>{output}</i></b> \n\n\nHey committee member you can go ahead and conduct activities for 12 mins not more not less.\nThe time consideration is only for fun activities, if they choose to solve code then, they have to finish the complete set of codes to proceed forward. If they do not solve the code they should be held there until they finish 😠.\n\nVerified by - {name}")
            await bot.send_message(Config.LOG_CHANNEL, f"Output string is <b><i>{output}</i></b> \n\n\nHey committee member you can go ahead and conduct activities for 12 mins not more not less.\nThe time consideration is only for fun activities, if they choose to solve code then, they have to finish the complete set of codes to proceed forward. If they do not solve the code they should be held there until they finish 😠\n\n<b>Verified from - {pl}\nVerified by - {name}<\b>")
        else:
            await update.reply_text(text = f"<b>Sorry guys you are at the wrong place 😱.\n\nVerified by - {name}</b>")
            await bot.send_message(Config.LOG_CHANNEL, f"<b>Sorry guys you are at the wrong place 😱.\n\nVerified from - {pl}\nVerified by - {name}</b>")
        # except:
        #     await update.reply(text = "Something went wrong please contact the admin - 9019646305.")
