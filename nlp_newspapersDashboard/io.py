import boto3
import io


def create_S3_session(AWS_KEY_ID: str, AWS_SECRET: str) -> boto3.resource:
    """Creates a connection to AWS and return the S3 resource for the dashboard

    Args:
        AWS_KEY_ID (str): Credentials to identify with AWS
        AWS_SECRET (str): Credentials to identify with AWS

    Returns:
        boto3.resource: Resource for the session
    """
    boto_session = boto3.Session(
        aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET
    )

    return boto_session.resource("s3")


def read_file_from_s3(s3: boto3.resource, bucket_name: str, file_name: str) -> io.BytesIO:
    """Reads data from a S3 bucket and return an in-memory stream.

    Args:
        s3 (boto3.resource): Resource from client
        bucket_name (str): Name of the bucket to read
        file_name (str): Name of the file

    Returns:
        io.BytesIO: Stream of data from the file
    """
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    data = obj['Body'].read()
    return io.BytesIO(data)
