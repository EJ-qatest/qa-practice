import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_user():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    users = response.json()
    assert len(users) == 10
    for user in users:
    
        assert "@" in user["email"] 
   
