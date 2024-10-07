Here’s the updated markdown for the landing page, including details about the AISHUB API wrapper and the formatted output example:

### AIS API Wrapper for AISHUB

This repository contains details an API connection designed to interact with the AISHUB API, a service that provides real-time AIS (Automatic Identification System) data. The API enable fetching, processing, and filtering vessel data from AISHUB, converting it into formats that can be easily used for maritime analytics. The purpose of this site is to extend AIS data to educational institutions and researchers. 

### Overview of the Scripts

#### `/home/tayljordan/flagship/ais/aishub_api_call.py`

This script retrieves AIS data from the AISHUB API in CSV format and saves it locally as `ais_output.csv`. It uses parameters such as `username`, `format`, and `output`, and includes error handling to manage failed requests.

- **Key Points:**
  - Sends a GET request to `https://data.aishub.net/ws.php` to fetch vessel data.
  - Saves the data as `ais_output.csv`.
  - Logs errors and handles request exceptions.

#### `/home/tayljordan/flagship/ais/convert_to_feather.py`

This script processes the AIS data from the CSV format, filters it, and converts it to Feather format. It also includes calculations for new vessel positions and integrates vessel type and navigational status.

- **Key Points:**
  - Reads the AIS data from the CSV file.
  - Filters out unwanted vessel types and data.
  - Applies a `calculate_new_position` function to update vessel coordinates.
  - Maps vessel types and navigational statuses.
  - Converts the processed DataFrame to a Feather file (`ais_output.feather`).

#### `/home/tayljordan/flagship/ais/shippingintel_api_call.py`

This script processes the AIS data stored in Feather format. It calculates a bounding box around a specified latitude and longitude, filters vessels within a given radius, and returns the filtered data in JSON format.

- **Key Points:**
  - Reads the Feather file (`ais_output.feather`).
  - Uses a bounding box to find vessels within a specific geographical range.
  - Returns vessel data in JSON format.

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

#### Endpoint: `/api/ais_temp`

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