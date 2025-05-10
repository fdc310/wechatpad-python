from util.http_util import async_request,post_json


class LoginApi:
    def __init__(self, base_url: str, token: str = None, admin_key: str = None):
        '''

        Args:
            base_url: 原始路径
            token: token
            admin_key: 管理员key
        '''
        self.base_url = base_url
        self.token = token
        # self.admin_key = admin_key

    def get_token(self, admin_key, day: int=365):
        # 获取普通token
        url = f"{self.base_url}/admin/GenAuthKey1"
        json_data = {
                "Count": 1,
                "Days": day
            }
        return post_json(base_url=url, token=admin_key, data=json_data)

    async def get_login_qr(self, Proxy: str = ""):
        '''

        Args:
            Proxy:异地使用时代理

        Returns:json数据

        '''
        #获取登录二维码
        url = f"{self.base_url}/login/GetLoginQrCodeNew"
        check = False
        if Proxy != "":
            check = True
        json_data = {
              "Check": check,
              "Proxy": Proxy
            }
        return await async_request(base_url=url, token_key=self.token, json=json_data)


    async def get_login_status(self):
        # 获取登录状态
        url = f'{self.base_url}/login/GetLoginStatus'
        return await async_request(base_url=url, token_key=self.token, method="GET")


    async def logout(self):
        # 退出登录
        url = f'{self.base_url}/login/LogOut'
        return await async_request(base_url=url, token_key=self.token, method="GET")


    async def wake_up_login(self, Proxy: str = ""):
        # 唤醒登录
        url = f'{self.base_url}/login/WakeUpLogin'
        check = False
        if Proxy != "":
            check = True
        json_data = {
            "Check": check,
            "Proxy": ""
        }
        return await async_request(base_url=url,token_key=self.token,json=json_data)





