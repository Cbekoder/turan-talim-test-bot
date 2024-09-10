from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def test_buttons(test):
    buttons = [[]]
    for option in test["options"]:
        buttons[0].append(
            InlineKeyboardButton(text=option, callback_data=f"test:{option}:{test["answer"]}")
        )
    markup = InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return markup