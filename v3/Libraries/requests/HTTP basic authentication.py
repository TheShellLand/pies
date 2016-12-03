import requests



response = requests.get('http://service.example.com', auth=requests.auth.HTTPBasicAuth('username', 'password'))

print(response.text)
