import time
import json
import asyncio
import logging
from aiogram import types
from threading import Thread
from keyboards.default import menu
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, db_users, db_passagese, db_messages, db_users_shelf
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton, MediaGroup
from aiogram.utils import exceptions, executor

from handlers.users.start import _random_passage
