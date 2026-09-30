# Architecture

## Logical Architecture

```text
React UI
   |
   | HTTPS/REST
   v
FastAPI
   |
   +--> Authentication/JWT
   |
   +--> PostgreSQL
   |
   +--> Object Storage
   |
   +--> AI Provider
            |
            +--> Local fallback
            +--> Gemini
```

## Cloud Responsibilities

### Compute
FastAPI runs as a web service/container.

### Storage
Uploaded objects are separated from relational records.

### Database
User/profile/plan metadata is relational.

### AI
AI is accessed through a provider interface.

### Security
Authentication and authorization happen before user-specific operations.

## Request Example

```text
POST /api/v1/plans/generate
        |
        v
JWT verification
        |
        v
Find authenticated user
        |
        v
Find that user's profile
        |
        v
AI provider
        |
        v
Validate result
        |
        v
Save plan with user_id
        |
        v
Return JSON
```
