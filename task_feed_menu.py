import telebot

bot = telebot.TeleBot("6137643802:AAFgksPRg8IpOBG3DIThU6i_tINtW5WT7Cw")

@bot.message_handler(commands=['start'])
def start_menu(message):
    # ... код главного меню ...

@bot.message_handler(func=lambda message: message.text == 'Лента заданий')
def task_feed(message):
    tasks = ['Задание 1', 'Задание 2', 'Задание 3']  # Пример списка заданий, можно загрузить из базы данных

    # Отправка списка заданий пользователю
    for task in tasks:
        bot.send_message(message.chat.id, task)

        # Обработка реакции пользователя на задание и пополнение баланса

bot.polling()
