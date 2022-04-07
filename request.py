from flask import jsonify
import requests,json

print("hello")

rep = requests.post(
    url="http://upload-icture-test-api.de.r.appspot.com", 
    timeout=60,
)

'''
rep = requests.post(
    url="https://upload-icture-test-api.de.r.appspot.com/api/upload_picture/login", 
    timeout=120,
    json=json.dumps({"email": "user1", "password": "user1"}) 
)'''

print(rep.url)
print(rep.status_code)
print(rep.reason)
print(rep.text)

print("hey")

