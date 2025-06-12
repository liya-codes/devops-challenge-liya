from fastapi import APIRouter, HTTPException
import boto3
from app.config import AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_KEY, CODE_NAME

router = APIRouter()


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

    response = dynamodb.get_item(
            TableName='devops-challenge',
            Key={
                'codeName': {'S': CODE_NAME}
            }
        )
    print(response)
    secret = response.get('Item')
    if secret is None:
        # FastAPI will convert this to a JSON response with HTTP 404
        raise HTTPException(status_code=404, detail="Secret not found")
    return {"secret_code": secret['secretCode']['S']}
