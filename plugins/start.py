from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/ytdofficial")],
        [InlineKeyboardButton(
            "ADMIN CONNECT 😊", url="https://t.me/Ytcs_bot")]
    ])
    welcomed = f"Hello Bro, Hope You Enjoy Bot Mr <b>{message.from_user.first_name}</b>\n Appo ini polikkaam"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
