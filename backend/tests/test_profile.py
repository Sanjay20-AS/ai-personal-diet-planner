def get_token(client):
    client.post("/api/v1/auth/register", json={
        "email": "profile@example.com",
        "password": "password123"
    })
    return client.post("/api/v1/auth/login", json={
        "email": "profile@example.com",
        "password": "password123"
    }).json()["access_token"]

def test_profile_save(client):
    token = get_token(client)
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "age": 21,
        "height_cm": 170,
        "weight_kg": 65,
        "activity_level": "moderate",
        "diet_preference": "vegetarian",
        "allergies": "peanuts",
        "goal": "general wellness",
        "meals_per_day": 4
    }
    r = client.put("/api/v1/profile", json=payload, headers=headers)
    assert r.status_code == 200
    assert r.json()["diet_preference"] == "vegetarian"
