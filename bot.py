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
	item2 = types.KeyboardButton("🧡 Your QA matches")
	item3 = types.KeyboardButton("📱 Get in touch with your match")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Welcome, {0.first_name}! If you are here, it means that you are looking for a perfect QA match.\nPlease first tap on '🔎 Find the 🔝 QA'".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == "🔎 Find the 🔝 QA":
			bot.send_message(message.chat.id, "You've got a new QA match!🔥\nTo check the result, please tap on\n'🧡 Your QA matches'")
		if message.text == "🧡 Your QA matches":
			bot.send_message(message.chat.id, "🎉Congratulations, you've found the 🔝 QA tester!\nName: Violetta Lukashevich\nAge: 28\nCountry of residence: Belgium\nAbout: Responsible, detail-oriented, communicative. I like to analyze everything, both in life and in work, so I can find the root cause of any problem, both mental and techical :). Sense of humor and openness are the most important human qualities for me. In my spare time, you can find me studying foreign languages, traveling, watching videos about Selenium automation, or growing cucumbers.\nTo contact Violetta, please tap on '📱 Get in touch with your match'")
		if message.text == "📱 Get in touch with your match":
			bot.send_message(message.chat.id, "Email: lukashevich.violetta@gmail.com\nPhone: 0488300167\nWas nice to meet you, {0.first_name}! 🤗 Have a great day and see you later!☀️")


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods