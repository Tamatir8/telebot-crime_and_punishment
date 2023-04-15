import telebot
from telebot import types

bot = telebot.TeleBot('5457853365:AAGEz8Yp8LPfQOO3_ATHC2pQoadAxhIgyo0')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Приветствую, дорогой любитель русской классики! В данном чате ты можешь сыграть в '
                     'визуальную новеллу, основанную по произведению Фёдора Михайловича Достоевского '
                     '"Преступление и наказание". В ней вы играете за главного героя романа, Родиона '
                     'Романовича Раскольникова. Начнём! Как же пойдёт ваша история?')
    markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("Начинаем!")
    markup0.add(btn0)
    bot.send_message(message.chat.id, text='Нажми. чтобы начать', reply_markup=markup0)


@bot.message_handler()
def get_user_text(message):
    if message.text == 'Начинаем!':
        bot.send_message(message.chat.id, "Вы наконец-то добрались до осуществления своего плана. Вы готовились к нему "
                                          "больше месяца, так что ничто не сможет пойти не так, даже удача сегодня на вашей стороне. "
                                          "Остался всего один шаг, и вы наконец узнаете, можете ли называть себя "
                                          "человеком «необыкновенным».")
        bot.send_message(message.chat.id, "Ваша рука лежит на спрятанном топоре и остался всего один шаг, и вы точно "
                                          "узнаете, можете ли называть себя человеком «необыкновенным».")

        # стоит перед дверью в самом начале
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton("Нет")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Но готовы ли вы к этому шагу?', reply_markup=markup)

        # сразу решает убить старуху
    elif (message.text == "Да"):
        bot.send_message(message.chat.id,
                         "Молодой человек постучался и попросил старуху пустить его. Он отдал ей ложный "
                         "злад и когда она отвернулась достал топор. Он взмахнул и ударил свою жертву. "
                         "Раскольников, весь в крови, смотрел, как из головы старухи текла кровь. "
                         "Посмотрев пару секунд, он побежал и начал искать вещи.")
        bot.send_message(message.chat.id, "Неожиданно он слышит, как открывается входная дверь. Лизавета, сестра"
                                          " этой женщины от шока не может ничего сказать и испуганными глазами смотрит "
                                          "на Раскольникова.")

        # убить или не убить Лизавету
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Убить Лизавету")
        btn2 = types.KeyboardButton("Не убить Лизавету")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Никто не должен узнать, что это вы убили старуху-процентщицу.'
                                               ' Вам нужно избавиться от свидетелей.', reply_markup=markup)
    elif (message.text == "Убить Лизавету"):
        bot.send_message(message.chat.id, "Паника Раскольникова. Забрал вещи и сбежал. и т.д.")
        bot.send_message(message.chat.id, "Разговаривает с Соней и то говорит ему, что надо признаться.")

        # слушать или не слушать соню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Слушать Соню")
        btn2 = types.KeyboardButton("Не слушать Соню")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='ваш поступок ужасен, но вы не хотите признаваться. Что же делать?',
                         reply_markup=markup)

        # концовка Вы тварь дрожащая
    elif (message.text == "Слушать Соню"):
        bot.send_message(message.chat.id, "Вы идёте с повинной. Потом каторга. Плачете на коленках у Сони.")
        bot.send_message(message.chat.id, "Вы получили оригинальную концоку. Концовка: Вы тварь дрожащая!")

        # не слушает Соню и решает убивать или нет
    elif (message.text == "Не слушать Соню"):
        bot.send_message(message.chat.id, "Вы не идёте с повинной. Не хотите отправляться на каторгу. Нужнр бежать. "
                                          "Но нельзя же так всё оставлять.")

        # бежать или остаться
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Бежать")
        btn2 = types.KeyboardButton("Остаться")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Как же вам следует поступить: бросить всё и воспользоваться помощью '
                                               'Свидригайлова или остаться в Петерурге и продолжить жить дальше?',
                         reply_markup=markup)

        # концовка Теория доказана, но какой ценой?
    elif (message.text == "Остаться"):
        bot.send_message(message.chat.id, "Вы впадаете в депрессию. Умираете.")
        bot.send_message(message.chat.id, "Концовка: Теория доказана, но какой ценой?")

        # бежать за границу и три концовки
    elif (message.text == "Бежать"):
        bot.send_message(message.chat.id,
                         "Вы решаете бежать за границу, да куда угодно, лишь бы подальше от этого города.")
        bot.send_message(message.chat.id, "А как же теория? Так вы тварь дрожащая или обыкновеннный человек?")

        # выбор одной из трёх концовок
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Убивать ради теории")
        btn2 = types.KeyboardButton("Убивать ради блага")
        btn3 = types.KeyboardButton("Жить спокойно")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text='Как жить дальше? Ничего не делать и успокоиться, доказать себе, '
                                               'что вы Наполеон? Или же вы всё ещё не уверены, что вы человек'
                                               ' необыкновенный?', reply_markup=markup)

        # концовка Кто же ты?
    elif (message.text == "Убивать ради теории"):
        bot.send_message(message.chat.id, "Вы не уверены в себе. Продолжаете убивать.")
        bot.send_message(message.chat.id, "Концовка: Кто же ты?")

        # концовка Вы Наполеон!
    elif (message.text == "Убивать ради блага"):
        bot.send_message(message.chat.id, "Вы уверены в себе. Продолжаете убивать, чтобы помочь нуждающимся.")
        bot.send_message(message.chat.id, "Концовка: Вы Наполеон!")

        # концовка Вы Наполеон без прав!
    elif (message.text == "Жить спокойно"):
        bot.send_message(message.chat.id,
                         "Вы решаете, что нужно начать жизнь с чисттго листа ии решаете продолжить спокойно жить.")
        bot.send_message(message.chat.id, "Концовка: Вы Наполеон без прав!")

        # концовка Вы тварь дрожащая
    elif (message.text == "Не убить Лизавету"):
        bot.send_message(message.chat.id, "Раскольников не смог. Он бросил топор на землю и опустился на землю. "
                                          "Лизавета медленно отступила и убежала. Через пару минут вернулась с дворником.")
        bot.send_message(message.chat.id, "Потом суд и каторга. Концовка: Вы тварь дрожащая!")

    elif message.text == "Нет":
        bot.send_message(message.chat.id, "Вы поднимаете руку, но в последний момент отдёргиваете её от двери. Что-то "
                                          "внутри вас не даёт пойти на такой поступок. «Но я же так долго готовился,» - "
                                          "думаете вы и осторожно оглядываетесь по сторонам. «Кто-то может прийти, нужно"
                                          " сделать всё быстро.» Снова сжав руку в кулак и подняв её к двери, "
                                          "вы глубоко вздыхаете…")

        # решает идти ли на убийство старухи
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Стучать")
        btn4 = types.KeyboardButton("Не стучать")
        markup1.add(btn3, btn4)
        bot.send_message(message.chat.id, text='Обратного пути нет будет. Стучать или не стучать?',
                         reply_markup=markup1)

    elif message.text == "Стучать":
        bot.send_message(message.chat.id, "Раскольников, весь в крови, смотрел, как из головы старухи текла кровь. "
                                          "Посмотрев пару секунд, он побежал и начал искать вещи.")

        # концовка "Вы мёртвая тварь дрожащая!"
    elif message.text == "Не стучать":
        bot.send_message(message.chat.id,
                         "… и несётесь прочь, подальше от комнаты старухи-процентщицы. Вы не понимаете,"
                         " какая неведомая сила заставила вас передумать. Может, это страх? Или совесть? "
                         "А может, всё это с самого начала было совершенно глупой затеей? Или же вы "
                         "всё-таки просто обыкновенный человек, не способный изменить мир?")
        bot.send_message(message.chat.id, "Погрузившись в собственные мысли, вы не замечаете, как доходите до "
                                          "своей комнаты. Закрыв дверь, вы вытаскиваете из-под пальто топор и задумчиво"
                                          " его разглядываете.")
        bot.send_message(message.chat.id, "«Да, это с самого начала была бессмысленная затея,» - думаете вы, опуская "
                                          "топор на пол. «Я такой же обыкновенный, как и все они, тут и проверять нечего.» "
                                          "Вы выходите из комнаты и уходите в неизвестном для себя направлении. "
                                          "Вас уже не волнует грязь на улицах, пьяницы, вываливающиеся из трактиров, "
                                          "исхудавшие лошади, запряжённые в повозки. Вас угнетает мысль о том, что не в ваших "
                                          "силах перевернуть мир с ног на голову.")
        bot.send_message(message.chat.id, "Со временем вы подходите к мосту, доходите до его середины…")

        markupend1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnend1 = types.KeyboardButton("Посмотреть в воду")
        markupend1.add(btnend1)
        bot.send_message(message.chat.id, text='Нажмите', reply_markup=markupend1)
    elif message.text == "Посмотреть в воду":
        bot.send_message(message.chat.id, "...и наклоняетесь к воде. Оттуда на вас смотрит самый обыкновенный из всех "
                                          "обыкновенных людей, и вам становится уже невыносимо от этой мысли, но вы всё"
                                          " продолжаете и продолжаете смотреть на своё отражение, наклоняясь всё ниже, "
                                          "пока полностью не сливаетесь с ним.")
        bot.send_message(message.chat.id, "Концовка: «Вы мёртвая тварь дрожащая!»")
        file = open('мёртвая тварь дрожащая.jpg', 'rb')
        bot.send_photo(message.chat.id, file, "«Вы мёртвая тварь дрожащая!»")

        markupsecr = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btnsecr = types.KeyboardButton("...")
        markupsecr.add(btnsecr)
        bot.send_message(message.chat.id, text='Это конец... наверно...', reply_markup=markupsecr)
    elif message.text == "...":
        bot.send_message(message.chat.id, "БУЛЬ БУЛЬ КАРАСИКИ, ВОТ И КОНЕЦ ЭТОЙ ДИВНОЙ ИСТОРИИ")


bot.polling(none_stop=True)