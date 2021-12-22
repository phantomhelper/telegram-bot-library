from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

genres = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Ламповое", callback_data="ламповое")
        ],
        [
            InlineKeyboardButton(text="Крипипаста", callback_data="крипипаста")
        ]
    ]
)
