from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)

def start(bot, update):
	text = 'Вызван /start'
	print(1/0)
	update.message.reply_text(text)

def talk_to_me(bot, update):
	user_text = update.message.text
	print(user_text)
	update.message.reply_text(user_text)

def main():
	updater = Updater("503178796:AAGv5Rw9ZhXQJu4jOYkgOGqkPyEDLdXwV5s")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))


	updater.start_polling()
	updater.idle()

main()


	


