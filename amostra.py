import boto3
bedrock = boto3.client(service_name = 'bedrock', region_name='us-east-1')
models = bedrock.list_foundation_models()
print(models)