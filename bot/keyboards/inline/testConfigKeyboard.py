from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

langsButton = InlineKeyboardMarkup(
    # row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="UZ 🇺🇿", callback_data="lang:UZ"),
            InlineKeyboardButton(text="TR 🇹🇷", callback_data="lang:TR"),
            InlineKeyboardButton(text="EN 🇬🇧", callback_data="lang:EN")
        ]
    ]
)

levelsButton = InlineKeyboardMarkup(
    # row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="A1", callback_data="level:A1"),
            InlineKeyboardButton(text="A2", callback_data="level:A2"),
        ],
        [
            InlineKeyboardButton(text="B1", callback_data="level:B1"),
            InlineKeyboardButton(text="B2", callback_data="level:B2"),
        ],
        [
            InlineKeyboardButton(text="C1", callback_data="level:C1"),
            InlineKeyboardButton(text="C2", callback_data="level:C2"),
        ]
    ]
)

countsButton = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="10", callback_data="count:10"),
            InlineKeyboardButton(text="20", callback_data="count:20"),
            InlineKeyboardButton(text="30", callback_data="count:30"),
            InlineKeyboardButton(text="40", callback_data="count:40")
        ]
    ]
)