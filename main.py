from os import path

import pyrogram
from pyrogram import Client, filters

from Checker import checker

with open(path.join(".", "target", "config.txt"), "r") as f:
    api_id, api_hash, admin_id, target1 = [
        i.strip() for i in f.readlines() if i != "\n" and i[0] != "#"
    ]


app = Client(
    "FreeFood",
    api_id,
    api_hash,
    proxy={"scheme": "socks5", "hostname": "127.0.0.1", "port": 9051},
)
self_ = None


@app.on_message(filters.chat(int(target1)))
async def process(client, m: pyrogram.types.messages_and_media.message.Message):
    if self_ and checker(m.text, self_):
        await m.reply("استفاده")
        await app.send_message(m.from_user.id, "سلام")
        await app.send_message(m.from_user.id, "من میتونم غذاتون رو استفاده کنم؟")

        self_ = None
        app.send_message(admin_id, "انجام شد.")


@app.on_message(filters.chat(int(admin_id)))
async def runner(client, m: pyrogram.types.messages_and_media.message.Message):
    if not self_:
        m.reply("ربات در حال اجرا است. صبور باشید.")
    if m.text in ["FAN1", "FAN2"]:
        self_ = m.text
        m.reply("درحال انجام ...")
    else:
        m.reply("متوجه نشدم :(")


if __name__ == "__main__":
    app.run()
