import requests
from bs4 import BeautifulSoup as bs

bot_token = input("bot token: ")
bot_chatID = input("chatID: ")

def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

test = telegram_bot_sendtext("Testing Telegram bot")
print(test)

def tablaPrecio(price, title):
    condicion = False
    if(price < 350 and ("3050" in title)):
        condicion = True
    elif(price < 400 and (("1660" in title) or ("6600" in title) or ("5500" in title) or ("580" in title) or ("590" in title) or ("570" in title) or ("1080" in title) or ("2060" in title))):
        condicion = True
    elif(price < 500 and (("2070" in title) or ("3060" in title) or ("5600 XT" in title)) or ("2060 super" in title)):
        condicion = True
    elif(price < 600 and (("3060 Ti" in title) or ("2080" in title) or ("5700" in title))):
        condicion = True
    elif(price < 700 and (("6700" in title) or ("3070" in title))):
        condicion = True
    elif(price < 800 and ("3070" in title) and ((not "LHR" in title) or (not "V2" in title) or (not "2.0" in title))):
        condicion = True
    elif(price < 900 and ("6800" in title)):
        condicion = True
    elif(price < 1000 and (("6800 XT" in title) or ("6900" in title) or ("3080" in title) or ("3090" in title))):
        condicion = True
    return condicion

