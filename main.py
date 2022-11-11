from datetime import datetime
from json import dump

from pyrogram import Client

with open(".\\target\\config.txt", "r") as f:
    api_id, api_hash, admin_id, target1 = [
        i.strip() for i in f.readlines() if i[0] != "#"
    ]

app = Client(
    "FreeFood",
    api_id,
    api_hash,
    proxy={"scheme": "socks5", "hostname": "127.0.0.1", "port": 9051},
)


async def main():
    out = set()
    async with app:
        async for chat in app.get_chat_history(target1):
            if chat.date < datetime(2022, 9, 18, 0, 0, 0):
                break
            out.add(chat.text)
        print(chat.date)
    with open("out.json", "a", encoding="utf-8") as f:
        dump(list(out), f, ensure_ascii=False)


if __name__ == "__main__":
    app.run(main())
