import requests
s = requests.Session()

def login_get_token():
    url = "http://api.shopip.caisxs.com/user/login"
    body = {
        "device_type": "Android",
        "device_number": "3517033688244",
        "mobile": "19842314796",
        "code": "qQ123456"
    }
    r = s.post(url, json=body)
    token = r.json()["data"]["token"]
    print(token)
    return token


if __name__ == '__main__':
    login_get_token()
