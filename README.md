# Telegram Bot | Library
### English version avaliable [>here<](README_eng.md)

## Что это за бот?
### **Бот написан на _aiogram_**

Немного истории. Это бот сделан на заказ, после которого человек не выходил на связь,
поэтому не пропадать ведь добру и дать в руки комьюнити.

По сути, это бот, в который Вы можете загрузить свои книги, отрывки из текста
и каждый день в определенное время бот будет случайно выбирать из базы данных
(MongoDB) отрывок и отправлять _всем_ пользователям. 

## Запуск бота
- Открыть консоль;
- _Прочитать и заменить файл_ (`.env.dist`)[.env.dist]
- `python app.py`

## Детальнее про базу данных
| Название в коде | Описание |
| --- | --- |
| client['telegram-bot-library'] | Название базы данных, где будут хранится коллекции.
| db['users'] | Коллекция, где собраны все пользователи.
| db['passages'] | Коллекция, где собраны все загруженные отрывки.
| db['users_shelf'] | Коллекция с личной полкой для каждого пользователя.
| db['messages'] | Коллекция где собраны отправленные сообщения (`MessageID` и отрывок). Используется в коде.

## Детали про бота
| Аргумент | Значение | PATH |
| --- | --- | --- |
| time_day | 09:00 AM (local time) | `handlers\users\daily_msg.py`|
| time_day| `str(time.strftime("%H:%M", time.localtime()))` | `handlers\users\daily_msg.py`|
| time_night | 08:00 PM (local time) | `handlers\users\daily_msg.py`|


## Требования
- (`Python 3.x`)[https://www.python.org/]
- (MongoDB)[https://www.mongodb.com/]
- Установлен (`aiogram`)[https://github.com/aiogram/aiogram]

## Референсы
- (aiogram)[https://github.com/aiogram/aiogram]
- (Пустая структура проекта)[https://youtu.be/fob8oQOjB2Q]

