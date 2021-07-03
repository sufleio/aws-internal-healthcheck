import json
from botocore.vendored import urllib3

http = urllib3.PoolManager()

def lambda_handler(event, context):
	#1. Parse out query string params
	url = event['queryStringParameters']['url']
	r = http.request('GET', url)

	#2. Construct the body of the response object
	transactionResponse = {}
	transactionResponse['url'] = url
	transactionResponse['message'] = r.status

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = r.status
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	#4. Return the response object
	return r.status
