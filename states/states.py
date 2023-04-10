from aiogram.filters import StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

storage: MemoryStorage = MemoryStorage()

class FSMUserStates(StatesGroup):
    creating_group_name = State()
    creating_words = State()
    looking = State()
    training = State()