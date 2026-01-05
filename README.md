# Bank Account Solution

This solution contains a simple Bank Account MVC project with a REST API back-end and a React front-end built with Vite.

## Project Overview

### Bank Account API (Python)
- **bank_account/controller.py**: Contains the bank account router which handles HTTP requests related to bank accounts.
- **bank_account/model.py**: Defines the `BankAccount` class representing a bank account with properties like `id`, `account_number`, `account_holder_name`, and `balance`.
- **bank_account/service.py**: Implements the `BankAccountService` class that provides business logic for managing bank accounts.

### **Bank Account UI**
The **Bank Account UI** is a React-based front-end application built with Vite that provides a user-friendly interface to interact with the API.

- **`components/Header.tsx`**: Renders the navigation bar with links.
- **`components/Footer.tsx`**: Displays a fixed footer with copyright information.
- **`components/BankAccountTable.tsx`**: Fetches and displays bank account data in a table format.
- **`api/bankAccountApi.ts`**: Handles API calls to retrieve bank accounts.
- **`pages/BankAccountsPage.tsx`**: Main page that renders the `BankAccountTable` and integrates layout components.

### Tests
- **test_bank_account_controller.py**: Contains unit tests for the bank account controller to ensure correct handling of HTTP requests.
- **test_bank_account_service.py**: Contains unit tests for the `BankAccountService` to verify business logic and data manipulation.
- **test_bank_account_model.py**: Contains unit tests for the `BankAccount` model to verify the correctness of its methods.
- **test_bank_account_e2e.py**: Contains end-to-end tests to verify the complete workflow of the application.

## Prerequisites

Before setting up this project, ensure you have the following installed:

- **Python 3.9+**: Required for the backend API
- **pip**: Python package manager (usually comes with Python)
- **Node.js 18+** and **npm**: Required for the frontend UI
- **Chrome browser**: Required for running UI tests (with matching ChromeDriver version)

Optional but recommended:
- **Poetry**: Modern Python dependency management tool

## Setup Instructions

1. Clone the repository:
   ```sh
   git clone https://github.com/xSolutions365/bank-account-api-python
   ```
### Running the API

1. Navigate to the project directory:
   ```sh
   cd bank-account-api-py
   ```

2. Install the dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

3. Run the API:
   ```sh
   python3 -m uvicorn app.main:app --reload --port 3000
   ```

4. Open the browser and navigate to:
   ```
   http://localhost:3000/api/BankAccount
   ```
   This will display the list of bank accounts.

### Running the UI

1. Open a new terminal and navigate to the UI project directory:
   ```sh
   cd bank-account-ui
   ```

2. Install the dependencies:
   ```sh
   npm install
   ```

3. Run the development server:
   ```sh
   npm run dev
   ```

4. Open the browser and navigate to:
   ```
   http://localhost:5173
   ```
   This will display the Bank Account UI.
   ![Bank Account UI](<images/bank-account-ui.png>)

## Running Tests

To run the tests in this project, follow these steps:

### Backend Tests

1. Open a terminal and navigate to the API directory.
   ```sh
   cd bank-account-api-py
   ```
2. Run the following command to execute all tests:
   ```sh
   python3 -m pytest
   ```
3. Run the following command to execute the unit tests only:
   ```sh
   python3 -m pytest tests/unit
   ```
4. Run the following command to execute the end-to-end tests only:
   ```sh
   python3 -m  pytest tests/e2e
   ```
5. Run tests with coverage:
   ```sh
   python3 -m pytest --cov=app --cov-report=html
   ```

### Frontend Tests

1. Make sure the API is running:
   ```sh
   cd bank-account-api-py
   uvicorn app.main:app --reload --port 3000
   ```

2. In a separate terminal, start the UI application:
   ```sh
   cd bank-account-ui
   npm run dev
   ```

3. Open a new terminal and run the UI tests:
   ```sh
   cd bank-account-ui
   npm run test:ui
   ```

   This will run Selenium-based tests that verify the UI components and functionality. The tests require both the API and UI to be running as they test the integration between them.

### Troubleshooting 

#### ChromeDriver Version Mismatch

If you encounter a `SessionNotCreatedError` when running the UI tests (`npm run test:ui`) with an error message similar to:
```
SessionNotCreatedError: session not created: This version of ChromeDriver only supports Chrome version X
Current browser version is Y...
```
Update the `chromedriver` npm package to align with your currently installed Chrome browser version:

```bash
npm uninstall chromedriver
npm install --save-dev chromedriver@latest
```

Then remove `node_modules` and `package-lock.json` and reinstall all dependencies:
```bash
rm -rf node_modules package-lock.json
npm install
```

After completing these steps, try running the UI tests again: `npm run test:ui`.

## Dependencies

### Backend Dependencies
- `fastapi`: Modern, fast web framework for building APIs with Python.
- `uvicorn`: ASGI server implementation for Python.
- `pytest`: Testing framework for Python applications.
- `pytest-cov`: Code coverage plugin for pytest.
- `pytest-asyncio`: Plugin for testing asyncio code with pytest.
- `httpx`: HTTP client library for Python, used for testing.
- `black`: Code formatter for Python.
- `flake8`: Linting tool for Python code.
- `mypy`: Static type checker for Python.

To install backend dependencies:
```sh
cd bank-account-api-py
pip3 install -r requirements.txt
# Or using Poetry (recommended)
poetry install
```

### Frontend Dependencies
- `react`: Declarative JavaScript library for building user interfaces.
- `react-dom`: React package for working with the DOM.
- `axios`: Promise-based HTTP client for API calls.
- `@mui/material`: Material-UI component library.
- `typescript`: Strongly-typed JavaScript for maintainable code.
- `vite`: Fast build tool and development server.
- `mocha`: Test framework for UI tests.
- `selenium-webdriver`: Browser automation for end-to-end testing.
- `chromedriver`: Chrome browser driver for Selenium tests.

To install frontend dependencies:
```sh
cd bank-account-ui
npm install
```

## Technologies Used

### Backend
- Python 3.9+
- FastAPI
- Uvicorn (ASGI server)
- pytest (for unit and E2E testing)
- pytest-cov (for code coverage)
- httpx (for HTTP testing)
- black, flake8, mypy (for code quality)

### Frontend
- React 19
- TypeScript
- Vite (build tool and dev server)
- Material-UI (MUI)
- Axios (HTTP client)
- Mocha + Selenium WebDriver (for UI testing)

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.
