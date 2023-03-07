from wechatpy import WeChatClient
from wechatpy.exceptions import WeChatClientException

from utils.config_utils import ConfigUtils


class UploadUtils(object):

    @classmethod
    def upload_img(cls, client):

        # 上传图片素材
        try:
            with open("../data/img1.jpg", "rb") as f:
                result = client.material.add("image", f)
                media_id = result["media_id"]
                print("图片上传成功，media_id 为", media_id)
                return media_id
        except WeChatClientException as e:
            print(e)


if __name__ == '__main__':
    cfg = ConfigUtils.get_config()

    # 创建wechatpy实例
    client = WeChatClient(appid=cfg.get(ConfigUtils.KEY_APP_ID), secret=cfg.get(ConfigUtils.KEY_APP_SECRET))
    s = UploadUtils.upload_img(client)
    print(s)
