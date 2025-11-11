## Folder Structure

This project follows a structured organization to separate concerns, making it scalable and maintainable. Below is a description of the key folders and their purposes:

### Root Level
- **alembic.ini**: Configuration file for Alembic, the database migration tool.
- **main.py**: The entry point of the FastAPI application, where the app is created and configured.
- **pyproject.toml**: Project metadata and dependency management configuration for tools like uv or pip.
- **README.md**: Documentation for the project, including setup and usage instructions.

### src/
The main source code directory, following Python packaging conventions.

#### app/
Application-specific business logic, organized by domain or feature.

- **user/**: Handles user-related functionality.
  - **routes.py**: Defines FastAPI routes/endpoints for user operations (e.g., CRUD).
  - **schema.py**: Pydantic models for request/response validation and serialization.
  - **typed.py**: Type hints and annotations specific to the user module.
  - **service/**: Business logic layer for user operations, separating concerns from routes.

#### core/
Shared utilities, configurations, and foundational components used across the application.

- **artifacts/**: Custom code artifacts like decorators and interfaces.
  - **decorator/**: Reusable decorators for common functionality (e.g., authentication, logging).
  - **interface/**: Abstract interfaces defining contracts (e.g., service.py for service abstractions).
  - **typed/**: Shared type definitions and annotations.

- **config/**: Configuration management, such as settings for the app, database, etc.
- **lib/**: Utility libraries and helper functions (e.g., logging, validation helpers).
- **security/**: Security-related modules, like authentication, authorization, and encryption.

#### db/
Database-related code, including models and migrations.

- **alembic/**: Alembic migration management.
  - **env.py**: Environment configuration for migrations.
  - **README**: Documentation for the migrations setup.
  - **script.py.mako**: Template for generating migration scripts.
  - **versions/**: Directory for versioned migration scripts.

- **models/**: SQLAlchemy ORM models representing database tables.
- **repository/**: Repository pattern implementations for data access, abstracting database operations.

### Create Project
```
uv init --python 3.12 --app 
```

### Run the project
```
uv run main.py
```

### Install Basic Packages
```
uv add fastapi --extra standard

```

### Install Alembic
```
uv add alembic
alembic init src/db/alembic
```

### SQLAlchemy

SQLAlchemy Documentation

[SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)

