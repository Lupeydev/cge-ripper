import random
import string
import requests

base_url = "https://wavespray.dathost.net/fastdl/teamfortress2/679d9656b8573d37aa848d60"

def random_map_name():
    length = random.randint(4, 20)
    chars = string.ascii_lowercase + string.ascii_uppercase + "_" * 5
    return ''.join(random.choices(chars, k=length))

def random_map_pull():
    while True:
        map_name = random_map_name()
        url = f"{base_url}/maps/{map_name}.bsp"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"✅ Found: {map_name}")
            with open(f"{map_name}.bsp", "wb") as f:
                f.write(response.content)
        else:
            print(f"❌ Not found: {map_name}")

def wordlist_map_pull():
    while True:
        for word in words:
                map_name = word
                url = f"{base_url}/maps/{map_name}.bsp"
                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        print(f"✅ Found: {map_name}")
                        with open(f"{map_name}.bsp", "wb") as f_out:
                            f_out.write(response.content)
                    else:
                        print(f"❌ Not found: {map_name}")
                except requests.RequestException as e:
                    print(f"⚠️ Error fetching {map_name}: {e}")

def directmap(map_name):
    url = f"{base_url}/maps/{map_name}.bsp"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"✅ Found: {map_name}")
        with open(f"{map_name}.bsp", "wb") as f:
            f.write(response.content)
    else:
        print(f"❌ Not found: {map_name}")

print("1. Random Generate text for Maps")
print("2. Use Wordlist for Maps")
print("3. Choose specific word for Maps")
menuselection = input("Select Option: ")

if(menuselection == "1"):
    random_map_pull()
elif(menuselection == "2"):
    wordlistpath = input("Enter your wordlist path: ")
    with open(wordlistpath, "r", encoding="utf-8") as f:
        words = [line.strip() for line in f if line.strip()]
    wordlist_map_pull()
elif(menuselection == "3"):
    mapchoice = input("What map do you choose: ")
    directmap(mapchoice)         
    

        