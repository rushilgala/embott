from httplib2 import Http
from json import dumps
import random

#
# Hangouts Chat incoming webhook quickstart
#
def main():
    urls = ['']
    
    messages = ["Timecards!", "Timecards, boys and girls", "Sapere aude! Timecards", 
    "Timecards, please", "TWimecards", "Timecards, y'all", "Timecards :D"]

    bot_message = {
        'text' : '<users/all> ' + random.choice(messages)
    }

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    for url in urls:
        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )

    print(response)

if __name__ == '__main__':
    main()
