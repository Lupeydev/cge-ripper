import requests

base_url = "https://wavespray.dathost.net/fastdl/teamfortress2/679d9656b8573d37aa848d60/maps/"
wordlist_file = "words_alpha.txt"

# Read all words from wordlist (one per line)
with open(wordlist_file, "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

for word in words:
    map_name = word
    url = f"{base_url}{map_name}.bsp"
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
