from os import path

import pyrogram
from pyrogram import Client, filters

from Checker import checker


class Run(object):
    def __init__(self):
        with open(path.join(".", "target", "config.txt"), "r") as f:
            self.api_id, self.api_hash, self.admin_id, self.target1 = [
                i.strip() for i in f.readlines() if i != "\n" and i[0] != "#"
            ]

        self.app = Client(
            "FreeFood",
            self.api_id,
            self.api_hash,
            proxy={"scheme": "socks5", "hostname": "127.0.0.1", "port": 9051},
        )
        self.self_ = None

        self.process()
        self.runner()
        self.app.run()

    def process(self):
        @self.app.on_message(filters.chat(int(self.target1)))
        async def process(client, m: pyrogram.types.messages_and_media.message.Message):
            if self.self_ and checker(m.text, self.self_):
                await m.reply("استفاده")
                await self.app.send_message(m.from_user.id, "سلام")
                await self.app.send_message(
                    m.from_user.id, "من میتونم غذاتون رو استفاده کنم؟"
                )

                self.self_ = None
                await self.app.send_message(self.admin_id, "انجام شد.")

    def runner(self):
        @self.app.on_message(filters.chat(int(self.admin_id)))
        async def runner(client, m: pyrogram.types.messages_and_media.message.Message):
            if self.self_:
                await m.reply("ربات در حال اجرا است. صبور باشید.")
            elif m.text in ["FAN1", "FAN2", "MEHR"]:
                self.self_ = m.text
                await m.reply("درحال انجام ...")
            elif m.text == "OFF":
                self.self_ = None
                await m.reply("کنسل شد.")
            else:
                await m.reply("متوجه نشدم :(")


if __name__ == "__main__":
    Run()
