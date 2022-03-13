# Telegram-python-bot
Some codes with functions using python-telegram-bot library. Just to not have to write again.

Based on [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library.

Creating a Telegram Bot
-   Start a conversation with [BotFather](https://t.me/BotFather);
-   Send it to the BotFather: /newbot
-   Choose a name for your bot;
-   Choose a username for your bot;
-   Done! You'll get a token to access the HTTP API.

Getting channel or chat (contact) ID
-   Start a conversation with [JsonDumpBot](https://t.me/JsonDumpBot);
-   It will reply with a json with information from the message;
-   Go to the channel or chat you want the id and forward a message from there to JsonDumpBot;
-   Find the id in the reply. It'll look something like this:
```html
   {...
    "forward_from_chat": {
          "id": xxxxxxxxx,
   ...}
```
-   Don't forget to add the bot as admin in channel so messages can be sent.

Getting a group ID
-   Open [Telegram web](https://web.telegram.org);
-   Go to group and check the url on address bar of browser;
-   That's the group ID (-xxxxxxxxx), it'll look something like this:
```html
  https://web.telegram.org/z/#-xxxxxxxxx
```
