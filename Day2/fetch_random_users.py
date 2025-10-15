import requests

def fetch_random_users(count=5):
    """
    Fetch random users from randomuser.me API and print their full names.
    """
    url = f"https://randomuser.me/api/?results={count}"
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for HTTP errors
    data = response.json()       # Deserialize JSON
    users = data.get("results", [])
    
    for i, user in enumerate(users, start=1):
        name = user["name"]
        full_name = f"{name['title']} {name['first']} {name['last']}"
        print(f"{i}. {full_name}")

if __name__ == "__main__":
    fetch_random_users()
