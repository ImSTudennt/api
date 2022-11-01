import requests
from pprint import pprint

class YaUploader:

    host = "https://cloud-api.yandex.net/"

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'
        }
    
    def post_upload(self,photos_dic):
        headers = self.get_headers()
        flag = True
        for el in photos_dic:
            path = "/photos/" + str(el) + ".jpg"
            url = self.host + "v1/disk/resources/upload"
            params = {"path": path, "url": photos_dic[el][0]}
            res = requests.post(url, params = params, headers = headers)
            if res.status_code == 202:
                flag == True
            else:
                flag == False
                status = res.status_code
                break
        if flag == True:
            print("Фотографии успешно загружены")
        else:
            print(f"Произошла ошибка {status}.")

    def get_upload_link(self, path):
        url = self.host + "v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path, "overwrite": "true"}
        res = requests.get(url, params = params, headers = headers).json()
        return res.get("href")

    def put_upload(self, path, file_name):
        href = self.get_upload_link(path)
        response = requests.put(href, open(file_name,"rb"))
        if response.status_code == 201:
            print("Файл успешно загружен")
        else:
            print(f"Произошла ошибка {response.status_code}.")