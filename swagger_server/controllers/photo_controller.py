import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util
import boto3


def upload_file(userId, additionalMetadata=None, file=None):  # noqa: E501
    # """uploads an image

    #  # noqa: E501

    # :param userId: ID of user to update
    # :type userId: int
    # :param additionalMetadata: Additional data to pass to server
    # :type additionalMetadata: str
    # :param file: file to upload
    # :type file: werkzeug.datastructures.FileStorage

    # :rtype: ApiResponse
    # """
    lis = []
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        lis.append(bucket.name)
    
    client = boto3.client('rekognition', region_name='us-west-2')
    response = client.detect_faces(
        Image={
            # 'Bytes': b'bytes',
            'Bytes': file.read()
        },
        Attributes=[
            'ALL',
        ]
    )
    return response
