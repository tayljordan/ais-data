import requests

url = "https://www.flagshiptechnologies.com/api/g4m8z9p0r1c5a6b7d2e3fql"
data = {
    "lat": "38.0",
    "lon": "-122.5",
    "radius": "50"
}

response = requests.post(url, data=data)

# Print the response
print(response.text)
