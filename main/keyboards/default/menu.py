from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мне повезет ⭐️'),
            KeyboardButton(text='Полка 📚')
        ]
    ],
  resize_keyboard=True
)
