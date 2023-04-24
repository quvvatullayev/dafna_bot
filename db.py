import requests

bas_url = "https://ogabek007.pythonanywhere.com/"

class DB:
    def katalog(self):
        url = bas_url + "dafna_app/get_katalog/"
        response = requests.get(url)
        return response.json()
    
    def get_prodouct_type(self, id):
        url = bas_url + f"dafna_app/get_prodouct_type/{id}/"
        response = requests.get(url)
        count = len(response.json()['prodouct_typt'])
        return [response.json(), count]