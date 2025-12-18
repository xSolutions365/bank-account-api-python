import pytest
from fastapi.testclient import TestClient
from app.main import app, populate_account_data


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_data():
    populate_account_data()
    yield


class TestBankAccountE2E:
    def test_get_all_accounts_returns_200(self, client):
        """
        Scenario 1: Retrieve all bank accounts
        Given the bank account API is running
        When I request all bank accounts
        Then I should receive a list of all accounts with a 200 OK response
        """
        response = client.get("/api/BankAccount")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_account_by_id_returns_200(self, client):
        """
        Scenario 2: Retrieve a bank account by ID
        Given the bank account API is running
        When I request a bank account by ID
        Then I should receive the account details with a 200 OK response
        """
        response = client.get("/api/BankAccount/1")
        assert response.status_code == 200
        assert "accountNumber" in response.json()

    def test_create_account_returns_201(self, client):
        """
        Scenario 3: Create a new bank account
        Given the bank account API is running
        When I create a new bank account
        Then I should receive a 201 Created response
        """
        account_data = {
            "id": 3,
            "accountNumber": "789",
            "accountHolderName": "Alice Doe",
            "balance": 3000,
        }
        response = client.post("/api/BankAccount", json=account_data)
        assert response.status_code == 201

    def test_update_account_returns_204(self, client):
        """
        Scenario 4: Update an existing bank account
        Given the bank account API is running
        When I update an existing bank account
        Then I should receive a 204 No Content response
        """
        account_data = {
            "id": 1,
            "accountNumber": "123",
            "accountHolderName": "John Doe Updated",
            "balance": 1500,
        }
        response = client.put("/api/BankAccount/1", json=account_data)
        assert response.status_code == 204

    def test_delete_account_returns_204(self, client):
        """
        Scenario 5: Delete an existing bank account
        Given the bank account API is running
        When I delete an existing bank account
        Then I should receive a 204 No Content response
        """
        response = client.delete("/api/BankAccount/1")
        assert response.status_code == 204
