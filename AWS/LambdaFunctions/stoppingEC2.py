import boto3
region = 'us-east-1'
instances = ['i-02fdea0754c02738e']

ec2 = boto3.client('ec2' , region_name = region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stoped your instances: '+ str(instances))
