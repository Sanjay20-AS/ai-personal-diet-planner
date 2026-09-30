def setup(client):
    client.post("/api/v1/auth/register", json={
        "email": "plans@example.com",
        "password": "password123"
    })
    token = client.post("/api/v1/auth/login", json={
        "email": "plans@example.com",
        "password": "password123"
    }).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    client.put("/api/v1/profile", json={
        "age": 21,
        "height_cm": 170,
        "weight_kg": 65,
        "activity_level": "moderate",
        "diet_preference": "vegetarian",
        "allergies": "",
        "goal": "general wellness",
        "meals_per_day": 4
    }, headers=headers)
    return headers

def test_generate_plan(client):
    headers = setup(client)
    r = client.post("/api/v1/plans/generate", headers=headers)
    assert r.status_code == 200
    data = r.json()
    assert data["ai_provider"] == "local"
    assert data["daily_calories"] > 0

def test_user_cannot_access_other_plan(client):
    headers = setup(client)
    plan = client.post("/api/v1/plans/generate", headers=headers).json()

    client.post("/api/v1/auth/register", json={
        "email": "other@example.com",
        "password": "password123"
    })
    token = client.post("/api/v1/auth/login", json={
        "email": "other@example.com",
        "password": "password123"
    }).json()["access_token"]

    r = client.get(
        f"/api/v1/plans/{plan['id']}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert r.status_code == 404
