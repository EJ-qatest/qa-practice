# CONFIDENCE ROUND - Challenge 3: Find the bugs
# This file has 5 bugs. Each one is something you've already seen and fixed.
# Run it, read the errors, fix one bug at a time. Target: 3 passed.

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user_two():
    response = requests.get(f"{BASE_URL}/users/2")

    assert response.status_code == 200

    user = response.json()
    assert user["id"] == 2


def test_create_comment():
    new_comment = {"postId": 1, "name": "Maru", "email": "maru@example.com", "body": "Great post"}

    response = requests.post(f"{BASE_URL}/comments", json=new_comment)

    assert response.status_code == 201
    created = response.json()
    assert created["email"] == "maru@example.com"


def test_post_one_has_a_title():
    response = requests.get(f"{BASE_URL}/posts/1")
    post = response.json()
    assert post["title"] != ""
