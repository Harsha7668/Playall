def ping(update: Update, context: CallbackContext):
    msg = update.effective_message

    start_time = time.time()
    message = msg.reply_text("🏓 ᴘɪɴɢɪɴɢ ʙᴀʙʏ....​")
    end_time = time.time()
    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))

    message.edit_text(
        "ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ! ❤️\n"
        "<b>ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode=ParseMode.HTML,
    )


@sudo_plus
def pingall(update: Update, context: CallbackContext):
    to_ping = ["Telegram"]
    pinged_list = ping_func(to_ping)
    pinged_list.insert(2, "")
    uptime = get_readable_time((time.time() - StartTime))

    reply_msg = "⏱ᴘɪɴɢ ʀᴇsᴜʟᴛs ᴀʀᴇ:\n"
    reply_msg += "\n".join(pinged_list)
    reply_msg += "\n<b>ᴜᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(uptime)

    update.effective_message.reply_text(
        reply_msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


PING_HANDLER = DisableAbleCommandHandler("ping", ping, run_async=True)
PINGALL_HANDLER = DisableAbleCommandHandler("pingall", pingall, run_async=True)

dispatcher.add_handler(PING_HANDLER)
dispatcher.add_handler(PINGALL_HANDLER)

command_list = ["ping", "pingall"]

handlers = [PING_HANDLER, PINGALL_HANDLER]
