from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetAllStickersRequest, GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from time import sleep
from datetime import datetime
import requests, os, sys, re, random, json, asyncio

os.system("cls" if os.name == "nt" else "clear")
BANNER="""
  ______    ______   ________  ______  _______  
 /      \  /      \ /        |/      |/       \ 
/$$$$$$  |/$$$$$$  |$$$$$$$$/ $$$$$$/ $$$$$$$  |
$$ |  $$/ $$ |  $$/    $$ |     $$ |  $$ |__$$ |
$$ |      $$ |         $$ |     $$ |  $$    $$/ 
$$ |   __ $$ |   __    $$ |     $$ |  $$$$$$$/  
$$ \__/  |$$ \__/  |   $$ |    _$$ |_ $$ |      
$$    $$/ $$    $$/    $$ |   / $$   |$$ |      
 $$$$$$/   $$$$$$/     $$/    $$$$$$/ $$/  
"""
api_id = 18537104
api_hash = '37fe72eeb1beff079bd6f8944f56dc36'

if len(sys.argv) == 2:
    nomer = sys.argv[1]
else:
    sys.exit(f"python {sys.argv[0]} +62858703453957")
if os.path.isdir("session") == False:
    os.mkdir("session")
print(f"\033[1;36m{BANNER}\033[0m\n\033[1;32mAuthor: \033[1;34mkakatoji\033[0m")
print("\033[1;37m="*60)
client = TelegramClient("session/"+nomer,api_id,api_hash).start(phone=nomer)

@client.on(events.NewMessage())
async def main(event):
    try:
        username ='@'+(await client.get_me()).username
    except:
        pass
    try:
        if event.from_id.user_id == 962775809 and event.message.out == False and "Created an airdrop in" in event.message.message:
            await asyncio.sleep(random.randint(5,10))
            message = event.message.message.split("Send")[1].split(" to grab it!")[0]
            await client.send_message(event.message.peer_id.channel_id, message)
            print(f"\033[1;31m{username} \033[1;32msend message \033[1;36m{message}\033[0m")
        elif "Created a giveaway in" in event.message.message:
            await asyncio.sleep(random.randint(1,3))
            await event.click(text='๐Grab๐')
            print(f"\033[1;31m{username} \033[1;33msuksess claim giveaway\033[0m")
        elif event.from_id.user_id == 962775809 and event.message.out == False and "Created a draw in" in event.message.message:
            await asyncio.sleep(random.randint(2,5))
            pesan = event.message.message.split("Send")[1].split("to grab it!")[0]
            await client.send_message(event.message.peer_id.channel_id, pesan)
            print(f"\033[1;31m{username} \033[1;32msend draw \033[1;36m{pesan}\033[0m")
    except:
        pass
async def main():
    await client.run_until_disconnected()
client.loop.run_until_complete(main())

