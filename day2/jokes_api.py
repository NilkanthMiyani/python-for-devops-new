import requests
import json

jokes_url = "https://official-joke-api.appspot.com/random_joke"
dad_jokes_url = "https://icanhazdadjoke.com/"


def get_joke(url_type,mood):
    headers = {
        "Accept": "application/json"
    }
    joke = requests.get(url=url_type, headers=headers)
    data = joke.json()  # Convert API response to Python dictionary

    filename = f"{mood}_joke.json"
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

    # Append the new joke data to the list
    existing_data.append(data)

    # Write the updated list back to the JSON file with indentation for readability
    with open(filename, "w") as f:
        json.dump(existing_data, f, indent=4)
    print(f"JSON output appended to {filename}")

    if mood == "dad":
        final_joke = data["joke"]
    if mood == "pj":
        final_joke = data["setup"] + data["punchline"]
    return final_joke



mood = input("Which joke would you like to hear? eg. (DAD,PJ)")
if mood == "dad":
    url_type = dad_jokes_url
elif mood == "pj":
    url_type = jokes_url
else:
    print("Invalid input, defaulting to Programming Joke")
    url_type = jokes_url

final_joke = get_joke(url_type,mood)

print(final_joke)