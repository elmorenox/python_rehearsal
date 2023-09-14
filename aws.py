import json
import subprocess


def aws_info(describe_instance):
    instances = describe_instance["Reservations"][0]["Instances"]
    print(instances)
    instance_ids = [
        instance["InstanceId"] for instance in instances
    ]

    running_instances = [
        instance["InstanceId"] for instance in instances if instance["State"]["Name"] == "running"
    ]

    ips = [
        {"public": instance["PublicIpAddress"], "private": instance["PrivateIpAddress"]}
        for instance
        in instances
        if instance["Tags"][1]["Value"] == "stg"
    ]
    print(f"instance_id_count, {len(instance_ids)}")
    print(f"running, {running_instances}")
    print(f"stg, {ips}")


givenJSON = """
{
    "Reservations": [
        {
            "ReservationId": "r-0b9d09c7fbb123456",
            "Instances": [
                {
                    "InstanceId": "i-0123456789abcdef0",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.150",
                    "PublicIpAddress": "52.14.82.122",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-1"
                        },
                        {
                            "Key": "environment",
                            "Value": "dev"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                },
                {
                    "InstanceId": "i-0123456789abcdef1",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.151",
                    "PublicIpAddress": "54.14.82.123",
                    "State": {
                        "Code": 16,
                        "Name": "disabled"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-2"
                        },
                        {
                            "Key": "environment",
                            "Value": "stg"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                },
                {
                    "InstanceId": "i-0123456789abcdef2",
                    "InstanceType": "t2.micro",
                    "KeyName": "my-key-pair",
                    "ImageId": "ami-0c55b159cbfafe1f0",
                    "PrivateIpAddress": "172.31.16.152",
                    "PublicIpAddress": "52.14.82.124",
                    "State": {
                        "Code": 16,
                        "Name": "running"
                    },
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "web-server-3"
                        },
                        {
                            "Key": "environment",
                            "Value": "dev"
                        }
                    ],
                    "SecurityGroups": [
                        {
                            "GroupName": "my-security-group",
                            "GroupId": "sg-0123456789abcdef0"
                        }
                    ],
                    "SubnetId": "subnet-0123456789abcdef0",
                    "VpcId": "vpc-0123456789abcdef0"
                }
            ]
        }
    ]
}
"""

describe_instance_dict = json.loads(givenJSON)

aws_info(describe_instance_dict)
