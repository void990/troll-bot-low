from pyrogram import Client, filters
from rich.console import Console
from addacc import app
from asyncio import sleep
import rich
import random

console = Console()

file = open('words.txt', 'r')
text = file.read().split('\n')
file.close()

console.print('''[bold white]
Copyright (C) 2022  https://github.com/void990/troll-bot
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
''')

chat_id = int(console.input(
       '[bold white]chat id >> '
       )
)

delay = int(console.input(
      '[bold red]delay >> '
      )
)

@app.on_message(filters.chat(int(chat_id)))
async def troiing(client, message):
      await sleep(delay)
      await message.reply(random.choice(text))
      console.log(f'reply: {message.text}')
      
app.run()
