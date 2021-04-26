from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

rating = InlineKeyboardMarkup(
    inline_keyboard=[
        [
#            InlineKeyboardButton(text="Читать полностью", url="google.com")
#        ],
#        [
            InlineKeyboardButton(text="👎", callback_data="rating:down"),
            InlineKeyboardButton(text="❤️", callback_data="rating:add"),
            InlineKeyboardButton(text="👍", callback_data="rating:up")

        ]
    ]
)

# 👎❤️👍
