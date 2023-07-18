from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Main menu')

# Главное меню
btnRandom = KeyboardButton('Random number')
btnOther = KeyboardButton('Others')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnOther, btnRandom)

# Другое меню
btnJoke = KeyboardButton('Joke')
btnInfo = KeyboardButton('Information')
btnAbout = KeyboardButton('About')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnAbout, btnJoke, btnMain)