# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

def read_texts(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()

api = read_texts('api.txt')
token = read_texts('token.txt')

board_id = 'MgALSadl'

url = "https://api.trello.com/1/boards/MgALSadl/lists"

headers = {
  "Accept": "application/json"
}

query = {
  'key': api,
  'token': token
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


url = "https://api.trello.com/1/cards"

headers = {
  "Accept": "application/json"
}

query = {
    'name': 'Test card 4',
    'desc': 'This is a test card 4.',
    'due': '',
    'start': '',
    'idList': '64d8afd40a17c6df228d4571',
    'key': api,
    'token': token
}

response = requests.request(
   "POST",
   url,
   headers=headers,
   params=query
)

# Check if the response is empty
if not response.text:
    print("Response is empty.")
else:
    # Print the raw response text
    print("Response text:", response.text)

    try:
        # Attempt to parse and print the response as JSON
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    except json.JSONDecodeError:
        print("Failed to decode the response as JSON.")

# Print the response status code
print("Status code:", response.status_code)
