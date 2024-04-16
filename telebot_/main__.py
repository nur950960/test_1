import telebot, wikipedia
from telebot import types

token = '7046347542:AAHVWaHpje6zI5GuqNHYJadxrgwUDpfk44o'
bot = telebot.TeleBot(token) 

wikipedia.set_lang('ru')

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('кнопка-1')
button2 = types.KeyboardButton('кнопка-2')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start(message):
    message2 = bot.send_message(message.chat.id, 'Привет! Я поисковик. Напиши любое слово.', reply_markup=keyboard)
    bot.register_next_step_handler(message2, hendle_text)

def getwiki(word): 
    try: 
        wikitext = wikipedia.page(word).content[:500]
        wikitext = wikitext.split('. ') 
        wikitext = '. '.join(wikitext[:-1]) + '.'
    except: 
        wikitext = 'Ваш запрос не найден:(' 
    return wikitext

def hendle_text(message): #Япония 
    word = message.text 
    info = getwiki(word) 
    bot.send_message(message.chat.id, info, reply_markup=types.ReplyKeyboardRemove()) 



bot.polling(non_stop=True)