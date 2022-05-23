#библиотеки, которые загружаем из вне
import telebot
TOKEN = '5355659877:AAEEf0XcVUVnQ5WKrNP5NUjn_Ih3-CICIVM'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🔎 Find the 🔝 QA")

	markup.add(item1)

	bot.send_message(message.chat.id, "Welcome, {0.first_name}! If you are here, it means that you are looking for a perfect QA match. Let’s start then! Please tap on 🔎 ".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🔎 Find the 🔝 QA':
			bot.send_message(message.chat.id, '🕵️‍♂️ here I am')
	
      
  



bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods