import telebot

bot = telebot.TeleBot("6137643802:AAFgksPRg8IpOBG3DIThU6i_tINtW5WT7Cw")

@bot.message_handler(commands=['start'])
def start_menu(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton('Имя пользователя'))
    keyboard.add(telebot.types.KeyboardButton('Лента заданий'))
    keyboard.add(telebot.types.KeyboardButton('Баланс'))
    keyboard.add(telebot.types.KeyboardButton('Создать задание'))
    keyboard.add(telebot.types.KeyboardButton('Принять задание'))
    keyboard.add(telebot.types.KeyboardButton('Выйти'))

    bot.send_message(message.chat.id, 'Добро пожаловать в игру "Do It on Time"!', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Имя пользователя')
def set_username(message):
    bot.send_message(message.chat.id, 'Введите ваше имя в игре:')

# Добавьте обработчик для сохранения имени пользователя

bot.polling()
