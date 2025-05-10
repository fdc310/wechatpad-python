from util.http_util import async_request, post_json

class DownloadApi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    async def send_download(self, aeskey, file_type, file_url):
        json_data = {
                  "AesKey": aeskey,
                  "FileType": file_type,
                  "FileURL": file_url
                }
        url = self.base_url + "/message/SendCdnDownload"
        return await async_request(url, json=json_data)