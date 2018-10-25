from bot import telegram_chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = telegram_chatbot("config.cfg")


def make_reply(msg):
	reply = None
	if msg is not None:
		if msg.strip() != 'bye':
			reply = bot1.get_response(msg)
			return reply	
		if msg.strip() == 'Bye':
			reply = 'bye'
			return reply					
update_id = None
bot1 = ChatBot('Bot')
bot1.set_trainer(ListTrainer)
x = os.path.join( '//home', 'xerous' , 'Desktop' , 'chatbot' , 'chatterbot-corpus','chatterbot_corpus' , 'data' , 'english/')
for files in os.listdir (x):
	data = open(x + files , 'r').readlines()
	bot1.train(data)
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
