import json
from botocore.vendored import urllib3

http = urllib3.PoolManager()

def lambda_handler(event, context):
    # 1. Parse out query string params
    url = event['queryStringParameters']['url']
    r = http.request('GET', url)

    # 2. Construct the body of the response object
    transaction_response = {
        'url': url,
        'message': r.status
    }

    # 3. Construct http response object
    response_object = {
        'headers': {
            'Content-Type': 'application/json'
        },
        'statusCode': r.status,
        'body': json.dumps(transaction_response)
    }

    # 4. Return the response object
    return response_object