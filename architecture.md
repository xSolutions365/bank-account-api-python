# Architecture Documentation

## Table of Contents
- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Directory Structure](#directory-structure)
- [Backend Architecture](#backend-architecture)
- [Frontend Architecture](#frontend-architecture)
- [API Endpoints](#api-endpoints)
- [Data Model](#data-model)
- [Data Flow](#data-flow)
- [Testing Architecture](#testing-architecture)
- [Development Workflow](#development-workflow)

## Project Overview

The Bank Account Solution is a full-stack web application that demonstrates a simple banking system with account management capabilities. The project follows the Model-View-Controller (MVC) architectural pattern with a clear separation between the backend REST API and the frontend React application.

### Key Features
- Create, Read, Update, and Delete (CRUD) operations for bank accounts
- In-memory data storage for account information
- RESTful API architecture
- Responsive React-based user interface
- Prime number checking utility
- Comprehensive test coverage (unit and end-to-end tests)

## System Architecture

The application follows a **client-server architecture** with three main layers:

```
┌─────────────────────────────────────────────────────────────┐
│                    Bank Account UI (Frontend)               │
│                   React + Vite + TypeScript                 │
│                     Port: 5173                              │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          │ HTTP/REST API
                          │
┌─────────────────────────▼───────────────────────────────────┐
│                Bank Account API (Backend)                   │
│                   FastAPI + Python                          │
│                     Port: 3000                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Controllers (HTTP Request Handlers)                 │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                        │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  Services (Business Logic)                           │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                        │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  Models (Data Entities)                              │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                        │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  In-Memory Data Storage                              │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Backend
- **Framework**: FastAPI (Modern Python web framework)
- **ASGI Server**: Uvicorn (for running the application)
- **Language**: Python 3.9+
- **Testing**: pytest, pytest-cov, pytest-asyncio, httpx
- **Code Quality**: black (formatter), flake8 (linter), mypy (type checker)
- **Dependency Management**: pip / Poetry (optional)

### Frontend
- **Framework**: React 19
- **Language**: TypeScript
- **Build Tool**: Vite
- **UI Library**: Material-UI (MUI)
- **HTTP Client**: Axios
- **Testing**: Mocha + Selenium WebDriver
- **Package Manager**: npm

### Development Tools
- **Version Control**: Git
- **Browser Testing**: Chrome + ChromeDriver
- **API Documentation**: FastAPI automatic OpenAPI/Swagger docs

## Directory Structure

```
bank-account-api-python/
├── bank-account-api-py/           # Backend Python API
│   ├── app/                       # Main application package
│   │   ├── __init__.py
│   │   ├── main.py                # Application entry point, FastAPI app setup
│   │   ├── bank_account/          # Bank account module
│   │   │   ├── __init__.py
│   │   │   ├── controller.py      # HTTP request handlers/routes
│   │   │   ├── model.py           # BankAccount data model
│   │   │   └── service.py         # Business logic and data management
│   │   └── prime/                 # Prime number utility module
│   │       ├── __init__.py
│   │       ├── controller.py      # Prime number API endpoints
│   │       └── service.py         # Prime number checking logic
│   ├── tests/                     # Test suite
│   │   ├── __init__.py
│   │   ├── unit/                  # Unit tests
│   │   └── e2e/                   # End-to-end tests
│   ├── requirements.txt           # Python dependencies
│   ├── pyproject.toml             # Poetry configuration
│   ├── .flake8                    # Linter configuration
│   └── README.md                  # Backend-specific documentation
│
├── bank-account-ui/               # Frontend React application
│   ├── src/                       # Source code
│   │   ├── api/                   # API client functions
│   │   │   └── bankAccountApi.ts  # Bank account API calls
│   │   ├── components/            # Reusable React components
│   │   │   ├── Header.tsx         # Navigation header
│   │   │   ├── Footer.tsx         # Page footer
│   │   │   └── BankAccountTable.tsx # Account data table
│   │   ├── pages/                 # Page components
│   │   │   └── BankAccountsPage.tsx # Main accounts page
│   │   ├── styles/                # CSS styles
│   │   ├── App.tsx                # Root application component
│   │   └── main.tsx               # Application entry point
│   ├── test/                      # UI tests (Selenium)
│   ├── public/                    # Static assets
│   ├── package.json               # Node.js dependencies
│   ├── tsconfig.json              # TypeScript configuration
│   ├── vite.config.ts             # Vite build configuration
│   └── README.md                  # Frontend-specific documentation
│
├── training/                      # Training materials and documentation
│   ├── spec.md                    # Feature specification
│   ├── plan.md                    # Implementation plan
│   ├── tasks.md                   # Task breakdown
│   ├── quickstart.md              # Quick start guide
│   ├── data-model.md              # Data model documentation
│   ├── research.md                # Research notes
│   ├── checklists/                # Development checklists
│   └── contracts/                 # API contracts
│
├── images/                        # Documentation images
├── .github/                       # GitHub configuration
├── .specify/                      # Specify tool configuration
├── README.md                      # Main project documentation
└── architecture.md                # This file

```

## Backend Architecture

The backend follows the **MVC (Model-View-Controller)** pattern with a service layer:

### Layered Architecture

#### 1. Controllers (HTTP Layer)
**Location**: `app/*/controller.py`

Controllers handle HTTP requests and responses. They:
- Define API routes using FastAPI decorators
- Parse request parameters and body
- Call service layer methods
- Format responses
- Handle HTTP status codes

**Modules**:
- `bank_account.controller`: Manages bank account CRUD operations
- `prime.controller`: Provides prime number checking endpoint

#### 2. Services (Business Logic Layer)
**Location**: `app/*/service.py`

Services contain business logic and data manipulation. They:
- Implement core business rules
- Manage in-memory data storage
- Validate business constraints
- Raise appropriate exceptions for error cases

**Modules**:
- `BankAccountService`: Manages account lifecycle (create, read, update, delete)
- `PrimeService`: Implements prime number checking algorithm

#### 3. Models (Data Layer)
**Location**: `app/*/model.py`

Models define data structures and entity behavior. They:
- Define data classes and properties
- Implement domain logic (deposit, withdraw, transfer)
- Provide data validation
- Offer serialization methods (to_dict, from_dict)

**Modules**:
- `BankAccount`: Represents a bank account with operations

#### 4. Main Application
**Location**: `app/main.py`

The main application file:
- Creates and configures the FastAPI application
- Registers routers from controllers
- Configures CORS middleware
- Implements application lifecycle (startup/shutdown)
- Populates initial test data

## Frontend Architecture

The frontend follows a **component-based architecture** using React:

### Component Hierarchy

```
App
└── BankAccountsPage
    ├── Header
    ├── BankAccountTable
    └── Footer
```

### Layer Breakdown

#### 1. Components (`src/components/`)
Reusable UI components:
- **Header.tsx**: Navigation bar with branding
- **Footer.tsx**: Fixed footer with copyright
- **BankAccountTable.tsx**: Data table component that fetches and displays accounts

#### 2. Pages (`src/pages/`)
Page-level components that compose layouts:
- **BankAccountsPage.tsx**: Main page combining header, table, and footer

#### 3. API Layer (`src/api/`)
HTTP client functions for backend communication:
- **bankAccountApi.ts**: Defines API interface and fetch functions

#### 4. Entry Points
- **main.tsx**: Application bootstrap and React rendering
- **App.tsx**: Root component with routing (if applicable)

## API Endpoints

### Bank Account Endpoints

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| GET | `/api/BankAccount` | Get all accounts | None | Array of account objects |
| GET | `/api/BankAccount/{id}` | Get account by ID | None | Account object |
| POST | `/api/BankAccount` | Create new account | Account object | 201 Created |
| PUT | `/api/BankAccount/{id}` | Update account | Account object | 204 No Content |
| DELETE | `/api/BankAccount/{id}` | Delete account | None | 204 No Content |

### Prime Number Endpoint

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| GET | `/api/prime/{number}` | Check if number is prime | None | Boolean |

### Additional Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| GET | `/` | Root endpoint | API status message |

### API Documentation
FastAPI automatically generates interactive API documentation:
- **Swagger UI**: `http://localhost:3000/docs`
- **ReDoc**: `http://localhost:3000/redoc`

## Data Model

### BankAccount

The core entity of the application.

```python
class BankAccount:
    id: int                      # Unique identifier
    account_number: str          # Account number
    account_holder_name: str     # Name of account holder
    balance: float               # Current balance

    # Methods
    deposit(amount, transaction_type)
    withdraw(amount, transaction_type)
    transfer(to_account, amount)
    to_dict()
    from_dict(data)
```

**Business Rules**:
- Deposits must be positive and transaction type must end with "Credit"
- Withdrawals must be positive and transaction type must end with "Debit"
- Withdrawals cannot exceed current balance
- Transfers require sufficient funds in source account

### Data Storage

The application uses **in-memory storage** via class variables:
- `BankAccountService._accounts`: List storing all bank accounts
- Data is populated on application startup
- Data is lost when the application restarts
- Suitable for development and demonstration purposes

## Data Flow

### Typical Request Flow

1. **Client Request**: User interacts with React UI
2. **API Call**: Frontend makes HTTP request via `bankAccountApi.ts`
3. **Routing**: FastAPI routes request to appropriate controller
4. **Controller**: Parses request, calls service method
5. **Service**: Executes business logic, manipulates data
6. **Model**: Validates data, applies domain rules
7. **Response**: Service returns data to controller
8. **Serialization**: Controller converts to JSON response
9. **HTTP Response**: FastAPI sends response to client
10. **UI Update**: React component updates display

### Example: Get All Accounts

```
User clicks "View Accounts"
    ↓
BankAccountTable.tsx calls fetchBankAccounts()
    ↓
HTTP GET /api/BankAccount
    ↓
bank_account_router matches route
    ↓
get_all_accounts() controller function
    ↓
BankAccountService.get_all_accounts()
    ↓
Returns List[BankAccount]
    ↓
Controller converts to list of dicts
    ↓
FastAPI serializes to JSON
    ↓
HTTP 200 OK with JSON array
    ↓
BankAccountTable updates state and renders
```

## Testing Architecture

### Backend Tests (`bank-account-api-py/tests/`)

#### Unit Tests (`tests/unit/`)
Test individual components in isolation:
- **test_bank_account_model.py**: Tests BankAccount class methods
- **test_bank_account_service.py**: Tests BankAccountService logic
- **test_bank_account_controller.py**: Tests API endpoints

**Testing Tools**:
- pytest: Test framework
- httpx: HTTP client for testing FastAPI endpoints
- pytest-cov: Code coverage reporting

**Run Commands**:
```bash
pytest tests/unit                    # Run unit tests
pytest --cov=app --cov-report=html   # Run with coverage
```

#### End-to-End Tests (`tests/e2e/`)
Test complete workflows:
- **test_bank_account_e2e.py**: Tests full API workflows

### Frontend Tests (`bank-account-ui/test/`)

UI tests using Selenium WebDriver:
- Browser automation testing
- Integration testing with live API
- User interaction simulation

**Testing Tools**:
- Mocha: Test framework
- Selenium WebDriver: Browser automation
- ChromeDriver: Chrome browser driver

**Run Commands**:
```bash
npm run test:ui   # Run UI tests (requires API and UI running)
```

### Test Coverage
The project emphasizes comprehensive test coverage:
- Unit tests for business logic
- Integration tests for API endpoints
- End-to-end tests for complete workflows
- UI tests for frontend functionality

## Development Workflow

### Local Development Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/xSolutions365/bank-account-api-python
   cd bank-account-api-python
   ```

2. **Start Backend**
   ```bash
   cd bank-account-api-py
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 3000
   ```

3. **Start Frontend** (separate terminal)
   ```bash
   cd bank-account-ui
   npm install
   npm run dev
   ```

4. **Access Application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:3000/api/BankAccount
   - API Docs: http://localhost:3000/docs

### Code Quality Tools

#### Backend
- **black**: Code formatting (PEP 8 compliant)
- **flake8**: Linting and style checking
- **mypy**: Static type checking

#### Frontend
- **ESLint**: Code linting for TypeScript/React
- **TypeScript**: Static type checking

### Continuous Integration
The project includes GitHub Actions workflows (`.github/`) for:
- Automated testing
- Code quality checks
- Build validation

### Best Practices

1. **Code Organization**
   - Keep controllers thin (routing only)
   - Put business logic in services
   - Keep models focused on data and domain logic

2. **Testing**
   - Write tests before or alongside code
   - Aim for high code coverage
   - Test both happy paths and error cases

3. **API Design**
   - Follow RESTful conventions
   - Use appropriate HTTP methods and status codes
   - Provide clear error messages

4. **Frontend Development**
   - Keep components small and focused
   - Separate presentation from logic
   - Use TypeScript for type safety

## Future Enhancements

Potential architectural improvements:

1. **Data Persistence**
   - Replace in-memory storage with database (PostgreSQL, MongoDB)
   - Add ORM layer (SQLAlchemy, Tortoise ORM)

2. **Authentication & Authorization**
   - Implement user authentication
   - Add JWT token-based authorization
   - Role-based access control

3. **Additional Features**
   - Transaction history
   - Loan management
   - Interest calculation
   - Statistical analysis API

4. **Scalability**
   - Add caching layer (Redis)
   - Implement database connection pooling
   - Add load balancing support

5. **Deployment**
   - Containerization (Docker)
   - Cloud deployment (AWS, Azure, GCP)
   - CI/CD pipeline automation
