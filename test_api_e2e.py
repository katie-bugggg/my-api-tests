import pytest
import requests


def test_post_lifecycle_e2e(base_url):
    # --- ШАГ 1: СОЗДАНИЕ (POST) ---
    new_post = {"title": "E2E Test", "body": "Hello", "userId": 1}
    # Склеиваем адрес: "https://jsonplaceholder.typicode.com" + "/posts"
    post_response = requests.post(base_url + "/posts", json=new_post)
    assert post_response.status_code == 201

    # --- ШАГ 2: ЧТЕНИЕ (GET) ---
    # В реальной системе мы бы взяли ID созданного поста.
    # Так как наш сервер учебный, мы сымитируем чтение поста №1
    get_response = requests.get(base_url + "/posts/1")
    assert get_response.status_code == 200

    # --- ШАГ 3: ОБНОВЛЕНИЕ (PUT) ---
    updated_post = {"title": "E2E Updated", "body": "Hello", "userId": 1}
    put_response = requests.put(base_url + "/posts/1", json=updated_post)
    assert put_response.status_code == 200
    assert put_response.json()["title"] == "E2E Updated"

    # --- ШАГ 4: УДАЛЕНИЕ (DELETE) ---
    delete_response = requests.delete(base_url + "/posts/1")
    assert delete_response.status_code == 200