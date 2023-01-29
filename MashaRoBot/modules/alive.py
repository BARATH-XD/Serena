import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from pyrogram import __version__ as pyro
from telethon import events, Button, custom, version
from MashaRoBot.events import register
from MashaRoBot import telethn as borg
from MashaRoBot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================SERENA====================== """
file1 = "https://telegra.ph/file/8a48d5b1fa7129a07bc2a.jpg"
file2 = "https://telegra.ph/file/a541cc9b5f38a7fcf6c13.jpg"
file3 = "https://telegra.ph/file/4cb3c137cc06121e410b4.jpg"
file4 = "https://telegra.ph/file/5f92dd01bf8d9d0528ed8.jpg"
file5 = "https://telegra.ph/file/f96a0748425e2fe528f0a.jpg"
""" =======================SERENA====================== """



START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    await yes.delete()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    user_id = yes.sender.id
    user_name = yes.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    pm_caption = f"** ♡ Hi {mention}! I,m Serena ✘ **\n\n"
    pm_caption += f"**♡ Bot State :** `Alive`\n\n"
    pm_caption += f"**♡ My Uptime :** `{uptime}`\n\n"
    pm_caption += f"**♡ Telethon Version :** `{version.__version__}`\n\n"
    pm_caption += f"**♡ Pyorgram Version :** `{pyro}`\n\n"
    pm_caption += "**♡ My Master :** [Barath](https://t.me/ImCrazy_Boy)\n"
    BUTTON = [[Button.url("Support", "https://t.me/serena_support"), Button.url("Updates", "https://t.me/Serena_Updates")]]
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption, buttons=BUTTON)
    

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file5, buttons=BUTTON)
