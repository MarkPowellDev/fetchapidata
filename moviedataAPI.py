import requests
import json
import pprint
"""
Simple script to capture API data in a json file using python.
Useful for manipulating data for builds and deployments. 
Fetches API DATA, creates & saves the data in a json file in the directory. 
Example for demo purposes: https://www.tvmaze.com/api
Read & Write JSON in PY: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python
"""

url = "https://api.tvmaze.com/singlesearch/shows"
params = {"q": "Star Trek"} # Change to any movie in database
response = requests.get(url, params)

if response.status_code <= 204: # 200 to 204 is OK
    data = json.loads(response.text)
    pprint.pprint(data) # <-----  Human Readable
    with open('data.json', 'w') as outfile: # <--
        json.dump(data, outfile) #Creates a json file 
else:
    print(f"Error: {response.status_code}")