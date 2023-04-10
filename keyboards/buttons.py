from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_KEYBOARDS
from data.user_data import usr_dict


def create_group_list_kb(groups_dict: dict[dict[str, str]]) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    groups_names = list(groups_dict.keys())
    btns: list[InlineKeyboardButton] = [InlineKeyboardButton(
        text=group_name,
        callback_data=group_name) for group_name in groups_names]
    kb_builder.row(*btns, width=1)
    return kb_builder.as_markup()

