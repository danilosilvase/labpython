import boto3
import os

# ECS Details
region = os.environ['REGION']
cluster_name = ['CLUSTER']
services = os.environ["SERVICES"].split(" ")

ecs_client = boto3.client('ecs', region_name=region)

def change_desiredcount():
    """Changes in Service the desired tasks to 0"""
    try:
        for item in services:
            response = ecs_client.update_service(
                cluster=cluster_name,
                service=item,
                desiredCount=0)
            print("Stoping Service {}".format(item))
    except:
        print("Service not found/not Active")


def lambda_handler(event, context):
    change_desiredcount()
    print("Changing desired tasks to 0")