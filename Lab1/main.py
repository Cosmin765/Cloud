import requests


URL = 'https://www.virustotal.com/en/documentation/public-api/'

res = requests.get(URL, allow_redirects=False)

print(res)

print('Redirecting to:', res.headers['Location'])

res = requests.get(URL, allow_redirects=True)

print(res)

with open('result.html', 'wb') as fd:
	fd.write(res.content)
