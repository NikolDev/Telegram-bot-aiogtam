#Import all files for work
import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

import random

#Paste your token bot
TOKEN = 'Here your token'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#Code in 12 line reply to message start
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
  await bot.send_message(message.from_user.id, 'Hi {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)

#After writes reply on button
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

    #If command !== name button - bot reply 'I don't understand you'
    else:
        await message.reply("I don't understand you")

#Just run your bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
