
from copyreg import dispatch_table
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import list

import config1

token = config1.token
id=config1.id

bot=telegram.Bot(token)
bot.sendMessage(chat_id=id, text="'help', '도움', '?'를 입력해 도움 받기")

updater=Updater(token=token, use_context=True)
dispatcher=updater.dispatcher
updater.start_polling()



def handler(update, context):
    user_text=update.message.text
    
    if user_text=="help" or user_text=="도움" or user_text=="?":
        context.bot.send_message(chat_id=id, text=list.help_return)

    elif user_text=="안녕":
        context.bot.send_message(chat_id=id, text="안녕하세요")

    elif user_text=="hello" or user_text=="Hi":
        context.bot.send_message(chat_id=id, text="Hello")

    elif user_text == "학교"or user_text == "school" :
        context.bot.send_message(chat_id=id, text="홈페이지\n리로스쿨\n급식\n수행평가")

    elif user_text == "홈페이지" :
        context.bot.send_message(chat_id=id, text="[대건고등학교 홈페이지](http://daegun.hs.kr)", parse_mode= 'Markdown')

    elif user_text == "리로스쿨" :
        context.bot.send_message(chat_id=id, text="[대건고등학교 리로스쿨](https://daegun.riroschool.kr/)", parse_mode= 'Markdown')

    elif user_text == "급식" :
        context.bot.send_message(chat_id=id, text="[대건고등학교 급식](https://url.kr/s98rdn)", parse_mode= 'Markdown')

    elif user_text == "수행평가" :
        context.bot.send_message(chat_id=id, text="[이번주 수행평가](193.123.237.18/process_judge.html)", parse_mode= 'Markdown')


echo_handler=MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)