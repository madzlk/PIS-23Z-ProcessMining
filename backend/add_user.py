import requests

# Replace with your FastAPI server URL
base_url = "http://localhost:8080"

def add_user(username, email, password, user_uid):
    url = f"{base_url}/users/"
    user_data = {
        "username": username,
        "email": email,
        "password": password,
        "user_uid": user_uid,
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
add_user("johwddawddw_doe", "jodwwdoe@exadwadmple.com", "securepassword", "user1wda43q")
