import requests
from bs4 import BeautifulSoup

url = "https://detik.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Success ! Response = {response.status_code}")
        # print(f"Content : {response.text}")
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.title.string)
    else:
        print(f"Wooops, ada kesalahan requests {response.status_code}")
except Exception as e:
    print(f"Ada error : {e}")
print("Program selesai!")
