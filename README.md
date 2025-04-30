 HEAD
# aws-s3-lambda-integration

# AWS Serverless File Upload Alert System

## Overview

This project demonstrates a serverless architecture on AWS using:
- S3 for file uploads
- Lambda for backend logic
- SNS for email notifications
- Slack Webhook for real-time alerts
- DynamoDB for metadata storage

## Architecture

1. 📁 A file is uploaded to an S3 bucket.
2. ⚙️ An S3 PUT event triggers the Lambda function.
3. 📨 The Lambda function does the following:
   - Sends an alert to Slack via webhook.
   - Publishes a message to an SNS topic (for email notification).
   - Stores metadata (file name, timestamp) in DynamoDB.

## AWS Services Used

- **Amazon S3**: For object storage.
- **AWS Lambda**: Event-driven compute service.
- **Amazon SNS**: For publish-subscribe messaging.
- **Slack Webhook**: Sends messages to a Slack channel.
- **Amazon DynamoDB**: NoSQL database to store file metadata.

## Lambda Environment Variables

Set the following environment variables in the Lambda function configuration:

- `SLACK_WEBHOOK_URL`: Your Slack channel's webhook URL.
- `SNS_TOPIC_ARN`: The ARN of the SNS topic to publish to.
- `DDB_TABLE_NAME`: The name of your DynamoDB table.

## Required IAM Permissions

- AWSLambdaBasicExecutionRole
- AmazonS3ReadOnlyAccess
- AmazonSNSFullAccess
- AmazonDynamoDBFullAccess

## Deployment Steps

1. Create and configure the S3 bucket (block public access, enable versioning, enable encryption).
2. Create the SNS topic and confirm your email subscription.
3. Set up a Slack channel and webhook.
4. Create the DynamoDB table (`s3-upload-metadata`) with `fileName` as partition key.
5. Deploy the Lambda function with environment variables.
6. Configure the S3 bucket to trigger Lambda on PUT events.

## Files Included

- `lambda_function.py`: Lambda handler logic.
- `requirements.txt`: Python package requirements.
- `README.md`: Project documentation.

## License

This project is for educational purposes.
>>>>>>> 652c762 (Finish the assignamentI - Lambda + S3 integration)
