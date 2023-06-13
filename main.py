import asyncio
from os import path
from random import choice

import pyrogram
from pyrogram import Client, filters

from Checker import checker


class Run(object):
    def __init__(self):
        with open(path.join(".", "target", "config.txt"), "r") as f:
            self.api_id, self.api_hash, self.admin_id, self.target1 = [
                i.strip() for i in f.readlines() if i != "\n" and i[0] != "#"
            ]

        self.app = Client("FreeFood", self.api_id, self.api_hash)
        self.self_ = []
        self.delay = 0.5

        self.process()
        self.runner()
        self.app.run()

    def process(self):
        @self.app.on_message(filters.chat(int(self.target1)))
        async def process(client, m: pyrogram.types.messages_and_media.message.Message):
            if self.self_ and any([checker(m.text, i) for i in self.self_]):
                self.self_ = []
                await self.app.send_message(self.admin_id, "انجام شد.")

                await asyncio.sleep(self.delay)
                await m.reply("استفاده")

                await asyncio.sleep(self.delay)
                await self.app.send_message(
                    m.from_user.id,
                    choice(
                        [
                            "من میتونم غذاتون رو استفاده کنم؟",
                            "کد رو میفرستید",
                            "کد رو محبت میکنید؟",
                            "سلام. غذا دارید؟",
                            "سلام\nکد دارید؟",
                            "ممنون میشم غذاتون رو بدید به من",
                            "سلام غذاتونو میدید به من",
                        ]
                    ),
                )

    def runner(self):
        @self.app.on_message(filters.chat(self.admin_id))
        async def runner(client, m: pyrogram.types.messages_and_media.message.Message):
            if m.text.split()[0] == "delay":
                self.delay = float(m.text.split()[1])
                await m.reply(f"delay set to {self.delay}")
            elif m.text == "OFF":
                self.self_ = []
                await m.reply("کنسل شد.")
            elif self.self_:
                await m.reply("ربات در حال اجرا است. صبور باشید.")
            elif set(m.text.split()).issubset(
                {"FAN1", "FAN2", "MEHR", "MODR", "OLUM", "HONR"}
            ):
                self.self_ = m.text.split()
                await m.reply("درحال انجام ...")
            else:
                await m.reply("متوجه نشدم :(")


if __name__ == "__main__":
    Run()

    # with open(path.join(".", "target", "config.txt"), "r") as f:
    #     api_id, api_hash, admin_id, target1 = [
    #         i.strip() for i in f.readlines() if i != "\n" and i[0] != "#"
    #     ]
    # app = Client("FreeFood", api_id, api_hash)

    # async def main():
    #     async with app:
    #         async for dialog in app.get_dialogs():
    #             print(dialog.chat.title or dialog.chat.first_name, dialog.chat.id)

    # app.run(main())
