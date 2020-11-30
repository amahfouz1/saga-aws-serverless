import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('payment')
    response = table.put_item(
          Item={
                'order_id': event['order_id'],
                'total': event['total'],
                'card_no': event['card_no']
            }
        )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return event
    else:
        return response
