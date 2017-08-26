from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

line_bot_api = LineBotApi('2b5af5a097a21b772555b3865ce95847')

try:
    line_bot_api.reply_message('hai', TextSendMessage(text='Hello World!'))
except LineBotApiError as e:
    # error handle
    ...
