import re
import time
from datetime import datetime
from threading import Thread

import telebot

from db_methods import set_user_id, get_user_id, get_values

bot = telebot.TeleBot('5266363672:AAEyg1z8QrEwfS31bJUhGybWZs7zpveD7wY')

# start bot method
def main_bot():
    # listen start command
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        bot.send_message(message.chat.id,
                         'Добрый день ' + message.from_user.first_name + ", вы подписались на уведомления о поставках.\nЕсли какой-нибудь из заказов доставят, вам пришлют уведомление")
        user_id = message.from_user.id
        rows = get_user_id()
        if len(rows):
            for row in rows:
                if user_id != row[0]:
                    set_user_id(int(user_id))
        else:
            set_user_id(int(user_id))
        pass

    # method for mass mailing when an order is received
    def mass_message():
        while True:
            print('mass_message check')
            x = datetime.now().hour
            if x == 8:
                dates = get_values()
                date_today = str(datetime.now().date())
                date_today = re.sub(r'-', ".", date_today)
                for row in dates:
                    if re.search(row[4], date_today):
                        ids = get_user_id()
                        for user_id in ids:
                            bot.send_message(user_id[0],
                                             'Заказ № ' + str(row[1]) + ' на сумму ' + str(
                                                 row[3]) + ' руб ' + ' доставлен')
            time.sleep(3600)
        pass

    # start bot
    def start_bot():
        try:
            print('start bot')
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(15)

    Thread(target=start_bot).start()
    time.sleep(10)
    Thread(target=mass_message).start()
