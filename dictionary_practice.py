import json

#sample dictionary
data = {
    "president": {
        "name": "Barack Obama",
        "number": "44",
    },
}

json_string = json.dumps(data, indent=4)

print(json_string)
print(type(json_string))

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

with open("data_file.json", "r") as read_file:
    data_dict = json.load(read_file)

print(type(data_dict))
print(data_dict)

example = {
  "Teams":[
    {"Giants":[{"wins":4}, {"losses":1}]},
    {"Patriots":[{"wins":2}, {"losses":3}]},
    {"Chiefs":[{"wins":4}, {"losses":1}]}
  ]
}

print(example["Teams"])
print(type(example["Teams"]))

print(example["Teams"][0]["Giants"][0]["wins"])


status = """
{
  "Status": "Healthy",
  "Checks": [
    {
      "Name": "Connections",
      "Status": "Healthy"
    },
    {
      "Name": "ConnectionRead",
      "Status": "unHealthy"
    },
    {
      "Name": "redis",
      "Status": "Healthy"
    },
    {
      "Name": "ProcessCheck",
      "Status": "Healthy"
    },
    {
      "Name": "UserProfile",
      "Status": "unHealthy"
    },
    {
      "Name": "features",
      "Status": "unHealthy",
      "Description": "sample sample sample"
    },
    {
      "Name": "shutdown",
      "Status": "Healthy"
    },
    {
      "Name": "lifespan",
      "Status": "unHealthy"
    }
  ]
}
"""

#make function that count healthy and unhealthy 
# function list unhealthy

status_dict = json.loads(status)

print(status_dict)

def healthy_count(log):
  log_dict = json.loads(log)
  checks = log_dict["Checks"]
  healthy = 0
  for item in checks:
    if item["Status"] == "Healthy":
      healthy+=1
  
  return healthy, len(checks) - healthy


def unhealthy_items(log):
  log_dict = json.loads(log)
  checks = log_dict["Checks"]
  unhealthy = []
  for item in checks:
    if item["Status"] == "unHealthy":
      unhealthy.append(item["Name"])
    
  return unhealthy

healthy, unhealthy = healthy_count(status)
print(healthy, unhealthy)

unhealthy_items = unhealthy_items(status)
print(unhealthy_items)