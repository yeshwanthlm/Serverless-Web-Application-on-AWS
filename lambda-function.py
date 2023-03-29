import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.table('serverless-web-application-on-aws')
def lambds_handler(event, context):
    response = table.get_item(Key={
        'id':'0'
    })
    users = response['Item']['users']
    users = users + 1
    print(users)
    response = table.put_item(Item={
        'id':'1',
        'users':users
    })

    return users
