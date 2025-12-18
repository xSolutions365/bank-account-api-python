import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.bank_account.controller import router
from app.bank_account.service import BankAccountService
from app.bank_account.model import BankAccount
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)
client = TestClient(app)


class TestBankAccountController:
    @pytest.fixture(autouse=True)
    def setup(self):
        BankAccountService.initialize_accounts([])

    @patch.object(BankAccountService, "get_all_accounts")
    def test_return_all_bank_accounts(self, mock_get_all):
        accounts = [
            BankAccount(1, "123", "John Doe", 1000),
            BankAccount(2, "456", "Jane Doe", 2000),
        ]
        mock_get_all.return_value = accounts

        response = client.get("/api/BankAccount")

        assert response.status_code == 200
        assert len(response.json()) == 2

    @patch.object(BankAccountService, "get_account_by_id")
    def test_return_bank_account_by_id(self, mock_get_by_id):
        account = BankAccount(1, "123", "John Doe", 1000)
        mock_get_by_id.return_value = account

        response = client.get("/api/BankAccount/1")

        assert response.status_code == 200
        assert response.json()["id"] == account.id

    @patch.object(BankAccountService, "create_account")
    def test_create_new_bank_account(self, mock_create):
        account_data = {
            "id": 3,
            "accountNumber": "789",
            "accountHolderName": "Alice Doe",
            "balance": 3000,
        }

        response = client.post("/api/BankAccount", json=account_data)

        assert response.status_code == 201
        mock_create.assert_called_once()

    @patch.object(BankAccountService, "update_account")
    def test_update_existing_bank_account(self, mock_update):
        account_data = {
            "id": 1,
            "accountNumber": "123",
            "accountHolderName": "John Doe Updated",
            "balance": 1500,
        }

        response = client.put("/api/BankAccount/1", json=account_data)

        assert response.status_code == 204
        mock_update.assert_called_once()

    @patch.object(BankAccountService, "delete_account")
    def test_delete_existing_bank_account(self, mock_delete):
        response = client.delete("/api/BankAccount/1")

        assert response.status_code == 204
        mock_delete.assert_called_once_with(1)
