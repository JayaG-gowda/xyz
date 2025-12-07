#Coded by the @legend580 💛❤️

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class script(object):
    START_MSG = """<b>🤗 Hello {},
ɪ ᴀᴍ ʜᴇʀᴇ ᴛᴏ ᴠᴇʀɪꜰʏ ᴀ ᴄʟᴜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ʙʏ ᴛʜᴇ ᴘʟᴀʏᴇʀꜱ ᴏꜰ ᴛʜᴇ ᴛʀᴇᴀꜱᴜʀᴇ ʜᴜɴᴛ ᴛᴇᴀᴍ.
ɪꜰ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴛʜᴇ <b>ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ</b> ʙᴇʟᴏᴡ 👇</b>"""

    WAIT_MSG = """"<b>Processing ...</b>"""

    ABOUT_TXT = """<b>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
 ‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/group_30_robot>𝐇𝐮𝐧𝐭𝐞𝐫</a>
 
 ‣ My best friend : <a href='tg://settings'>Tʜɪs Pᴇʀsᴏɴ</a> 
 
 ‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/legend580'>ಕನ್ನಡಿಗ 💛❤️</a> 
 
 ‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a> 
 
 ‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a> 
 
 ‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ ᴅʙ</a> 
 
 ‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ1.0.1 [sᴛᴀʙʟᴇ]</b>"""

    HELP_TEXT = """
    <b>𒊹︎︎︎ Contact details</b>
    
     ➪ Jayanna G   - 9019646305
     ➪ Athishay    - 9972156903
     ➪ Harshitha   - 6361673855

     """
    
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Contact 🫂', callback_data='help'),
        InlineKeyboardButton('🧑‍🎓 About🧑‍🎓', callback_data='about')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('🧑‍🎓 About 🧑‍🎓', callback_data='about')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('Contact 🫂', callback_data='help')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    AUTH_ADD_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👁️Confirm', callback_data='addauthuser'),
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    AUTH_DELETE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👁️Confirm', callback_data='deleteauthuser'),
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
