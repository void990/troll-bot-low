from pyrogram import Client
from rich.console import Console
from config import api_id, api_hash
import rich

console = Console()

app = Client(
    "my_acc",
    api_id,
    api_hash
)
with app:
     me = app.get_me()
     console.log(f'{me.first_name} {me.id}')
