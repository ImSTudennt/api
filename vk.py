import requests
from pprint import pprint
import json
import os

class Vk_photo:
    with open(r"C:\Users\vladi\Desktop\token_vk.txt","r") as file:
        token = file.readline().strip()
    
    host = 'https://api.vk.com/method/'
    
    def __init__(self,id):
        self.id = id
    
    def get_album_id(self, name_album):
        url = self.host + "photos.getAlbums"
        params = {
            "v": "5.131",
            "access_token": self.token,
            "owner_id": self.id,
        }
        res = requests.get(url, params=params).json()
        for el in res["response"]["items"]:
            if el["title"] == name_album:
                return el["id"]

    def get_photos(self, count = 5, name_album = None):
        album_id = "profile"
        if self.get_album_id(name_album) is not None:
            album_id = self.get_album_id(name_album)
        get_photo_url = self.host + 'photos.get'
        params = {
            "v": "5.131",
            "access_token": self.token,
            "album_id": album_id,
            "count": count,
            "extended": "1",
            "owner_id": self.id,
            "photo_sizes": "1"
        }
        res = requests.get(get_photo_url, params=params)
        res = res.json()
        return res["response"]["items"]

    def get_dic_max_size_photos(self,lis):
        photos_dic = {}
        for el in lis:
            for photo in el["sizes"]:
                if photo["type"] == "w":
                    if el["likes"]["count"] not in photos_dic:
                        photos_dic[el["likes"]["count"]] = [photo["url"], photo["type"]]
                        break
                    else:
                        photos_dic[el["date"]] = [photo["url"], photo["type"]]
                        break
            else:
                if el["likes"]["count"] not in photos_dic:
                    photos_dic[el["likes"]["count"]] = [el["sizes"][-1]["url"], el["sizes"][-1]["type"]]
                else:
                    photos_dic[el["date"]] = [el["sizes"][-1]["url"], el["sizes"][-1]["type"]]
        return photos_dic

    def get_json_file(self, photos_dic):
        file = [{"file_name": f'{el}.jpg', "type": photos_dic[el][1]} for el in photos_dic]
        current = os.getcwd()
        file_name = "new.json"
        full_path = os.path.join(current, file_name)
        with open(full_path, "w") as f:
            json.dump(file, f, indent = 2)