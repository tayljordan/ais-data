Here is the updated markdown including the correct endpoint with the API key placeholder:

### AIS API Wrapper for AISHUB

This repository contains details of an API connection designed to interact with the AISHUB API, a service that provides real-time AIS (Automatic Identification System) data. The API enables fetching, processing, and filtering vessel data from AISHUB, converting it into formats that can be easily used for maritime analytics. The purpose of this repository is to extend AIS data access to educational institutions and researchers.

### Instructions for Using the API in Python

To use the AIS API wrapper in Python, follow these steps:

1. **Install the required libraries**:
   If not already installed, make sure you have the `requests` library. You can install it using:
   
   ```bash
   pip install requests
   ```

2. **Send a POST request to the API**:
   Use the following Python code to send a request to the API and retrieve vessel data within a specified radius.

   ```python
   import requests

   url = "https://www.flagshiptechnologies.com/api/[ENTER API KEY HERE]"
   data = {
       "lat": 37.7749,   # Latitude of the center point
       "lon": -122.4194, # Longitude of the center point
       "radius": 50      # Radius in kilometers (maximum 100 km)
   }

   response = requests.post(url, json=data)

   # Print the response (vessel data in JSON format)
   if response.status_code == 200:
       print(response.json())
   else:
       print(f"Error: {response.status_code} - {response.text}")
   ```

3. **Interpreting the response**:
   The response will be in JSON format and will include real-time vessel data such as `MMSI`, `latitude`, `longitude`, `speed`, and more.

### Sample Output from the API

Here is an example of the API response (shortened and formatted for clarity):

```json
[
    {
        "MMSI": 367514780,
        "NAME": "OCEAN SCOUT",
        "TSTAMP": "2024-10-07 02:06:55 GMT",
        "NAVSTAT": 5,
        "DEST": "RCH3 PIER",
        "ETA": "10-01 20:00",
        "DRAUGHT": 2.6,
        "COG": 311,
        "SOG": 0.0,
        "LATITUDE": 37.90578,
        "LONGITUDE": -122.37032,
        "VESSEL_TYPE": "Anti-pollution",
        "STATUS": "Moored"
    },
    {
        "MMSI": 368212750,
        "NAME": "MADISON LYNNE",
        "TSTAMP": "2024-10-07 02:07:47 GMT",
        "NAVSTAT": 0,
        "DEST": "Unknown",
        "ETA": "00-00 24:60",
        "DRAUGHT": 1.0,
        "COG": 360,
        "SOG": 0.0,
        "LATITUDE": 37.77415,
        "LONGITUDE": -122.38425,
        "VESSEL_TYPE": "Passenger",
        "STATUS": "Underway using engine"
    }
]
```

### Terrestrial Automated Information Systems (AIS) API

#### Endpoint: `/api/[ENTER API KEY HERE]`

- **Method**: `POST`
- **Description**: Retrieves real-time vessel positions within a specified radius, using latitude, longitude, and radius as input parameters.

#### Parameters:
- `lat` (float, required): Latitude of the center point.
- `lon` (float, required): Longitude of the center point.
- `radius` (int, required): Radius in kilometers (maximum 100 km).

#### Request Example:
```json
{
    "lat": 37.7749,
    "lon": -122.4194,
    "radius": 50
}
```

#### Success Response:
```json
[
    {
        "MMSI": "123456789",
        "LATITUDE": 37.7749,
        "LONGITUDE": -122.4194,
        "SPEED": 15.5,
        "COURSE": 90.0,
        "TIMESTAMP": "2024-07-08T12:34:56Z"
    }
]
```

For more details, contact **Shipping Intel** at [info@shippingintel.com].