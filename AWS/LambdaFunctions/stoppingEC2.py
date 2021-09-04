import boto3
import os

#Attributes

region = os.environ['REGION']
instances = os.environ["INSTANCES"].split(" ")


ec2 = boto3.client('ec2' , region_name = region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stoped your instances: '+ str(instances))
