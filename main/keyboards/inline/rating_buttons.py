from  aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import rating_callback

rating = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="test:one"),
            InlineKeyboardButton(text="2", callback_data="test:two")
        ],
        [
            InlineKeyboardButton(text="3", callback_data="test:three")
        ]
    ]
)
