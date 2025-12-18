# Bank Account API - Python

Python implementation of the Bank Account API using FastAPI.

## Setup

### Using pip
```bash
pip install -r requirements.txt
```

### Using Poetry (recommended)
```bash
poetry install
```

## Running the Application

### Development mode
```bash
# Using uvicorn directly
uvicorn app.main:app --reload --port 3000

# Or using Poetry
poetry run uvicorn app.main:app --reload --port 3000
```

The API will be available at: http://localhost:3000/api/BankAccount

## Testing

### Run all tests
```bash
pytest
```

### Run with coverage
```bash
pytest --cov=app --cov-report=html
```

### Run unit tests only
```bash
pytest tests/unit
```

### Run e2e tests only
```bash
pytest tests/e2e
```

## Code Quality

### Format code
```bash
black app tests
```

### Lint code
```bash
flake8 app tests
```

### Type checking
```bash
mypy app
```
