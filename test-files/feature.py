import boto3

client = boto3.client('s3', aws_access_key_id = 'AKIA4SSDS7JTA7RIKTNV', aws_secret_access_key = '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')

bucket_list_response = client.list_buckets()
# print(bucket_list_response['Buckets'])
for i in bucket_list_response['Buckets']:
	print(i['Name'], i['CreationDate'])
