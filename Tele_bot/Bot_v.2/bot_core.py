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

if __name__ == "__main__":
    bot.run()