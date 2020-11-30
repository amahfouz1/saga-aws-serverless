import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('payment')
    if 'order_id' in event:
        response = table.delete_item(
              Key={
                    'order_id': event['order_id']
                }
            )
    else:
        response = {'error': 'order_id is not provided'}
