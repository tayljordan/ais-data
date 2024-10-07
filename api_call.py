import requests

url = "https://www.flagshiptechnologies.com/api/[ENTER API KEY HERE]"
data = {
    "lat": "38.0",
    "lon": "-122.5",
    "radius": "50"
}

response = requests.post(url, data=data)

# Print the response
print(response.text)
