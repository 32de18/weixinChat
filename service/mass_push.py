from wechatpy import WeChatClient, WeChatClientException
from wechatpy.client.api import WeChatMedia, WeChatUser

from utils.config_utils import ConfigUtils


class MassPushService(object):

    @classmethod
    def mass_push(cls, client: WeChatClient):
        # 创建图文消息

        articles = [
            {
                'title': '',
                "thumb_media_id": '',
                'author': "李",
                'digest': "快乐",
                'show_cover_pic': 1,
                'content': "",
                "need_open_comment": 1,
                "only_fans_can_comment": 1
            }
        ]
        media = WeChatMedia(client)
        result = media.upload_articles(articles)
        media_id = result["media_id"]
        print("文章上传成功，media_id 为", media_id)
        openid_list = cls.get_all_open_id(client)
        try:
            # 群发消息
            result = client.message.send_mass_article(openid_list, media_id=media_id)
            print(result)
        except WeChatClientException as e:
            print(e)

    @staticmethod
    def get_all_open_id(client: WeChatClient):
        user = WeChatUser(client)

        # 获取公众号所有关注者的openid
        openid_list = user.get_followers()
        print('共获取到', len(openid_list), '个openid')
        print(openid_list)
        return openid_list

    @classmethod
    def single_push(cls, client: WeChatClient):
        # 创建图文消息

        articles = [
            {
                'title': '',
                "thumb_media_id": '',
                'author': "李",
                'digest': "快乐",
                'show_cover_pic': 1,
                'content': "",
                "need_open_comment": 1,
                "only_fans_can_comment": 1
            }
        ]
        openid_list = cls.get_all_open_id(client)
        for open_id in openid_list:
            result=client.message.send_articles(user_id=open_id,articles=articles)
            print(result)

if __name__ == '__main__':
    cfg = ConfigUtils.get_config()

    # 创建wechatpy实例
    client = WeChatClient(appid=cfg.get(ConfigUtils.KEY_APP_ID), secret=cfg.get(ConfigUtils.KEY_APP_SECRET))
    MassPushService.mass_push(client)
    # MassPushService.single_push(client)