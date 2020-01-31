import logging
import os
import json
import io
import gzip
import boto3
from .record_matches import record_matches
from .construct_event import construct_event
from .store_event import store_event
from .config import CONFIG


logger = logging.getLogger()
logging.getLogger().setLevel(CONFIG.log_level)


def lambda_handler(event, context):
    if not event["Message"]:
        logger.error("Invalid message format for cloudtrail SQS messages")
        logger.error("Malformed Message: {}".format(event))
        return False

    if event["Message"] == "CloudTrail validation message.":
        logger.debug("Validation message received : {}".format(event))
        return False

    message = json.loads(event["Message"])

    if "s3ObjectKey" not in message:
        logger.error("Invalid message format, expecting an s3ObjectKey in Message")
        logger.error("Malformed Message: {}".format(event))
        return False

    client = boto3.client('s3')
    for log_file in message["s3ObjectKey"]:
        logger.debug("Downloading and parsing {}".format(log_file))
        s3_object = client.get_object(Bucket=message["s3Bucket"], Key=log_file)
        compressed_data = s3_object["Body"].read()
        data_buffer = io.BytesIO(compressed_data)
        gzip_file = gzip.GzipFile(fileobj=data_buffer)
        json_logs = json.loads(gzip_file.read())
        for record in json_logs["Records"]:
            if record_matches(record):
                event = construct_event(record)
                store_event(event)
