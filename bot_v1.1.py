from twx.botapi import *
import config
import telebot
import time
import apsw

#bot = TelegramBot('210743449:AAGu5Re1Lfw0AClRh0yNDxpEoIxEYfiGcO8')
#bot.update_bot_info().wait()
#print(bot.username)

userpoint = 0

def listener(messages):
    global userpoint
    for m in messages:
        connection=apsw.Connection("db.db3")
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM db')
        if m.content_type == 'text':

                for row in cursor:


                        if m.text == row[0]:
                            strn = 'You get ' + str(row[1]) + ' points from ' + row[2]
                            bot.send_message(m.chat.id, strn)
                            userpoint += row[1]
                            strn = 'Now you have ' + str(userpoint) + ' points'
                            bot.send_message(m.chat.id, strn)
        cursor.close()


if __name__=='__main__':
    username = 0
    bot = telebot.TeleBot(config.token)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)