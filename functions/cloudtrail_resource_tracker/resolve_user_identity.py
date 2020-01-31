def resolve_user_identity(user_identity):
    # https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html
    if user_identity['type'] == 'Root':
        return ('Root', None)
    elif user_identity['type'] == 'IAMUser':
        return ('IAMUser', user_identity['userName'])
    elif user_identity['type'] == 'AssumedRole':
        return 'Not yet implemented'
    elif user_identity['type'] == 'FederatedUser':
        return 'Not yet implemented'
    elif user_identity['type'] == 'AWSAccount':
        return 'Not yet implemented'
    elif user_identity['type'] == 'AWSService':
        return 'Not yet implemented'
    else:
        return None

    # TODO : Implement the remaining types