from pyrogram import *
from pyrogram.handlers import *
import KEY
import asyncio

api_id = KEY.api_id
api_hash = KEY.api_hash

st = ' started ... '

print(st.center(51, '*'))

app = Client('superChannel', api_id= api_id, api_hash= api_hash)



@app.on_message(filters.channel)
async def superChannel(client, message):
    msid = [0]
    if message.message_id in msid:
        print(msid)
    elif message.message_id not in msid:
        await message.forward(KEY.ch_id)
        msid.append(message.message_id)
        #print(message)
        
app.run()

