from rich.console import Console
from addacc import app
from asyncio import sleep
from pyrogram import filters, enums

console = Console()

menu = console.input('''
[white]|1| [red]Get chat members
[white]|2| [red]Get chat administrators[white]

> ''')

if menu == "1":
   chat_id = int(
    console.input('[red]CHAT ID: ')
   )
   async def main():
         async with app:
               async for member in app.get_chat_members(chat_id):
                     console.print('[bold red]First name: [white]{}\n[bold red]Last name: [white]{}\n[bold blue]Username: [white]@{}\n[bold magenta]Phone: [white]{}\n'.format(
                          member.user.first_name,
                          member.user.last_name,
                          member.user.username,
                          member.user.phone_number
                
                          )
                     )

elif menu == "2":
     chat_id = int(console.input('[red]CHAT ID: '))
     async def main():
          async with app:
                administrators = []
                async for admins in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
                      administrators.append(admins)
                      console.print(f'{admins.user.first_name} > [red]ADMIN')
            
app.run(main())
