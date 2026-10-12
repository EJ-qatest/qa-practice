# Lesson 10: API testing - testing the "backend" directly, no browser
# Read it first. Guess. Then run it.

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_one_user():
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Leanne Graham"


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200

    posts = response.json()
    assert len(posts) == 100


def test_missing_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/9999")

    assert response.status_code == 404

def test_get_one_post():
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    post = response.json()
    assert post["id"] == 1
    assert post["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert post["title"] != "", "Post title should not be empty"


def test_create_post():
    new_post = {"title": "My first API post", "body": "Hello from Maru", "userId": 1}

    response = requests.post(f"{BASE_URL}/posts", json=new_post)

    assert response.status_code == 201

    created = response.json()
    assert created["title"] == "My first API post"
    assert "id" in created
    
def test_update_post():
    updated_post = {"title": "My updated title", "body": "Changed by Maru", "userId": 1}

    response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)

    assert response.status_code == 200

    changed_post = response.json()
    assert changed_post["title"] == "My updated title"

def test_delete_post():

    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
     
    

    
    
