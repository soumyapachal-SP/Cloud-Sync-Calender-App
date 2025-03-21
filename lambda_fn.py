import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = 'calendar-app-events'

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        event_id = str(datetime.now().timestamp())
        data['event_id'] = event_id
        
        s3.put_object(
            Bucket=bucket_name,
            Key=f"events/{event_id}.json",
            Body=json.dumps(data)
        )
        return {"statusCode": 200, "body": "Event created successfully!"}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
