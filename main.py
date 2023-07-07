import telebot
from telebot import types
API_TOKEN = '5901202049:AAF8T--IvNmjPWY9V0i1lc-TC0GE5o5pTz4'
bot = telebot.TeleBot(API_TOKEN)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])

@bot.message_handler(commands=['start'])
def start(message):
    Keeboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)#создание разметки клавиатуры, resize_keyboard=True размер клавиатуры, row_width количество кнопок которое можно передать
    button_one = types.KeyboardButton(text='/photo ')#создаем кнопку и  параметр текст передаем ее текст
    button_two = types.KeyboardButton(text='Привет')
    Keeboard.add(button_one,button_two)#если кнопок несколько передаем через запятую
    bot.send_message(message.chat.id, "Привет, я Bin_bot, создан для обучению написания ботов на Python)", reply_markup=Keeboard)#  можем передать клавиатуру через reply_markup=

@bot.message_handler(commands=['photo'])
def start(x):
    f = open('/Users/admin/Documents/test_bot_py/photo/cats2.jpeg','rb')
    bot.send_photo(x.chat.id,f)

@bot.message_handler(func = lambda message: (message.text.lower == "hi")) # ПРИВЕТ => привет
@bot.message_handler(func = lambda message: (message.text.lower() == "привет"))
def funcia_one(message):
    Keeboard = types.InlineKeyboardMarkup(row_width=1)
    button_one = types.InlineKeyboardButton(text='xd',url= 'google.com')
    Keeboard.add(button_one)
    bot.send_message(message.chat.id,"Уже виделись)",reply_markup=Keeboard)



#else
@bot.message_handler(func = lambda message: True,chat_types=['private'])
def error(message):
    bot.send_message(message.chat.id, "Вы ввели неверный запрос. Повторите!")




bot.infinity_polling()