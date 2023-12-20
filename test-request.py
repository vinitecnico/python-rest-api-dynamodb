import json
import uuid
import urllib.request

GET_RAW_PATH = "/getPerson"
CREATE_RAW_PATH = "/createPerson"

def lambda_handler(event, context):
    print(event)
    url = "https://www.google.com"

    try:
        response = urllib.request.urlopen(url)
        body = response.read().decode('utf-8')
        status_code = response.getcode()
        return {
            'statusCode': status_code,
            'body': body
        }
    except urllib.error.URLError as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }