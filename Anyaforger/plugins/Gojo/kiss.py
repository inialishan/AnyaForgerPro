from requests import get
from pyrogram import filters
from pyrogram.types import Message
from Anyaforger import app

@app.on_message(filters.command("kiss"))
async def es_url(_, message):
    try:
        api = "https://api.otakugifs.xyz/gif?reaction=kiss&format=gif"
        get_kiss = get(api)
        get_json = get_kiss.json()
        get_gif_url = get_json["url"]
        await message.reply_video(get_gif_url)
    except:
        pass
