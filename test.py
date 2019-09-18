import requests

#req = requests.get('http://google.com')
#print req.status_code

r = requests.get('https://github.com/timeline.json')
print r.text
