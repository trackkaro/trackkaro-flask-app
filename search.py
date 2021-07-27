import requests
import json


def search(keywords, region="US"):

    key = ""
    with open("secrets.txt", "r") as secrets:
        key = secrets.readline().split()[1]

    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

    querystring = {"q": keywords, "region": region}

    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    _response = requests.request(
        "GET", url, headers=headers, params=querystring)

    response = json.loads(_response.text)

    return response['quotes']
