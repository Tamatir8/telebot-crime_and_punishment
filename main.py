import telebot

bot = telebot.TeleBot('5457853365:AAGEz8Yp8LPfQOO3_ATHC2pQoadAxhIgyo0')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую, дорогой любитель русской классики! В данном чате ты можешь сыграть в '
                                      'визуальную новеллу, основанную по произведению Фёдора Михайловича Достоевского '
                                      '"Преступление и наказание". Начнём!')

bot.polling(none_stop=True)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Начинаем!':
        bot.send_message(message.chat.id, "Раскольников стоял перед дверью старухи-процентщицы.")
    else:
        bot.send_message(message.chat.id, "Извините, но я вас не понимаю.")
