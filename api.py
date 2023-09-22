import requests

BASE_URL = "https://gorest.co.in/public-api"

def get_todos():
    endpoint = f"{BASE_URL}/todos"
    response = requests.get(endpoint)
    todos = response.json()
    # Print the first 10 todo items
    print("First 10 todo items:")
    for todo in todos['data'][:10]:
        print(todo)

def get_inactive_users():
    endpoint = f"{BASE_URL}/users"
    params = {
        'status': 'inactive'
    }
    response = requests.get(endpoint, params=params)
    users = response.json()
    # Print the first 10 inactive users
    print("First 10 inactive users:")
    for user in users['data'][:10]:
        print(user)

if __name__ == "__main__":
    print("Getting todos...")
    get_todos()
    
    print("\nGetting inactive users...")
    get_inactive_users()
