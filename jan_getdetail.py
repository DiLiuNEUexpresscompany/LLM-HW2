import requests
import json

# Assume that the previous code sent the request
url = "http://localhost:1337/v1/models/llama3.1-8b-instruct" #change model here 
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Response Text:", response.text)
    try:
        # Parse json content and print it formatted
        json_response = response.json()
        print(json.dumps(json_response, indent=4))
    except requests.exceptions.JSONDecodeError:
        print("Not Valid JSON")
else:
    print(f"Failed, Code: {response.status_code}, Error Message: {response.text}")
