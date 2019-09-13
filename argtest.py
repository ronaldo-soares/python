
import argparse
import os.path
import sys


parser = argparse.ArgumentParser(
    usage="usage aqui",
    description="description aqui"
)
parser.add_argument(
    "-m",
    "--method",
    metavar="GET",
    choices=['GET', 'POST', 'PUT', 'DELETE'],
    dest="nam_method",
    help="-m --method GET, POST, PUT, HEADER, DELETE",
    required=True
)
parser.add_argument(
    "-f",
    "--file",
    type=str,
    dest="nam_file",
    help="-f --file fileName format csv",
    required=True
)
parser.add_argument(
    "-w",
    "--worker",
    type=int,
    dest="nam_worker",
    help="-w --worker Number of workers to requestes",
    default=1
)

args = parser.parse_args()

if not os.path.isfile(args.nam_file):
    print 'Err: file %s not found' % args.nam_file
    sys.exit(1)

f = open(args.nam_file)
f1 = f.readlines()
for x in f1:
    print 'bucetada'
    print x #x.replace('\n','')
    print 'ota buceta'
#urls = []
#with open(args.nam_file, 'r') as file:
#    #print file.read()
#    urls.append(file.read())

#print urls


'''
try:
    response = requests.post('http://localhost:808/index_example2.html', headers=headers, data=data)
except requests.exceptions.Timeout:
    print "Maybe set up for a retry, or continue in a retry loop"
except requests.exceptions.TooManyRedirects:
    print "Tell the user their URL was bad and try a different one"
except requests.exceptions.RequestException as e:
    print "catastrophic error. bail."
    print e
'''


