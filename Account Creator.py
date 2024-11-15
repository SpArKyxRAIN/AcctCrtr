import webbrowser
import os
import random
import json
import requests
import string



chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://defendtheweb.net/auth/signup'

names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))
    rannames = name.lower() 
    
    useremail = name.lower() + name_extra + '@yahoo.com'
    username = name.lower() + name_extra 
    'password = ''.join(random.choice(chars) for i in range(12))'
    password = 'isthishackgoodenough'
    'g = requests.get(url)'
    req = requests.post(url, allow_redirects=False, data={
        'token': '017e9e279cede8ef16e562432d0ebbcb5746f3d4aea0f238b26a7044fb32e25b',
        'username': rannames,
        'email': useremail,
        'password': password
    })
    print req
    
webbrowser.open(p)


