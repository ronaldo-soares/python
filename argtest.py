#!/usr/bin/env python

import argparse
import os.path
import sys
import logging
import requests
import json

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

parser.add_argument(
    "-s",
    "--set-header",
    type=str,
    dest="nam_headers",
    help="-s --set-header Headers in format json ex: ",
    default='{}',
)


args = parser.parse_args()


def is_json(json_data):
    try:
        json_object = json.loads(json_data)
    except ValueError as e:
        return False
    return True


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
    print 'Err: file %s not found' % args.nam_file
    sys.exit(1)

if not is_json(args.nam_headers):
    print 'Err: value %s is not valid' % args.nam_headers
    sys.exit(1)


with open(args.nam_file, "r") as fd:

    for line in fd:
        line = line.strip()
        response = call_request_post(line, json.loads(args.nam_headers), "data")
        logging.info("Sending call to %s with response: %s" % (line,response))


