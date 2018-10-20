#!/usr/bin/env python3.6

import requests, sys, argparse
from requests.exceptions import ConnectionError

# Define description for script
parser = argparse.ArgumentParser(description='HTTP Request Tool')

# Define requirement arguments
required_argument = parser.add_argument_group('required arguments')

# Requirement arguments
required_argument.add_argument(
    '-u','--url',
    help="Url for request. Example: http://google.com",
    type=str, 
	required=True
)

# Optional arguments
parser.add_argument(
    '-m','--method',
    help="Method request. Example: GET or HEAD Default: GET",
    type=str, 
    default="GET",
	required=False
)

parser.add_argument(
    '-t','--timeout',
    help="Define a timeout Example: 10 Default: 20",
    type=float,
    default=20,
	required=False
)

parser.add_argument(
    '-n','--number',
    help="Requests number Example: 10 Default: 1",
    type=int,
    default=1,
	required=False
)

parser.add_argument(
    '-sh','--show-header',
    help="Return header Example: True Default: False",
    type=bool,
    default=False,
	required=False
)

# Get arguments
args = parser.parse_args()
url = args.url

try:
    # Loop for number of requests. Default is 1 request
    for i in range(args.number):
        method = args.method.lower()
        if method == "get":
            req = requests.get(url, timeout=args.timeout)
        elif method == "head":
            req = requests.head(url, timeout=args.timeout)
        else:
            msg = "Unknow type of request. Try GET or HEAD"
            print("sys=http-request-tool log=ERROR error='%s'" % msg)
            sys.exit(1)

        # Get total of request seconds
        requestTime = req.elapsed.total_seconds()
        # Get HTTP response
        httpCode = str(req.status_code)

        # Manipulating response
        if httpCode[0] == "2" or httpCode[0] == "3":
            if args.show_header == True:
                header = req.headers
                print("sys=http-request-tool log=INFO status=%s url=%s requestTime=%s header=%s" % (httpCode,url,requestTime,header))
            else:
                print("sys=http-request-tool log=INFO status=%s url=%s requestTime=%s" % (httpCode,url,requestTime))

        elif httpCode == "404":
            msg = "Path not found"
            print("sys=http-request-tool log=ERROR status=%s url=%s error='%s'" % (httpCode,url,msg))
            sys.exit(1)

        elif httpCode == "405":
            msg = "Method not allowed"
            print("sys=http-request-tool log=ERROR status=%s url=%s error='%s'" % (httpCode,url,msg))
            sys.exit(1)

        elif httpCode[0] == "5":
            msg = "Server error"
            print("sys=http-request-tool log=ERROR status=%s url=%s error='%s'" % (httpCode,url,msg))
            sys.exit(1)

# Manipulating ConnectionErrors
except ConnectionError as e:
    if "ConnectTimeout" in str(e):
        msg = "Connection timeout"
    else:
        msg = "Error to connect, verify url and port"
    print("sys=http-request-tool log=ERROR url=%s error='%s'" % (url, msg))
    sys.exit(1)

# Manipulating generic errors
except Exception as e:
    print("sys=http-request-tool log=ERROR url=%s error=%s" % (url,str(e)))
    sys.exit(1)