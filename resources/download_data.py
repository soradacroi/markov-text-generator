import requests

url = "https://www.gutenberg.org/files/1661/1661-0.txt"

response = requests.get(url)

if response.status_code == 200:
    with open("D:\markov-text-generator\sherlock.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Download")
else:
    print("Failed")