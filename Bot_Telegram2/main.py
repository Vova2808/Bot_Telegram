import telebot
from telebot import types

bot = telebot.TeleBot('6088717747:AAGQtmOEIsNxbBwbsFGP3thxsmE3SxlCwoI')

print("Bot Запущен")
@bot.message_handler(commands=['start'])
def strt(message):
    name = '<b>Здравствуйте это компания Colector23 у Саши Васеленко сгорел дом и он находится в сложном положении можете ли вы ему помочь если вы готовы помочь то напишите /donate_Saha</b>'
    bot.send_message(message.chat.id, name, parse_mode='html')

@bot.message_handler(commands=['donate_Saha'])
def HelpSaha(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Помочь Саше', url='https://donate.qiwi.com/payin/Colector23'))
    bot.send_message(message.chat.id, 'Пожалуйста Помогите Саше', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Этот бот толька для сбора средств Саше что бы помочь саше напишите /donate_Saha')

@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "Привет")
    elif message.text == "Саша Крутой":
        bot.send_message(message.chat.id, 'Саша правада крутой')
    else:
        bot.send_message(message.chat.id, 'Я вас не понимаю напишите /help')


bot.polling(none_stop=True)
