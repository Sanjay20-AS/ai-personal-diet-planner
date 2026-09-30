# Deployment Guide

## 1. Database

Create a PostgreSQL database with a free-tier managed provider such as Supabase.

Copy its PostgreSQL connection string into:

```env
DATABASE_URL=postgresql+psycopg://...
```

## 2. Backend

Deploy the `backend` directory to a Python web service.

Build/install:

```bash
pip install -r requirements.txt
```

Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Environment variables:

```text
SECRET_KEY=<long-random-secret>
DATABASE_URL=<postgres-url>
CORS_ORIGINS=<frontend-url>
AI_PROVIDER=local
STORAGE_PROVIDER=local
```

For an external AI provider:

```text
AI_PROVIDER=gemini
GEMINI_API_KEY=<secret>
```

## 3. Frontend

Set:

```env
VITE_API_URL=https://your-backend-domain/api/v1
```

Build:

```bash
npm run build
```

Deploy the `dist` output as a static site.

## 4. Storage

For the student demonstration, local storage is enough for the fully executable project.

For a cloud deployment, implement the same `StorageProvider` interface using Supabase Storage and store only object paths/metadata in PostgreSQL.

## 5. Security Checklist

- Never commit `.env`
- Use HTTPS in production
- Use a strong secret key
- Restrict CORS to the deployed frontend
- Keep cloud service keys in deployment secrets
- Validate file size/type
- Enforce user ownership on every user resource
- Do not use real health data
