import telebot
from telebot import types
import globus_parsed

token = '7128087705:AAGgTLRl3Qiw3-eI06i3Lt_ognuW5WeVXeg'
bot = telebot.TeleBot(token=token,parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Добрый день: ')
    
    markup = types.ReplyKeyboardMarkup(row_width=3)
    btn1 = types.KeyboardButton('Globus')
    btn2 = types.KeyboardButton('Народный')
    btn3 = types.KeyboardButton('Фрунзе')
    markup.add(btn1, btn2, btn3)

    bot.send_message(chat_id=message.chat.id, 
                     text='Выберите магазин',
                     reply_markup=markup)
    
bot.message_handler(func=lambda x: True)
def echo_all(message):
    if message.text == 'Globus':
        categories = globus_parsed.get_categories()
        for category in categories:
            text = f'_{category["title"]}_\n' ,
            f'[-------------------------]({category["image"]})' 
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(
                text='Перейти', callback_data='folliw_sub_category'

            )
            keyboard.add(button)
            bot.send_message(chat_id=message.chat.id, 
                             text=text,
                             parse_mode='Markdown',
                             reply_markup=keyboard)


bot.polling()