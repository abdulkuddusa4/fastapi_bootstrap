# FastAPI Bootstrap

A clean, production-ready FastAPI starter template featuring JWT authentication, customer management, SQLite database integration, and environment-based configuration — all managed with the modern [`uv`](https://github.com/astral-sh/uv) package manager.

---

## Features

- **FastAPI** — High-performance async web framework
- **JWT Authentication** — Secure token-based auth via the `auth` module
- **Customer Module** — Ready-to-extend CRUD resource example
- **SQLite** — Lightweight database with `db.py` setup out of the box
- **`config.py`** — Centralized settings powered by `.env` variables
- **`uv`** — Ultra-fast Python package manager for dependency management
- **`pyproject.toml`** — Modern Python project metadata and dependency declaration

---

## Project Structure

```
fastapi_bootstrap/
├── auth/               # JWT authentication logic (login, token, dependencies)
├── customer/           # Customer resource (routes, schemas, models)
├── main.py             # FastAPI app entry point, router registration
├── db.py               # Database engine and session setup
├── config.py           # App settings loaded from .env
├── .env                # Environment variables (not committed in production)
├── db.sqlite3          # SQLite database file
├── pyproject.toml      # Project metadata and dependencies
└── uv.lock             # Locked dependency versions
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- [`uv`](https://github.com/astral-sh/uv) installed

```bash
pip install uv
```

### 1. Clone the repository

```bash
git clone https://github.com/abdulkuddusa4/fastapi_bootstrap.git
cd fastapi_bootstrap
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Copy the `.env` file and fill in your values:

```bash
cp .env .env.local
```

Example `.env`:

```env
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./db.sqlite3
```

### 4. Run the development server

```bash
uv run uvicorn main:app --reload
```

The API will be available at **http://localhost:8000**

---

## API Documentation

FastAPI provides interactive docs automatically:

| Interface | URL |
|-----------|-----|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

## Authentication

The `auth` module handles user login and JWT token issuance. Protected routes use FastAPI dependency injection to verify tokens.

**Login flow:**

```
POST /auth/token
  → Returns: { access_token, token_type }
```

Include the token in subsequent requests:

```
Authorization: Bearer <access_token>
```

---

## Customer Module

The `customer` module provides a base CRUD resource that can be extended to fit your domain model. It demonstrates the recommended pattern for organizing routes, schemas, and database operations.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM / DB layer |
| [SQLite](https://www.sqlite.org/) | Database |
| [python-jose](https://github.com/mpdavis/python-jose) | JWT encoding/decoding |
| [passlib](https://passlib.readthedocs.io/) | Password hashing |
| [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) | Env-based configuration |
| [uv](https://github.com/astral-sh/uv) | Package management |

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## License

This project is open-source. See [LICENSE](LICENSE) for details.