import requests

param = {"q": "Python"}
r = requests.get('https://www.google.com.tw/search', params=param)
print(r.url)

data = {'firstname':'Adam', 'lastname': 'Chang'}
r = requests.post('https://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)

# upload file
file = {'uploadFile': open('./invest.png', 'rb')}
r = requests.post('https://pythonscraping.com/pages/files/processing2.php', files=file)
print(r.text)

# login
payload = {'username': 'adam', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)