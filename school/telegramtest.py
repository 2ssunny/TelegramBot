import telegram

import config1
token = config1.token
id=config1.id

bot=telegram.Bot(token)
bot.sendMessage(chat_id=id, text="Hello World")