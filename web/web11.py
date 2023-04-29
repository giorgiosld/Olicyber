import requests


URLFLAG  = "http://web-11.challs.olicyber.it/flag_piece"
URLLOGIN = "http://web-11.challs.olicyber.it/login"


s = requests.Session()

data = {"username": "admin", "password": "admin"}

r = s.post(url=URLLOGIN, json=data)
csrf1 = r.text[31:47]
header1 = {'csrf': csrf1}
payload = {'csrf': csrf1,"index":"0"}
r = s.get(url=URLFLAG, params=payload)
flag = ""+r.text[19:29]

r = s.post(url=URLLOGIN, headers=header1, json=data)
csrf2 = r.text[31:47]
header2 = {'csrf': csrf2}
payload = {'csrf': csrf2,"index":"1"}
r = s.get(url=URLFLAG, params=payload)
flag = flag+r.text[19:29]

r = s.post(url=URLLOGIN, headers=header2, json=data)
csrf3 = r.text[31:47]
header3 = {'csrf': csrf3}
payload = {'csrf': csrf3,"index":"2"}
r = s.get(url=URLFLAG, params=payload)
flag = flag+r.text[19:29]

r = s.post(url=URLLOGIN, headers=header3, json=data)
csrf4 = r.text[31:47]
header4 = {'csrf': csrf4}
payload = {'csrf': csrf4,"index":"3"}
r = s.get(url=URLFLAG, params=payload)
flag = flag+r.text[19:29]

print(flag)