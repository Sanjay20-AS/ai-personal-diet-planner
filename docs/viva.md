# Viva / Interview Preparation

## Why FastAPI?

It is lightweight, Python-based, supports REST APIs and automatic OpenAPI documentation.

## Why PostgreSQL?

Relational user data such as profiles and plan metadata fits well in SQL. JSONB can hold flexible AI output.

## Why object storage?

Files are binary objects and should not be stored directly inside relational tables.

## Why a local AI fallback?

It keeps the project executable without a paid API and demonstrates provider abstraction.

## What is cloud storage?

Cloud storage stores objects separately from compute and database services and provides scalable access.

## How is user data isolated?

Every protected database query filters by the authenticated user's ID.

## What happens if the AI API fails?

The provider abstraction can switch to local mode. In production, the system should also log failures and expose useful error messages.

## How is the application scalable?

The FastAPI service is designed to be stateless. User state is stored in external database/storage services rather than process memory.

## What is CI/CD?

The GitHub Actions workflow automatically installs dependencies, runs backend tests and builds the frontend after repository changes.

## What are the security measures?

JWT authentication, password hashing, authorization checks, input validation, file type/size checks, CORS configuration and environment-based secrets.

## What would you improve for production?

- Managed secrets
- Redis rate limiting
- Structured logs
- Metrics/tracing
- Database migrations with Alembic
- Object storage signed URLs
- Better AI output validation
- Automated backups
- More comprehensive frontend tests
- Privacy/compliance review
