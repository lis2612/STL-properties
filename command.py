from telebot import types

def com_start(message):
    markup_start = types.ReplyKeyboardMarkup(row_width=1)
    btn_raspis = types.KeyboardButton('Расписание')
    btn_about = types.KeyboardButton('Контакты')
    markup_start.row(btn_raspis, btn_about)
    bot.send_message(
        message.chat.id, "Выберите, что хотите узнать:", reply_markup=markup_start)

def math_my(x,z):
    res=x+z
    return res