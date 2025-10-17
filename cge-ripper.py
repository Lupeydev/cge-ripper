import random
import string
import requests

base_url = "https://wavespray.dathost.net/fastdl/teamfortress2/679d9656b8573d37aa848d60/maps/"

def random_map_name():
    length = random.randint(4, 20)
    #Adds more letters to characters list
    chars = string.ascii_lowercase + string.ascii_uppercase + "_" * 5
    return ''.join(random.choices(chars, k=length))

while True:
    map_name = random_map_name()
    url = f"{base_url}{map_name}.bsp"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"✅ Found: {map_name}")
        with open(f"{map_name}.bsp", "wb") as f:
            f.write(response.content)
    else:
        print(f"❌ Not found: {map_name}")
