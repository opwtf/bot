import time
from urllib.request import urlopen

import telebot

import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6196489236:AAHFCDVFxeXvgxPF-34JJIHe5qO6Xg5yIII')
id_channel = "@chanel_test_links"


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'hi!')

    photo1 = urlopen('https://sun1-29.userapi.com/impg/OVBMoARFiyE3L4xJ7q6K7oYHHMyJFdsLsa0XDQ/UF7Mc5xciac.jpg?size=1280x1000&quality=96&sign=36d1d32aef25f92d6944a85e462cf90a&c_uniq_tag=GtIotbpivTxY1pQlfpYHmeMA1JygLoXEK5eFVOdrzbA&type=album')
    bot.send_photo(message.chat.id, 'https://sun1-29.userapi.com/impg/OVBMoARFiyE3L4xJ7q6K7oYHHMyJFdsLsa0XDQ/UF7Mc5xciac.jpg?size=1280x1000&quality=96&sign=36d1d32aef25f92d6944a85e462cf90a&c_uniq_tag=GtIotbpivTxY1pQlfpYHmeMA1JygLoXEK5eFVOdrzbA&type=album')



@bot.message_handler(content_types=['text'])
def commands(message):
    if message.text == "start":
        back_post_id = None
        while True:
            post_text = parser(back_post_id)
            back_post_id = post_text[1]

            if post_text[0] != None:
                if post_text[2]!=None:
                #bot.send_message(id_channel, post_text[0])
                    bot.send_photo(id_channel,post_text[2],post_text[0])

                else:
                    bot.send_message(id_channel, post_text[0])
                time.sleep(960)

    else:
        bot.send_message(message.from_user.id, "invalid")


def parser(back_post_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    URL = "https://vk.com/datascience"
    page = requests.get(URL, timeout=100, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    post = soup.find("div", class_="wall_posts own mark_top", id=True)
    post_id = post["id"]
    if post_id != back_post_id:
        title = post.find("div", class_="wall_post_text").text.strip()
        description = post.find("img", class_="MediaGrid__imageOld")['src']
        return f"{title}", post_id, description
    else:
        return None, post_id


bot.polling(none_stop=True)
