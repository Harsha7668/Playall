import json, subprocess

from pyrogram import Client, filters

from tata import download_catchup, download_playback_catchup

from utils import check_user, get_tplay_data

from config import api_id, api_hash, bot_token, script_developer




print("Installing YT-DLP")
subprocess.run("pip install yt-dlp".split())


data_json = get_tplay_data()

app = Client("RC_tplay_dl_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)




@app.on_message(filters.incoming & filters.text)
def tplay_past_catchup_dl_cmd_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return
    
    if "/tata" in message.text:
        
        if len(message.text.split()) < 3:
            message.reply_text("<b>Syntax: </b>`/tata [channelName] | [filename]`")
            return
        
        

        cmd = message.text.split("|")
        _, channel = cmd[0].strip().split(" ")

        if channel not in data_json:
            message.reply_text(f"<b>Channel Not in DB</b>")
            return

        download_playback_catchup(channel, cmd[1].strip() , data_json, app, message)

    if not "watch.tataplay.com" in message.text:
        return 
    
    if "coming-soon" in message.text:
        message.reply_text(f"<b>Can't DL something which has not aired yet\nCheck URL and try again...</b>")
        return
    download_catchup(message.text , data_json, app, message)


    

@app.on_message(filters.incoming & filters.command(['start']) & filters.text)
def start_cmd_handler(app, message):

    message.reply_text("<b>A Telegram bot to download from tataPlay</b>\n\n`> >`<b> Made with Love by RC</b>")
    

print(script_developer , "\n")

@app.on_message(filters.incoming & filters.command(['ping']) & filters.text)
async def ping(_, message):
    start_time = time.time()
    msg =  await message.reply_text("Ping...")
    await msg.edit("✮ᑭｴƝGing...✮")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    await msg.edit(f"I Aᴍ Aʟɪᴠᴇ Mᴀꜱᴛᴇʀ\n⋙ 🔔 ᑭｴƝG: {ping_time}\n⋙ ⬆️ ⴑⲢⲦⲒⲘⲈ: {uptime}")
    try:
        await message.delete()
    except:
        return

app.run()
