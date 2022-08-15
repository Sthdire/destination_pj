import time
from threading import Thread
import telebot
from datetime import date

from doc_save import save_db_values
from db_methods import set_user_id
from db_methods import get_user_id
from matplot import graf_img



def autoupdate():
    save_db_values()
    graf_img()
    while True:
        time.sleep(60)
        save_db_values()
        graf_img()
    pass


bot = telebot.TeleBot('5266363672:AAEyg1z8QrEwfS31bJUhGybWZs7zpveD7wY')


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Добрый день ' + message.from_user.first_name + ", вы подписались на уведомления о поставках.\nЕсли какой-нибудь из заказов доставят, вам пришлют уведомление")
    user_id = message.from_user.id
    print(user_id)
    set_user_id(int(user_id))
    pass

def start_bot():
    if __name__ == '__main__':
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(15)

def f():
    rows = get_user_id()
    if date.today() == date.today():
        for row in rows:
            bot.send_message(row[0], str(date.today()))
    pass


Thread(target=autoupdate).start()
Thread(target=start_bot).start()
Thread(target=f).start()
