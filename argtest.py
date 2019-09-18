
import argparse
import os.path
import sys
import logging
import requests

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)
#logger = logging.getLogger("my-app")

parser = argparse.ArgumentParser(
    usage="usage aqui",
    description="description aqui",
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
'''
parser.add_argument(
    "-h",
    "--headers",
    type=str,
    dest="nam_headers",
    help="-h --headers Number of workers to requestes",
)
'''

args = parser.parse_args()


def call_request_post(url_data, headers_data, data_data):
    """

    :param url_data:
    :param headers_data:
    :param data_data:
    :return: http status code
    """
    try:
        response = requests.post(url_data, headers=headers_data, data=data_data)
    except requests.exceptions.Timeout:
        logging.ERROR("Maybe set up for a retry, or continue in a retry loop")
    except requests.exceptions.TooManyRedirects:
        logging.ERROR("Tell the user their URL was bad and try a different one")
    except requests.exceptions.RequestException as e:
        logging.ERROR("catastrophic error. bail.")
        logging.ERROR(e)

    return response.status_code


if not os.path.isfile(args.nam_file):
    logging.ERROR('Err: file %s not found' % args.nam_file)
    sys.exit(1)


with open(args.nam_file, "r") as fd:

    #lines = fd.read().splitlines()
    for line in fd:
        line = line.strip()
        #logging.info('bucetada - %s - bucetada' % line)
        headers = {'Content-type': 'application/json'}
        response = call_request_post(line, headers, "data")
        #response = line + "Content-type: application/json" + '{"key":"value"}'
        logging.info("Sending call to %s with response: %s" % (line,response))




