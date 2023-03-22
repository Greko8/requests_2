import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path': disk_file_path, 'overwrite': 'true'}
        headers = self.get_headers()
        responce = requests.get(upload_url,headers=headers, params=params)
        return responce.json()

    def upload(self, disk_file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(disk_file_path).get("href", "")
        responce = requests.put(href, data=open(disk_file_path, 'rb'))
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'testfile.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)