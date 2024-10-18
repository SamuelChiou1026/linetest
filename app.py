from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        access_token = 'sCpM9qnUDRdtLUz5MxymEkZTZzShz75oUbiKEmtPT1WKPtmIfOdKYNvlfV7jhvrOjDT0FXai5pvh6gYjznPaAlYrDHmUDxEKvgts4Lz/5jf4g76nQKavvRRihMSfGKgUjf4M5GRpmWrj8NyLiwAa6QdB04t89/1O/w1cDnyilFU='
        secret = '70da3810e2af36dbb2322c491e45daee'
        line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
        handler = WebhookHandler(secret)                     # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print(msg)                                       # 印出內容
            # 使用main.py中的handle_message函數處理消息
            if msg == "牧心好可愛":
                reply = TextSendMessage("對啊我是寶寶喔")
            else:
                # 這裡應該導入並使用handle_message函數
                # 目前handle_message函數未定義，需要在適當的地方定義或導入
                # 暫時使用一個佔位回覆
                reply = TextSendMessage("抱歉，我還在學習中，無法處理這個訊息。")
        else:
            reply = TextSendMessage('再傳三小?請輸入文字喇!!')
        print(reply)
        line_bot_api.reply_message(tk, reply)               # 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()

