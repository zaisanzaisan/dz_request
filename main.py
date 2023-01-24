# =======================1задание===========================

import requests

superhero_list = ["Hulk", "Captain America", "Thanos"]
url = 'https://akabab.github.io/superhero-api/api/all.json'

def get_smart_superhero():
    all = requests.get(url).json()
    smart = 0
    name = None
    for hero in all:
        for name in superhero_list:     
            if name in hero.values():
                intelligence = hero['powerstats']['intelligence']
                if intelligence > smart:
                    smart = intelligence
                    name = hero['name']
    return f"Самый умный супергерой из списка - {name}\nего интеллект {intelligence}"

print(get_smart_superhero())


# =======================2задание===========================

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Файл успешно загружен!")


if __name__ == '__main__':
    ya = YandexDisk(token=input("Введите Ваш токен: "))
    ya.upload_file_to_disk(disk_file_path=input("Введите имя файла: "), filename = input("Введите путь к файлу: "))