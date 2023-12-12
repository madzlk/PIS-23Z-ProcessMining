import requests

# Replace with your FastAPI server URL
base_url = "http://127.0.0.1:8080"


def add_user(username, email):
    url = f"{base_url}/users/"
    user_data = {
        "username": username,
        "email": email,
    }

    response = requests.post(url, json=user_data)

    if response.status_code == 200:
        print("User added successfully!")
        print("User details:")
        print(response.json())
    else:
        print(f"Failed to add user. Status code: {response.status_code}")
        print(f"Error details: {response.text}")

# Example usage


add_user("johqeweqwddawddw_doe", "jodwwdoe@exadwadmple.com")
