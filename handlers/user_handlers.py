from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON_COMMANDS

router: Router = Router()
# router.message.filter()

@router.message(CommandStart())
async def start_com(message: Message):
    await message.answer(LEXICON_COMMANDS['/start'])

@router.message(Command(commands='help'))
async def help_com(message: Message):
    await message.answer(LEXICON_COMMANDS['/help'])

@router.message(Command(commands='create'))
async def create_com(message: Message):
    await message.answer(LEXICON_COMMANDS['/create'])

@router.message(Command(commands='look'))
async def look_com(message: Message):
    await message.answer(LEXICON_COMMANDS['/look'])
