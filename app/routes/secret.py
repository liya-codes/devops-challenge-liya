from fastapi import APIRouter
import boto3
import os
from app.config import AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_KEY ,CODE_NAME

router = APIRouter()

print("AWS_REGION:", AWS_REGION)
print("AWS_ACCESS_KEY:", AWS_ACCESS_KEY)
print("AWS_SECRET_KEY:", AWS_SECRET_KEY)

dynamodb = boto3.client(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)


response = dynamodb.get_item(
            TableName='devops-challenge',
            Key={
                'code_name': {'S': 'thedoctor'}
            }
        )

