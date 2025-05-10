from util.http_util import post_json,async_request

class UserApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    async def get_profile(self):
        """获取个人资料"""
        url = f'{self.base_url}/user/GetProfile'

        return await async_request(base_url=url, token_key=self.token, method="GET")

    async def get_qr_code(self, recover:bool=True, style:int=8):
        """获取自己的二维码"""
        param = {
              "Recover": recover,
              "Style": style
            }
        url = f'{self.base_url}/user/GetMyQRCode'
        return await async_request(base_url=url, token_key=self.token, json=param)

    async def get_safety_info(self):
        """获取设备记录"""
        url = f'{self.base_url}/equipment/GetSafetyInfo'
        return await async_request(base_url=url, token_key=self.token)



    async def update_head_img(self,  head_img_base64):
        """修改头像"""
        param = {
              "Base64": head_img_base64
            }
        url = f'{self.base_url}/user/UploadHeadImge'
        return await async_request(base_url=url, token_key=self.token, json=param)