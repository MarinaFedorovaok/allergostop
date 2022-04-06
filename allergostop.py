import telebot
import bot_id
import allergens
bot = telebot.TeleBot(bot_id.api)
print(bot_id.api)
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Давайте проверим, аллергенный ли это продукт. Введите название продукта:")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # bot.reply_to(message, "Проверяем "+ message.text)
    find_text = str.lower(message.text)
    if find_text in allergens.allergens:
        bot.send_message(message.chat.id, "К сожалению, " + message.text + " есть в базе аллергенов. Будьте внимательны при употреблении!")
    else:
        bot.send_message(message.chat.id, message.text + " не найден в нашей базе аллергенов. Но есть еще индивидуальная непереносимость! ")


bot.polling(none_stop=True, interval=0)
print(list)