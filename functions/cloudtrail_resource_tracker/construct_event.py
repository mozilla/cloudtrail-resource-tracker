from .resolve_user_identity import resolve_user_identity


def construct_event(record):
    # Based on this record, construct an event that will be written to the DB
    event = {}
    event['event_time'] = record['eventTime']  # 2019-06-19T00:18:31Z
    event['event_source'] = record['eventSource']  # ec2.amazonaws.com
    event['account_id'] = record['recipientAccountId']  # 123456789012
    event['region'] = record['awsRegion']  # us-west-2
    event['user_identity'] = resolve_user_identity(record['userIdentity'])

    # TODO : add the remaining fields
    return event
