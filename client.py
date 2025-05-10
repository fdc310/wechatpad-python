
from api.login import LoginApi
from api.friend import FriendApi
from api.message import MessageApi
from api.user import UserApi
from api.downloadpai import DownloadApi





class XYPadClient:
    def __init__(self,base_url, token):
        self._login_api = LoginApi(base_url, token)
        self._friend_api = FriendApi(base_url, token)
        self._message_api = MessageApi(base_url, token)
        self._user_api = UserApi(base_url, token)
        self._download_api = DownloadApi(base_url, token)

    def get_token(self,admin_key, day: int):
        '''获取token'''
        return self._login_api.get_token(admin_key, day)

    async def get_login_qr(self, Proxy:str=""):
        """登录二维码"""
        return await self._login_api.get_login_qr(Proxy=Proxy)

    async def awaken_login(self, Proxy:str=""):
        '''唤醒登录'''
        return await self._login_api.wake_up_login(Proxy=Proxy)

    async def log_out(self):
        """退出登录"""
        return await self._login_api.logout()

    async def get_login_status(self):
        """获取登录状态"""
        return await self._login_api.get_login_status()

    async def send_text_message(self, to_wxid, message, ats: list=[]):
        """发送文本消息"""
        return await self._message_api.post_text(to_wxid, message, ats)

    async def send_image_message(self, to_wxid, img_url, ats: list=[]):
        """发送图片消息"""
        return await self._message_api.post_image(to_wxid, img_url, ats)

    async def send_video_message(self, to_wxid, video_url, ats: list=[]):
        """发送音频消息"""
        return await self._message_api.post_voice(to_wxid, video_url, ats)

    async def send_app_message(self, to_wxid, app_message, type):
        """发送app消息"""
        return await self._message_api.post_app_msg(to_wxid, app_message, type)

    async def send_emoji_message(self, to_wxid, emoji_md5, emoji_size):
        """发送emiji消息"""
        return await self._message_api.post_emoji(to_wxid,emoji_md5,emoji_size)

    async def revoke_msg(self, to_wxid, msg_id, new_msg_id, create_time):
        """撤回消息"""
        return await self._message_api.revoke_msg(to_wxid, msg_id, new_msg_id, create_time)

    async def get_profile(self):
        """获取用户信息"""
        return await self._user_api.get_profile()

    async def get_qr_code(self, recover:bool=True, style:int=8):
        """获取用户二维码"""
        return await self._user_api.get_qr_code(recover=recover, style=style)

    async def get_safety_info(self):
        """获取设备信息"""
        return await self._user_api.get_safety_info()

    async def update_head_img(self,  head_img_base64):
        """上传用户头像"""
        return await self._user_api.update_head_img(head_img_base64)

    async def cdn_download(self, aeskey, file_type, file_url):
        """cdn下载"""
        return self._download_api.send_download( aeskey, file_type, file_url)


