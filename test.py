import telebot
import openpyxl

from telebot import types


bot = telebot.TeleBot("1634806032:AAGTbHGWYYzcbF7PAHWZMK3fmt9RS2Sm8SI")
book = openpyxl.open('data.xlsx', read_only=True)

# def menu_naprav()


@bot.message_handler(commands=['start'])
def com_start(message):
    markup_start = types.ReplyKeyboardMarkup(row_width=1)
    btn_raspis = types.KeyboardButton('Расписание')
    btn_about = types.KeyboardButton('Контакты')
    markup_start.row(btn_raspis, btn_about)
    bot.send_message(
        message.chat.id, "Выберите, что хотите узнать:", reply_markup=markup_start)
    #bot.send_message(message.chat.id,'Добро пожаловать в тестовый бот!\nЧтобы узнать все комманды введите /help')


@bot.message_handler(commands=['help'])
def com_help(message):
    bot.send_message(message.chat.id, 'Запрос расписания: /raspisanie')


@bot.message_handler(regexp='Расписание')
def com_raspisanie(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    btn_aero = types.KeyboardButton('Аэро')
    btn_robo = types.KeyboardButton('Робо')
    markup.row(btn_aero)
    markup.row(btn_robo)
    bot.send_message(message.chat.id, "Выберите направление:",
                     reply_markup=markup)


@bot.message_handler(regexp='Контакты')
def com_about(message):
    bot.send_message(
        message.chat.id, "Телефон: +78422302900\nE-mail: info@kvantorium73.ru\nВремя работы: ПН-ПТ 9:00 - 18:00")


@bot.message_handler(regexp='Аэро')
def com_rasp_aero(message):
    sheet1 = book['Аэро']

    txt_val = ''
    for row in sheet1.iter_rows():
        for cell in row:
            txt_val += str(cell.value)+'\t'
        txt_val += '\n'
    bot.send_message(message.chat.id, txt_val)
    com_start(message)


@bot.message_handler(regexp='Робо')
def com_rasp_robo(message):
    sheet1 = book['Робо']
    txt_val = ''
    for row in sheet1.iter_rows():
        for cell in row:
            txt_val += str(cell.value)+'\t'
        txt_val += '\n'
    bot.send_message(message.chat.id, txt_val)
    com_start(message)


bot.polling()
