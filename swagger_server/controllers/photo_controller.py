import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util
import boto3


def upload_file(file, userId=0, additionalMetadata=None):
    lis = []
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        lis.append(bucket.name)
    
    client = boto3.client('rekognition', region_name='us-west-2')
    response = client.detect_faces(
        Image={
            'Bytes': file.read()
        },
        Attributes=[
            'ALL',
        ]
    )
    return response
