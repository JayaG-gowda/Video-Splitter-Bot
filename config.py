#Code by KA18 the @legend580 💛❤️

import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6100891233:AAHo_OjnFWTdY_JewRdcqphxASAcAK1IHVg") #ajhhsa
    #BOT_TOKEN = os.environ.get("BOT_TOKEN", "5872747581:AAH7_XPCOCEVfbgUhepjJWlcOmj8wjDTjBk") #jn_url

    API_ID = int(os.environ.get("API_ID", "3393749"))

    API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1061576483").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATES_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001512853438")

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001512853438"))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483"))
    
    #Port
    PORT = os.environ.get("PORT", "8080")

    START_TEXT = """<b>🤗 Hello {}
    ɪ ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏ ꜱᴘʟɪᴛᴛᴇʀ ʙᴏᴛ. 
    ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ/ꜰɪʟᴇ ᴛᴏ ꜱᴘʟɪᴛ ɪɴᴛᴏ ᴇQᴜᴀʟ ᴘᴀʀᴛꜱ. 
    ᴜꜱᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ ᴍᴇ.</b>"""
    
    NOT_AUTH = """<b>🤗 Hello {}
    ʏᴏᴜʀ ɴᴏᴛ ᴀɴ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴜꜱᴇʀ.
    ʏᴏᴜ ɴᴇᴇᴅ ʙᴜʏ ᴀ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ ꜰʀᴏᴍ [ಕನ್ನಡಿಗ 💛❤️](https://t.me/legend580) ᴛᴏ ʙᴇᴄᴏᴍᴇ ᴀɴ ᴀᴜᴛʜᴏʀɪꜱᴇᴅ ᴜꜱᴇʀ.</b>"""

    PROGRESS_BAR = """<b>\n
    ╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
    ┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
    ┣⪼ ⏳️ Dᴏɴᴇ : {0}%
    ┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
    ┣⪼ ⏰️ Eᴛᴀ: {4}
    ╰━━━━━━━━━━━━━━━➣ </b>"""

    HELP_TEXT = """
     𒊹︎︎︎ How To Split File Or Video

     ➪ Send Your File Or Video For Download.
     ➪ Then Reply Command /sp With Split Size To Your File Or Video.
     ➪ Example: Reply <code>/sp 5</code> To Any File Or Video \nHere The Given Video Is Splitted Into 5 Parts And Upload.

     𒊹︎︎︎ How to set thumbnail

     ➪ Send Your Thumbnail Photo To Add Your Permanent Thumbnail Photo.

     𒊹︎︎︎ How To Deleting Thumbnail

     ➪ Send /delthumb To Delete Your Thumbnail.

     𒊹︎︎︎ How To Show Thumbnail 

     ➪ Send /showthumb To View Custom Thumbnail 
 
     """
    
    ABOUT_TEXT = """
     **📛 My Name** : [𝐕𝐢𝐝𝐞𝐨 𝐒𝐩𝐥𝐢𝐭𝐭𝐞𝐫🚀](http://t.me/{username})

     **❤️ Version** : VSBV01.01 🔥

     **🤖 Source** : Not Available ❌

     **🧿 Language** : [Python 3](https://www.python.org/)

     **📢 Framework** : [Pyrogram](https://docs.pyrogram.org/)

     **👨‍💻 Developer** : [ಕನ್ನಡಿಗ 💛❤️](https://t.me/legend580)

     """
    
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help 🫂', callback_data='help'),
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
        InlineKeyboardButton('Help 🫂', callback_data='help')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )

    

    
    
