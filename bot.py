#import logging
from pyrogram import Client,idle
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_NAME = os.environ.get("SESSION_STRING")


app = Client(SESSION_NAME, API_ID, API_HASH,plugins=dict(root="plugins"))
#logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
