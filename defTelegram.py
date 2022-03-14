#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# - mar/2022 - b0nz
#
# Brief documentation
#     There are two functions in this file, one for sending messages and one for sending images.
#     Images can be sent from numpy import character
#     from local directory or using an url. Although the terminology message
#     is used in both options, it's important to notice that while messages have a max lenght of
#     4096 characters, text sent with a photo as a caption max lenght is 1024 chars. Also, the 
#     imported library requires the argument text, not message, as we are using. 
#
# Message or photo with caption can be sent to a Telegram chat (contact), channel or group.

# Creating a Telegram Bot
# -   Start a conversation with [BotFather](https://t.me/BotFather);
# -   Send it to the BotFather: /newbot
# -   Choose a name for your bot;
# -   Choose a username for your bot;
# -   Done! You'll get a token to access the HTTP API.

# Getting channel or chat (contact) ID
# -   Start a conversation with [JsonDumpBot](https://t.me/JsonDumpBot);
# -   It will reply with a json with information from the message;
# -   Go to the channel or chat you want the id and forward a message from there to JsonDumpBot;
# -   Find the id in the reply. It'll look something like this:
#    {...
#     "forward_from_chat": {
#           "id": xxxxxxxxx,
#    ...}
# -   Don't forget to add the bot as admin in channel so messages can be sent.

# Getting a group ID
# -   Open [Telegram web](https://web.telegram.org);
# -   Go to group and check the url on address bar of browser;
# -   That's the group ID (-xxxxxxxxx), it'll look something like this:
#       https://web.telegram.org/z/#-xxxxxxxxx


import argparse
import telegram

top_parser = argparse.ArgumentParser(description='Telegram functions')
top_parser.add_argument('-m', '--message', action="store", dest="message", required=True, help="Message to be sent.")
top_parser.add_argument('-p', '--photo', action="store", dest="photo", type=str, help="Local file or url to photo to be sent. When used with -m the message will be sent as caption.")
top_parser.add_argument('-c', '--chat-id', action="store", dest="chat_id", type=str, help="Chat ID to deliver the message.")
top_parser.add_argument('-t', '--token', action="store", dest="token", type=str, help="Telegram bot token.")
top_parser.add_argument('-v', '--verbose', action="store_true", dest="verbose", help="Adds verbosity.")
args = top_parser.parse_args()

message = args.message
photo = args.photo
chat_id = args.chat_id
token = args.token
verbose = args.verbose

def sendTelegMes(message, token, chat_id):
    sent = False
    retry_c = 0
    while sent == False:
        try:
            bot = telegram.Bot(token=token, request=telegram.utils.request.Request(connect_timeout=20, read_timeout=20))
            sent = bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN, timeout=20)
        except Exception as err:
            if retry_c > 4:
                print('Telegram attempts exceeded. Message not sent.')
                break
            elif str(err) == 'Unauthorized':
                print('Invalid Telegram bot token, message not sent.')
                break
            elif str(err) == 'Timed out':
                retry_c += 1
                print('Telegram timeout count: '+str(retry_c))
                pass
            elif str(err) == 'Chat not found':
                print('Invalid Telegram Chat ID, message not sent.')
                break
            elif str(err)[:35] == '[Errno 2] No such file or directory':
                print('Telegram module couldn\'t find an image to send.')
                break
            elif str(err) == 'Media_caption_too_long':
                print('Telegram image caption lenght exceeds 1024 characters. Message not send.')
                break
            else:
                print('Unexpected error: '+str(err)+'\nMessage not sent.')
                break
        else:
            if sent["chat"]["type"] == "private" and verbose == True:
                print("Telegram message successfully sent.")
                print("Verbosity on\nMessage delivery information:\n  text: "+str(sent["text"])+"\n  date: "+str(sent["date"])+"\n  message_id: "+str(sent["message_id"])+"\n  username: "+str(sent["chat"]["username"])+"\n  first_name: "+str(sent["chat"]["first_name"])+"\n  id: "+str(sent["chat"]["id"]))
            else:
                print("Telegram message successfully sent.")
    return sent

def sendTelegPho(photo, message, token, chat_id):
    import telegram
    sent = False
    retry_c = 0
    while sent == False:
        try:
            bot = telegram.Bot(token=token, request=telegram.utils.request.Request(connect_timeout=20, read_timeout=20))
            sent = bot.send_photo(chat_id=chat_id, photo=photo, caption=message, parse_mode=telegram.ParseMode.MARKDOWN, timeout=20)
        except Exception as err:
            if retry_c > 4:
                print('Telegram attempts exceeded. Message not sent.')
                break
            elif str(err) == 'Unauthorized':
                print('Invalid Telegram bot token, message not sent.')
                break
            elif str(err) == 'Timed out':
                retry_c += 1
                print('Telegram timeout count: '+str(retry_c))
                pass
            elif str(err) == 'Chat not found':
                print('Invalid Telegram Chat ID, message not sent.')
                break
            elif str(err)[:35] == '[Errno 2] No such file or directory':
                print('Telegram module couldn\'t find an image to send.')
                break
            elif str(err) == 'Media_caption_too_long':
                print('Telegram image caption lenght exceeds 1024 characters. Message not send.')
                break
            else:
                print('Unexpected error: '+str(err)+'\nMessage not sent.')
                break
        else:
            if sent["chat"]["type"] == "private" and verbose == True:
                print("Telegram message successfully sent.")
                print("Verbosity on\nMessage delivery information:\n  text: "+str(sent["text"])+"\n  date: "+str(sent["date"])+"\n  message_id: "+str(sent["message_id"])+"\n  username: "+str(sent["chat"]["username"])+"\n  first_name: "+str(sent["chat"]["first_name"])+"\n  id: "+str(sent["chat"]["id"]))
            else:
                print("Telegram message successfully sent.")
    return sent

if photo != None:
    print("Sending photo...")
    sent = sendTelegPho(photo, message, token, chat_id)
    print("Done.")
else:
    print("Sending message...")
    sent = sendTelegMes(message, token, chat_id)
    print("Done.")
