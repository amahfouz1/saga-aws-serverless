import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('order')
    response = table.put_item(
          Item={
                'order_id': event['order_id'],
                'order_total': event['total']
            }
        )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return event
    else:
        return response
