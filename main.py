import requests


def telegram_bot_sendtext(bot_message):
    bot_token = '5109891577:AAFbJbPZEapZUVvQ9qYKny4gapH4ULo3ig0'
    bot_chatID = '1723075046'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()

test = telegram_bot_sendtext("Testing Telegram bot")
print(test)
