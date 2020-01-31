WHITELISTED_EVENTS = [
    ('ec2.amazonaws.com', 'RunInstances')
]

def record_matches(record):
    # Is this record a create or delete that we want to store?
    # Is it of a resource type that we support?

    # https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html

    event_source = record['eventSource']  # ec2.amazonaws.com
    event_name = record['eventName']  # RunInstances

    if [x for x in WHITELISTED_EVENTS if event_source == x[0] and event_name == x[1]]:
        return True
    else:
        return False
