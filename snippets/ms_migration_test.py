import requests

url = "https:// /token"
host_url = "https://203.193.223.5/token"

payload = "username=humaniti%40beyondanalysis.net&password=humaniti1!&grant_type=password"
headers = {
    'Referer': "https://beyondanalysis.moneysoft.com.au",
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers, timeout=60)

print(response.ok)

print(response.text)