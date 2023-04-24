import requests

bas_url = "https://ogabek007.pythonanywhere.com/"

class DB:
    def katalog(self):
        url = bas_url + "dafna_app/get_katalog/"
        response = requests.get(url)
        return response.json()