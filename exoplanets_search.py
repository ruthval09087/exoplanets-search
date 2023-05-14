import requests

# Define the API endpoint
url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI"

# Set the API parameters
params = {
    "table": "exoplanets",  # Table name for exoplanet data
    "format": "json"  # Response format
}

# Send a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Retrieve information about exoplanets
    for planet in data:
        planet_name = planet["pl_name"]
        discovery_method = planet["pl_discmethod"]
        print("Planet Name:", planet_name)
        print("Discovery Method:", discovery_method)
        print("-----")
else:
    print("Error:", response.status_code)
