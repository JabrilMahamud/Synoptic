import boto3
import json

# Function to tag an EC2 instance
def tag_ec2_instance(instance_id, tags):
    # Create a Boto3 EC2 client
    ec2_client = boto3.client('ec2', region_name='eu-west-2')
    
    # Convert the hash table into a list of dictionaries
    tag_list = [{'Key': key, 'Value': value} for key, value in tags.items()]
    
    # Tag the EC2 instance
    response = ec2_client.create_tags(Resources=[instance_id], Tags=tag_list)
    
    # Check if the tagging was successful
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('Instance tagged successfully.')
    else:
        print('Failed to tag instance:', response)


# Read the JSON file
with open(r'C:/Users/maham/OneDrive/Desktop/github repo/github repo/Synoptic/cfn/ct_event.json') as file:
    data = json.load(file)

# Extract the tags from the JSON data
tags = data['event']['detail']['requestParameters']['tagSpecificationSet']['items']

# Create a hash table to store the key-value pairs
hash_table = {}

# Populate the hash table with the key-value pairs
for tag in tags:
    for item in tag['tags']:
        key = item['key']
        value = item['value']
        hash_table[key] = value

# Print the hash table
for key, value in hash_table.items():
    print(f"Key: {key}, Value: {value}")

# Select an EC2 instance ID (replace with your own logic to choose the instance)
instance_id = 'i-0f634885c5daddc11'

# Tag the selected EC2 instance with the key-value pairs
tag_ec2_instance(instance_id, hash_table)
print("success?")