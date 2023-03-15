import telegram

import config1

token = config1.id
bot = telegram.Bot(token)
updates = bot.getUpdates()
for u in updates:
    print(u.message)