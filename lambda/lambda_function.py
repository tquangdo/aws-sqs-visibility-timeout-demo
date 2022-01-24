import boto3

def lambda_handler(event, context):
    try:
        sqsClient=boto3.client("sqs",region_name="us-east-1")
        try:
            response=sqsClient.receive_message(
                QueueUrl="<URL of SQS 3-2)>",
                AttributeNames=['All'],
            )
            print(response)
            return response
        except Exception as e:
            print("msg NG!!!: ",e)
    except Exception as e:
            print("Lambda NG!!!: ",e)