from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мне повезет ⭐️', callback_data="menu:random"),
            KeyboardButton(text='Полка 📚', callback_data="menu:my_shelf"),
            KeyboardButton(text='По жанрам 🎭', callback_data="menu:by_genre")
        ]
    ],
  resize_keyboard=True
)
