import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

import random

TOKEN = '5457559759:AAHErKuopsbNNsZomX0V1owpuryPOABI76g'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
  await bot.send_message(message.from_user.id, 'Hi {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_mwssage(message: types.Message):
    if message.text == 'Random number':
        await bot.send_message(message.from_user.id, 'Your number: ' + str(random.randint(1, 10)))

    elif message.text == 'Information':
        await bot.send_message(message.from_user.id, 'I am a bot')

    elif message.text == 'About':
        await bot.send_message(message.from_user.id, 'Author\nVersion\nDonate')

    elif message.text == 'Joke':
        await bot.send_message(message.from_user.id, 'JavaScript is good programming language')

    elif message.text == 'Main menu':
        await bot.send_message(message.from_user.id, 'Main menu', reply_markup=nav.mainMenu)

    elif message.text == 'Others':
        await bot.send_message(message.from_user.id, 'Others', reply_markup=nav.otherMenu)

    else:
        await bot.send_message(message.from_user.id, 'I dont understand you')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)