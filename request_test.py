import requests
import sys
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

data = {
  'msg1': 'wow',
  'msg2': 'such'
}

try:
    response = requests.post('http://localhost:808/index_example2.html', headers=headers, data=data)
except requests.exceptions.Timeout:
    print "Maybe set up for a retry, or continue in a retry loop"
except requests.exceptions.TooManyRedirects:
    print "Tell the user their URL was bad and try a different one"
except requests.exceptions.RequestException as e:
    print "catastrophic error. bail."
    print e
    sys.exit(1)


print response.content
print response.status_code