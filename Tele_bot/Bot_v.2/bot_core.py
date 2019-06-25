import botogram
import datetime
bot = botogram.create("758922168:AAEFekW7CIaE8tjlEOw7nu3V1Zm7_J9kQaQ")

@bot.command("hello")
def hello_command(chat, message, args):
    chat.send("Hello world")

@bot.command("time")
def time(chat ,message , args):
        x = str(datetime.datetime.now())
        chat.send(x)

@bot.command("spam")
def spam_command(chat , message , args):
        bts = botogram.Buttons()
        bts[0].callback("Delete this message" , "Delete")

        chat.send("This is  spam" , attach=bts)
@bot.callback('Delete')
def Delete_callback(query , chat ,message):
        message.delete()
        query.notify("Spam message deleted . Sorry!")
if __name__ == "__main__":
    bot.run()