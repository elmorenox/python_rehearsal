import boto3
import csv
import os

iam_client = boto3.client('iam')
# create a boto client specific to IAM
response = iam_client.list_policies()

# open a csv file to write to
with open('iam_policies.csv', mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['Policy Name', 'PolicyId', 'Arn'])
    writer.writeheader()

    # iterate through policies in response
    for policy in response['Policies']:
        # Get the policy name, policy ID, and ARN.
        policy_name = policy['PolicyName']
        policy_id = policy['PolicyId']
        arn = policy['Arn']

        # create dictionary of values and write to csv
        writer.writerow({'Policy Name': policy_name, 'PolicyId': policy_id, 'Arn': arn})
