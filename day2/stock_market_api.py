import requests
import json

api_url = "https://www.alphavantage.co/"

API_KEY = "BL6VGF2SW0ZWBW2A"
# symbol = "AMZN"
interval = "1min"

def get_stock_market_data(symbol):
    if is_timeseries:
        query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&interval={interval}&apikey={API_KEY}"
    else:
        query = f"query?symbol={symbol}&interval={interval}&apikey={API_KEY}"

    response = requests.get(url=api_url+query)
    data = response.json()  # Convert API response to Python dictionary

    filename = f"{symbol}_stock_data.json"
    try:
        # Try to open and read existing JSON data from the file
        with open(filename, "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or has invalid JSON, start with an empty list
        existing_data = []

    # If existing data is a single dict (from an older save), wrap it in a list
    if isinstance(existing_data, dict):
        existing_data = [existing_data]

    # Append the new stock data to the list
    existing_data.append(data)

    # Write the updated list back to the JSON file with indentation for readability
    with open(filename, "w") as f:
        json.dump(existing_data, f, indent=4)
    print(f"JSON output appended to {filename}")

    for k,v in data.items():
        if is_timeseries:
            print(k, ":", v)
        else:
                continue


symbol = input("Enter the symbol you want for Stock Market API eg. (AMZN, IBM, GOGL, .. ) ")
is_timeseries = True
get_stock_market_data(symbol)