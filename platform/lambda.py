def lambda_handler(event, context):
    import boto3
    sqs = boto3.resources('sqs')
    queue = sqs.get_queue_by_name(QueueName='my-queue')
    response = queue.send_message(
        MessageBody="boto3",
        MessageAttributes={
            'KeyPair': {
                'Key1': 'Pair1',
                'Key2': 'Pair2'
            }
        }
    )

    return response.get('MessageId')
    return response.get('MD5OfMessageBody')
