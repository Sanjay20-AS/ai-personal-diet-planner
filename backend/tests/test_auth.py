def test_register_and_login(client):
    r = client.post("/api/v1/auth/register", json={
        "email": "demo@example.com",
        "password": "password123"
    })
    assert r.status_code == 200

    r = client.post("/api/v1/auth/login", json={
        "email": "demo@example.com",
        "password": "password123"
    })
    assert r.status_code == 200
    assert "access_token" in r.json()
