
import requests



url = "https://cc1-s3-bucket-1.s3.us-east-2.amazonaws.com/team.json"
response = requests.get(url)

JSON_DATA = response.json()

print(JSON_DATA)