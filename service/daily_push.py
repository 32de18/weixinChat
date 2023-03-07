from wechatpy.exceptions import WeChatClientException



class DailyPushService(object):


    @classmethod
    def love_push(cls, client):
        # 发送图片消息
        try:
            media_id = 'your media id'  # 图片素材的media_id
            client.message.send(
                {
                    'touser': 'openid',
                    'msgtype': 'image',
                    'image': {
                        'media_id': media_id
                    }
                }
            )
            print('图片消息发送成功')
        except WeChatClientException as e:
            print('图片消息发送失败：', e)

        # 发送文本消息
        try:
            client.message.send(
                {
                    'touser': 'openid',
                    'msgtype': 'text',
                    'text': {
                        'content': '您好，这是一条文本消息'
                    }
                }
            )
            print('文本消息发送成功')
        except WeChatClientException as e:
            print('文本消息发送失败：', e)
