# AI-Powered Personal Diet Planner with Cloud Storage

A student-friendly, industry-oriented Cloud Computing project demonstrating:

- React frontend
- FastAPI REST backend
- JWT authentication
- SQLite local development / PostgreSQL cloud-ready database
- User-specific data
- Local file storage / Supabase Storage adapter
- AI diet-plan generation with local fallback
- Docker
- Pytest
- GitHub Actions CI
- Cloud deployment configuration
- Swagger API documentation

> **Important:** This project generates educational/demo meal plans. It is not medical or clinical nutrition advice. Use synthetic/demo data only.

## Architecture

```text
                    Browser
                       |
                 React + Vite
                       |
                    REST API
                       |
                 FastAPI Backend
          _____________|________________
         |             |                |
     Authentication   Database          AI
         |             |                |
       JWT          SQLite/Postgres   Local/Gemini
                       |
                  File Storage
                 Local/Supabase
```

## Features

1. Register and login
2. JWT authentication
3. Create/update personal demo profile
4. Generate an AI-style meal plan
5. Save plan history
6. Upload files
7. List/delete own files
8. Dashboard statistics
9. Local mode without paid cloud services
10. Cloud-ready PostgreSQL/Supabase configuration
11. Swagger API documentation
12. Automated tests
13. Docker support
14. GitHub Actions CI

## Project Structure

```text
ai-personal-diet-planner/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
├── frontend/
│   ├── src/
│   ├── package.json
│   ├── Dockerfile
│   └── .env.example
├── docs/
│   ├── architecture.md
│   ├── api.md
│   ├── deployment.md
│   └── viva.md
├── database/
│   └── schema.sql
├── .github/workflows/ci.yml
├── docker-compose.yml
└── README.md
```

## Local Setup

### 1. Backend

Python 3.11+ is recommended.

```bash
cd backend
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env`.

Run:

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## Demo Login

You can create your own demo account from Register.

Never commit real passwords, API keys or cloud credentials.

## AI Modes

Default:

```env
AI_PROVIDER=local
```

The local provider generates deterministic demo plans without an external API.

Optional Gemini provider:

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=your_key
```

The AI interface is intentionally provider-based so the application still works when an external AI API is unavailable.

## Storage Modes

Default:

```env
STORAGE_PROVIDER=local
```

Files are stored under:

```text
backend/storage/
```

For a cloud adapter, configure the Supabase variables in `.env`. The project keeps storage behind an interface so local development does not depend on a cloud service.

## Database Modes

Local:

```env
DATABASE_URL=sqlite:///./dietplanner.db
```

PostgreSQL:

```env
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/postgres
```

## Docker

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:5173
```

Backend:

```text
http://localhost:8000
```

## Testing

```bash
cd backend
pytest
```

## Cloud Deployment

A simple student deployment can use:

- React frontend: Vercel or Render Static Site
- FastAPI backend: Render or another container/web-service provider
- PostgreSQL: Supabase
- Object storage: Supabase Storage
- AI: Gemini or local provider

Set production environment variables in the deployment dashboard rather than committing `.env`.

See `docs/deployment.md`.

## Cloud Computing Concepts Demonstrated

| Concept | Implementation |
|---|---|
| SaaS/web application | React browser application |
| IaaS/containerization | Docker |
| REST API | FastAPI |
| Authentication | JWT |
| Cloud DB | PostgreSQL-ready |
| Object storage | Storage abstraction / Supabase-ready |
| AI service | Provider abstraction |
| Scalability | Stateless API design |
| Security | JWT, validation, CORS, file checks |
| DevOps | GitHub Actions |
| Testing | Pytest |
| Configuration | Environment variables |

## Limitations

- Local AI mode is intentionally simple and is not a nutrition expert.
- No medical diagnosis is performed.
- Cloud provider free-tier limits can change.
- Demo data should be synthetic.
- Production systems would require stronger observability, secret management, rate limiting, backups and privacy controls.

## Screenshots for GitHub

Capture these after running the project:

1. Login
2. Register
3. Dashboard
4. Profile
5. Generate Plan
6. Generated Plan
7. Plan History
8. File Upload
9. Swagger `/docs`
10. Database/cloud storage
11. GitHub Actions passing
12. Deployed application

## Author

Sanjay A  
B.Tech Computer Science and Business Systems

