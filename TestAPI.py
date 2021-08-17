
import requests
import json

url = "https://public-api.tracker.gg/v2/splitgate/standard/profile/{}/{}"
platform = "steam"
platformUserIdentifier = "76561198320465710"

headers = {
        "TRN-API-Key": "f47e6a25-e2ba-47f0-b711-2de0d13d9629"
        }

response = requests.get(url.format(platform, platformUserIdentifier), headers=headers)

userProfile = json.loads(response.text)
print(json.dumps(userProfile, indent=4))
