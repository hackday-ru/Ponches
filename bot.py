import config
import telebot
import time
import apsw




def listener(messages):
    for m in messages:
        con = apsw.Connection("db.db3")
        cur = con.cursor()
        cur.execute('SELECT username FROM customers')
        if twx.User.firstName == "text":
            bot.send_message(m.chat.id, "Input your login")
            for row in cur:
                if m.text == row[0]:
                    username = m.text
                    userpoint = row[2]
                    hello = username + ', you have ' + str(userpoint) + ' points.'
                    bot.send_message(m.chat.id, hello)
        connection=apsw.Connection("db.db3")
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM db')
        if m.content_type == 'text':

                for row in cursor:


                        if m.text == row[0]:
                            strn = username + ', you get ' + str(row[1]) + ' points from ' + row[2]
                            bot.send_message(m.chat.id, strn)
                            userpoint += row[1]
                            strn = 'Now you have ' + str(userpoint) + 'points'
                            bot.send_message(m.chat.id, strn)
        cursor.close()

def help_message(arguments, message):
    response = {'chat_id': message['chat']['id']}
    result = ["Hey, %s!" % message["from"].get("first_name"),
              "\rI can accept only these commands:\nlogin\price or ur own key"]
    response['text'] = "\n\t".join(result)
    return response



if __name__=='__main__':
    bot = telebot.TeleBot(config.token)
    bot.set_update_listener(listener)
    bot.polling(none_stop=True)
    while True:
        time.sleep(200)


