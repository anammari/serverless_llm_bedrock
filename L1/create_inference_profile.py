import requests
import json

# Define the endpoint and headers
endpoint = "https://bedrock.us-west-2.amazonaws.com/"
headers = {
    "Content-Type": "application/json"
}

# Define the payload
payload = {
    "inferenceProfileName": "USNovaMicroApplicationIP",
    "modelSource": {
        "copyFrom": "amazon.nova-micro-v1:0"
    },
    "tags": [
        {
            "key": "projectId",
            "value": "abcdef123456"
        }
    ]
}

# Convert the payload to a JSON string
payload_json = json.dumps(payload)

# Make the POST request
response = requests.post(endpoint, headers=headers, data=payload_json)

# Check the response
if response.status_code == 200:
    print("Inference profile created successfully.")
    print("Response:", response.json())
else:
    print("Failed to create inference profile.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
