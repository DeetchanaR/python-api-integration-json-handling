# Import requests library
import requests

try:
    # API URL
    url = "https://jsonplaceholder.typicode.com/users"

    # Send GET request to API
    response = requests.get(url)

    # Check if request was successful
    response.raise_for_status()

    # Convert JSON response into Python data
    users = response.json()

    print("User List:\n")

    # Search users from a specific city
    search_city = "South Christy"

    # Display matching user information
    for user in users:
        if user["address"]["city"] == search_city:
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])
            print("-" * 30)

# Handle API-related errors
except requests.exceptions.RequestException as e:
    print("API Error:", e)

# Handle other unexpected errors
except Exception as e:
    print("An error occurred:", e)
