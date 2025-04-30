import json
import boto3
import os
import urllib3
from datetime import datetime

# Initialize clients and HTTP manager
http = urllib3.PoolManager()
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

# Get environment variables
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')
DDB_TABLE_NAME = os.environ.get('DDB_TABLE_NAME')

def lambda_handler(event, context):
    # Extract S3 upload info from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    timestamp = datetime.utcnow().isoformat()

    # Send Slack notification
    slack_message = {
        'text': f'📁 New file uploaded: `{key}` to bucket `{bucket}`.'
    }
    http.request(
        'POST',
        SLACK_WEBHOOK_URL,
        body=json.dumps(slack_message),
        headers={'Content-Type': 'application/json'}
    )

    # Publish notification to SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=f'A new file `{key}` was uploaded to S3 bucket `{bucket}`.',
        Subject='S3 Upload Notification'
    )

    # Store metadata in DynamoDB
    table = dynamodb.Table(DDB_TABLE_NAME)
    table.put_item(Item={
        'fileName': key,
        'uploadTimestamp': timestamp
    })

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed file upload event.')
    }
