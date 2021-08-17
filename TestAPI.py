
import requests
import json


def getAPIKey():
    with open(".TRN-API-Key", "r") as f:
        return f.read().strip()

def getHeaders():
    # headers = { "TRN-API-Key": getAPIKey() }
    return { "TRN-API-Key": getAPIKey() }

def searchUser(queryString):
    url = "https://public-api.tracker.gg/v2/splitgate/standard/search"
    params = {
            "platform": "steam",
            "query": queryString
            }
    headers=getHeaders()
    response = requests.get(url, params=params, headers=headers)
    searchResults = json.loads(response.text)
    print(json.dumps(searchResults, indent=4))


def getUserStats(playerIdentifier):
    platform = "steam"
    platformUserIdentifier = playerIdentifier
    url = "https://public-api.tracker.gg/v2/splitgate/standard/profile/{}/{}".format(platform, platformUserIdentifier)
    headers = getHeaders()
    response = requests.get(url.format(platform, platformUserIdentifier), headers=headers)
    userStats = json.loads(response.text)
    print(json.dumps(userStats, indent=4))


searchUser("Cpapi")
getUserStats("76561198320465710")
