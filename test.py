from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('2b5af5a097a21b772555b3865ce95847')
handler = WebhookHandler('GGyQWDYaUDaV6pFp2f5iwj3NJN5Ih3/th7I7Q3UceXdvIHt9Gp1Meirv+xT+tRiu5L97Glbc4cfX8q8upe8NgygOswBm1NYY5bLm/MSZjxbly5hd/MtigMwxZKvvAn2xixM4jazM76nNBXpd5bNtxQdB04t89/1O/w1cDnyilFU=')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
