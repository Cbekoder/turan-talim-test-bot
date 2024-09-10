from aiogram.types import Message
from utils.api_request import send_request
from loader import dp

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        # Send a copy of the received message
        response = send_request(message.text)
        await message.answer(response)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")