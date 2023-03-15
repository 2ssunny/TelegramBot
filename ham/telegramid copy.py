import telegram

import configham

token = configham.token
bot = telegram.Bot(token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)