




















@dp.message_handler(commands=['add'])
async def add_title(message: Message):
    if message.chat.id in admins:
        await message.answer(text='Заголовок:')
        await passage.title.set()
        print(message.text)

@dp.message_handler(state=passage.title)
async def add_brief(message: Message, state: FSMContext):
    await message.answer(text='Краткий рассказ:')
    await passage.brief.set()
