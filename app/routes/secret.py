from fastapi import APIRouter, HTTPException
import boto3
from app.config import AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_KEY, CODE_NAME

router = APIRouter()

# connect to the database 
dynamodb = boto3.client(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)


@router.get(
    "/secret",
    summary="Get Secret",
    description=f"Get the secret code from DynamoDB. codeName: {CODE_NAME}"
)
def get_secret():
    """
    Get the secret code from DynamoDB.
    codeName: {CODE_NAME}
    """
    # request to get the item 
    response = dynamodb.get_item(
            TableName='devops-challenge',
            Key={
                'codeName': {'S': CODE_NAME}
            }
        )
    # take out item from the response
    secret = response.get('Item')
    if secret is None:
        # handle error if the secret is not in the response
        raise HTTPException(status_code=404, detail="Secret not found")
    return {"secret_code": secret['secretCode']['S']} # reutrn the needed json if the secret is found
