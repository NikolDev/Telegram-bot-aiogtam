<h1>Telegram-bot</h1>
<h3>This is not a big telegram bot created in Python with the ability to change data. It has a menu, menu navigation, and buttons.</h3>
<img src='/pyth.png' alt='python image' width='1080' height='500'>

First you need to install all the necessary files
<a href='https://pypi.org/project/aiogram/'>aiogram</a>

<b>1 - Then we import the necessary files</b>
<pre>
1. import logging
2. from aiogram import Bot, Dispatcher, executor, types
3. import markups as nav
</pre>

<b>2 - Next, we prescribe the TOKEN and look for the BotFazer in telegrams. We create a new bot there, set the name and username. BotFaser will send us a long code, this is our token, copy it and paste it into the TOKEN area</b>
<pre>
7. TOKEN = 'Here your token'
</pre>

<b>3 - The first function responds to the "start" command. She takes the first telegram username and adds Hi. It also adds menus and buttons.</b>
<pre>
12.  @dp.message_handler(commands=['start'])
13.  async def command_start(message: types.Message):
14.    await bot.send_message(message.from_user.id, 'Hi {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)
</pre>

<b>4 - The next function is to watch for messages. Well, the conditions are already below, if the message is equal to the name that we set in murkups, then the bot responds taking into account the given instructions. At the very bottom, else, means that if you write an unknown name or random text, it will respond with the given text, in my case "I don't understand what you want"</b>
<pre>
16. @dp.message_handler()
17. async def bot_mwssage(message: types.Message):
18.    if message.text == 'Random number':
19.       await bot.send_message(message.from_user.id, 'Your number: ' + str(random.randint(1, 10)))
20.
21.    elif message.text == 'Information':
22.        await bot.send_message(message.from_user.id, 'I am a bot')
23.
24.    elif message.text == 'About':
25.        await bot.send_message(message.from_user.id, 'Author\nVersion\nDonate')
26.
27.    elif message.text == 'Joke':
28.        await bot.send_message(message.from_user.id, 'JavaScript is good programming language')
29.
30.    elif message.text == 'Main menu':
31.        await bot.send_message(message.from_user.id, 'Main menu', reply_markup=nav.mainMenu)
32.
33.    elif message.text == 'Others':
34.        await bot.send_message(message.from_user.id, 'Others', reply_markup=nav.otherMenu)
35.
36.    else:
37.        await bot.send_message(message.from_user.id, 'I dont understand you')
</pre>

<b>5 - The last lines simply launch the bot.</b>
<pre>
39.  if __name__ == '__main__':
40.    executor.start_polling(dp, skip_updates=True)
</pre>

If something is not clear here, you can watch the video on YouTube (it is in Russian). I hope you liked my version of the code and appreciate it, thanks for your attention!
<a href='https://youtu.be/njfkrf1H6XM'>Watch video</a>
