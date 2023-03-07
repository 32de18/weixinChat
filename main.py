import logging

from wechatpy import parse_message, create_reply, WeChatClient
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from flask import Flask, request, abort

from service.daily_push import DailyPushService
from utils.config_utils import ConfigUtils

app = Flask(__name__)

import os



cfg = ConfigUtils.get_config()
# 创建wechatpy实例
client = WeChatClient(appid=cfg.get(ConfigUtils.KEY_APP_ID), secret=cfg.get(ConfigUtils.KEY_APP_SECRET))


@app.route('/wechat', methods=['GET', 'POST'])
def wechat():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echo_str = request.args.get('echostr', '')
    token = '12345678111111'

    try:
        check_signature(token, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(400)

    if request.method == 'GET':
        return echo_str

    msg = parse_message(request.data)
    logging.info(msg)
    reply = create_reply('Hello, ' + msg.content, msg)
    return reply.render()


@app.get('/daily')
def daily_push():
    DailyPushService.love_push(client)


@app.get('/mass')
def mass_push():
    pass


if __name__ == '__main__':

    app.run(port=5000)
