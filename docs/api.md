# API

Base URL:

```text
/api/v1
```

## Authentication

### Register

```http
POST /auth/register
```

### Login

```http
POST /auth/login
```

Response:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

Use:

```http
Authorization: Bearer <token>
```

## Profile

```http
GET /profile
PUT /profile
```

## Plans

```http
POST /plans/generate
GET /plans
GET /plans/{id}
DELETE /plans/{id}
```

## Files

```http
POST /files/upload
GET /files
DELETE /files/{id}
```

## Dashboard

```http
GET /dashboard
```

## Health

```http
GET /health
```

Interactive documentation is automatically available at:

```text
/docs
```
