from pprint import pprint

from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, StateFilter
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON_COMMANDS
from data.user_data import usr_dict
from states.states import FSMUserStates, storage, FSMContext

router: Router = Router()


# router.message.filter()

@router.message(CommandStart())
async def start_com(message: Message):
    await message.answer(LEXICON_COMMANDS['/start'])
    if message.from_user.id not in usr_dict:
        usr_dict[message.from_user.id] = {}
    pprint(usr_dict)


@router.message(Command(commands='help'))
async def help_com(message: Message):
    await message.answer(LEXICON_COMMANDS['/help'])


@router.message(Command(commands='create'))
async def create_com(message: Message, state: FSMContext):
    await message.answer(LEXICON_COMMANDS['/create'])
    await state.set_state(FSMUserStates.creating_group_name)


@router.message(StateFilter(FSMUserStates.creating_group_name))
async def create_words(message: Message, state: FSMContext):
    group_name: str = message.text
    await state.update_data(group_name=group_name)
    usr_dict[message.from_user.id][group_name] = {}
    print(usr_dict)
    await message.answer(text='Great\!\nInput the words')
    await state.set_state(FSMUserStates.creating_words)

@router.message(StateFilter(FSMUserStates.creating_words), Text(text='DONE'))
async def stop_creating_words(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text='SAVED')
    print(usr_dict)

@router.message(StateFilter(FSMUserStates.creating_words))
async def create_words(message: Message, state: FSMContext):
    data = await state.get_data()
    group_name: str = data.get('group_name')
    word, meaning = message.text.split(',')
    usr_dict[message.from_user.id][group_name].setdefault(word.strip(), meaning.strip())
    print(usr_dict)
    await message.answer(text='Ok\!\nInput the next. If you need stop and save, input "DONE"')

@router.message(Command(commands='look'))
async def look_com(message: Message):
    await message.answer(LEXICON_COMMANDS['/look'])
