from pyrogram import Client, filters, enums
from rich.console import Console
from addacc import app
from asyncio import sleep
import rich
import random
from config import trigger

console = Console()

file = open('words.txt', 'r')
text = file.read().split('\n')
file.close()

console.print('''[bold white]
Copyright (C) 2022  https://github.com/void990/troll-bot-low
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.

[bold red]TEST VERSION [!]
''')

flood = console.input('[bold red]flood mode? [purple]|y/n| ')

try:
   if flood == "y":
      count = int(console.input('[red]count message: '))
      chat_id = int(console.input('[bold white]chat or user id >> '))
      delay = int(console.input('[magenta]delay >> '))
      console.print('[bold red][+] [white]Send to !{} chat'.format(trigger))
      
      @app.on_message(filters.command(trigger, prefixes="!"))
      async def flood_troll(client, message):        
            for i in range(count):
                await sleep(delay)
                await app.send_message(chat_id, random.choice(text))
                console.log(f'[green]sended -> [white]{i}')
  
   elif flood == "n":
        chat_id = int(console.input('chat or user id >> '))
        delay = int(console.input('[red]delay >> '))
        
        @app.on_message(filters.chat(chat_id))
        async def trolling(client, message):
             await app.send_chat_action(
                    chat_id,
                    enums.ChatAction.TYPING
             )
                
             await sleep(delay)
             await message.reply(random.choice(text))
             
             console.log('{} -> {}'.format(
                chat_id,
                message.text
                )
             )
                
except Exception as error:
       console.print(f'[red]ERROR: {error}')

      
app.run()
