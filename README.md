
```
project/
├── app/
│   ├── __init__.py
│   ├── main.py                  # App factory, lifespan, middleware
│   ├── config.py                # Settings via pydantic-settings
│   ├── dependencies.py          # Shared FastAPI dependencies
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── engine.py            # Engine + session factory
│   │   └── migrations/          # Alembic lives here
│   │       ├── env.py
│   │       └── versions/
│   │
│   ├── models/                  # SQLModel table=True models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── base.py              # Shared base (id, created_at, updated_at)
│   │
│   ├── schemas/                 # Request/response shapes (no table=True)
│   │   ├── user.py
│   │   └── common.py            # Pagination, error response, etc.
│   │
│   ├── routers/                 # One file per resource
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── auth.py
│   │
│   ├── services/                # Business logic layer
│   │   ├── user.py
│   │   └── auth.py
│   │
│   ├── crud/                    # Raw DB operations only
│   │   └── user.py
│   │
│   ├── core/
│   │   ├── security.py          # JWT, hashing
│   │   ├── exceptions.py        # Custom exception classes
│   │   └── middleware.py        # Logging, request ID, CORS setup
│   │
│   └── utils/
│       └── email.py             # Misc helpers
│
├── tests/
│   ├── conftest.py              # Test DB, fixtures
│   ├── test_users.py
│   └── test_auth.py
│
├── .env
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```