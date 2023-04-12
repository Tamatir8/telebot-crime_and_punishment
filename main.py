import telebot
from telebot import types

bot = telebot.TeleBot('5457853365:AAGEz8Yp8LPfQOO3_ATHC2pQoadAxhIgyo0')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую, дорогой любитель русской классики! В данном чате ты можешь сыграть в '
                                      'визуальную новеллу, основанную по произведению Фёдора Михайловича Достоевского '
                                      '"Преступление и наказание". Начнём!')
    bot.send_message(message.chat.id,'Напиши "Начинаем!"')

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Начинаем!':
        bot.send_message(message.chat.id, "Раскольников стоял перед дверью старухи-процентщицы.")
        bot.send_message(message.chat.id, "Она открыла ему дверь, взяла заклад, а Раскольников окончательно "
                                          "решил:")

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Убить")
        btn2 = types.KeyboardButton("Не убить")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='От вас зависит жизнь этой женщины. Что же вы сделаете?',reply_markup=markup)
    elif (message.text == "Убить"):
        bot.send_message(message.chat.id, "Раскольников, весь в крови, смотрел, как из головы старухи тексла кровь. "
                                              "Посмотрев пару секунд, он побежал и начал искать вещи.")

    elif message.text == "Не убить":
        bot.send_message(message.chat.id, "Раскольников спрятал топор и быстро вышел из квартиры. Он не смог, "
                                          "он слишком слаб!")



bot.polling(none_stop=True)
