import boto3
import os

region = os.environ['REGION']
instances = os.environ["INSTANCES"].split(" ")

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your inastances: '+ str(instances))
