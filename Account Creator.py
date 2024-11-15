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
#you will need to load your own names.json file for this portion to work

for name in names:
    name_extra = ''.join(random.choice(string.digits))
    rannames = name.lower() 
    #email can be anything @yahoo @gmail @hotmail.com etc
    useremail = name.lower() + name_extra + '@yahoo.com'
    username = name.lower() + name_extra 
    'password = ''.join(random.choice(chars) for i in range(12))'
    password = 'isthisgoodenough'
    'g = requests.get(url)'
    req = requests.post(url, allow_redirects=False, data={
        'token': 'f6921b3ca5db3731862f0c49857e330f3dc19073b2b1533cbe4692c6a873ef4e',
        'username': rannames,
        'email': useremail,
        'password': password
#this information can be grabbed my inspecting the website in Chrome > going to "Network" > put a random character in the username field and hit enter > Look for signup '(has all information needed for above)'"
#if script doesn't work remove the comments
    })
    print req
    
webbrowser.open(p)


