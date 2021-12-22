# Telegram Bot | Library
### Russian version avaliable [>here<](README.md)

## What does this bot?
### **Bot is written using _aiogram_**

A little story. This is a custom made bot for a client, who did not
come online pretty long time. So, I am ready to give this bot to the GitHub community.

Actually, you can upload your books, text passages and this bot sends a random
passage to _all users_ at 9am and 8pm everyday. An user can save this message by clicking a button,
and raise or downgrade a rating. 


## Start
- Open CMD;
- _Read and modify this file_ `.env.dist`
- `python app.py`

## Details about DateBase
| Name | Description |
| --- | --- |
| client['telegram-bot-library'] | Main DateBase, where are collections.
| db['users'] | Collection, which has users' information for Telegram.
| db['passages'] | Collection, which has uploaded passages.
| db['users_shelf'] | Collection with a personal shelf.
| db['messages'] | Collection which has send messages (`MessageID` and passage). Using in the code.

## Details about the bot
| Argument | Value | PATH |
| --- | --- | --- |
| time_day | 09:00 AM (local time) | `handlers\users\daily_msg.py`|
| time_day| `str(time.strftime("%H:%M", time.localtime()))` | `handlers\users\daily_msg.py`|
| time_night | 08:00 PM (local time) | `handlers\users\daily_msg.py`|


## Requirements
- `Python 3.x`
- `MongoDB`
- Installed `aiogram`

## References
- https://github.com/aiogram/aiogram
- Empty bot structure - https://youtu.be/fob8oQOjB2Q

