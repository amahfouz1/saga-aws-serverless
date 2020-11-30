import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('shipment')
    response = table.put_item(
          Item={
                'order_id': event['order_id'],
                'address': event['address']
            }
        )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return event
    else:
        return response
