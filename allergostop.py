import telebot
import bot_id
import allergens
bot = telebot.TeleBot(bot_id.api)
print(bot_id.api)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Давайте проверим, аллергенный ли это продукт. Введите название продукта:")
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     print("user wrote: ", message)
#     bot.reply_to(message, "Давайте проверим, аллергенный ли это продукт. Введите название продукта:")
 
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # bot.reply_to(message, "Проверяем "+ message.text)
    if message.text in allergens.allergens:
        bot.send_message(message.chat.id, "К сожалению," + message.text + " есть в базе аллергенов. Будьте внимательны при употреблении!")
    else:
        bot.send_message(message.chat.id, message.text + " не найден в нашей базе аллергенов. Но она не идеальна! Будьте внимательны при употреблении!")


bot.polling(none_stop=True, interval=0)
print(list)