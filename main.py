from vk import Vk_photo
from yandex import YaUploader


if __name__ == '__main__':
    id_cl = input("Пожалуйста введите id пользователя для сохранения его фотографий: ")
    oauth_token = input("Введите токен с Полигона Яндекс.Диска: ")
    vk_client = Vk_photo(id_cl)
    ya_client = YaUploader(oauth_token)
    name_album = input("Если хотите сохранить фотографии конкретного альбома напишите название альбома, если нет введите цифру 1: ")
    id_al = vk_client.get_album_id(name_album)
    if name_album == "1":
        photos_dic = vk_client.get_dic_max_size_photos(vk_client.get_photos())
        vk_client.get_json_file(photos_dic)
        ya_client.put_upload(f"/photos/{id_cl}.json", "new.json")
        ya_client.post_upload(photos_dic)
    elif id_al == None:
        print("Название альбома введено не корректно") 
    else:
        photos_dic = vk_client.get_dic_max_size_photos(vk_client.get_photos(name_album=name_album))
        vk_client.get_json_file(photos_dic)
        ya_client.put_upload(f"/photos/{id_cl}.json", "new.json")
        ya_client.post_upload(photos_dic)

