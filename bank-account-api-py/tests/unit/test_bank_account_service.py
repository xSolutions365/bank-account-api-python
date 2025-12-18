import pytest
from fastapi import HTTPException
from app.bank_account.service import BankAccountService
from app.bank_account.model import BankAccount


class TestBankAccountService:
    @pytest.fixture(autouse=True)
    def setup(self):
        BankAccountService.initialize_accounts([])
        yield
        BankAccountService.initialize_accounts([])

    def test_return_all_accounts(self):
        expected_accounts = [
            BankAccount(1, "123456", "John Doe", 1000),
            BankAccount(2, "654321", "Jane Doe", 2000),
        ]

        for acc in expected_accounts:
            BankAccountService.create_account(acc)

        accounts = BankAccountService.get_all_accounts()

        assert len(accounts) == len(expected_accounts)

    def test_return_bank_account_by_id(self):
        account = BankAccount(1, "123456", "John Doe", 1000)
        BankAccountService.create_account(account)

        result = BankAccountService.get_account_by_id(1)

        assert result is not None
        assert result.account_number == account.account_number

    def test_create_account(self):
        account = BankAccount(1, "123456", "John Doe", 1000)

        BankAccountService.create_account(account)
        result = BankAccountService.get_account_by_id(1)

        assert result is not None
        assert result.account_number == account.account_number

    def test_update_account(self):
        account = BankAccount(1, "123456", "John Doe", 1000)
        BankAccountService.create_account(account)
        account.balance = 1500

        BankAccountService.update_account(account)
        result = BankAccountService.get_account_by_id(1)

        assert result.balance == 1500

    def test_delete_account(self):
        account = BankAccount(1, "123456", "John Doe", 1000)
        BankAccountService.create_account(account)

        BankAccountService.delete_account(1)

        with pytest.raises(HTTPException, match="Account with ID 1 not found"):
            BankAccountService.get_account_by_id(1)

    def test_initialize_accounts_and_clear_existing(self):
        account1 = BankAccount(1, "123456", "John Doe", 1000)
        BankAccountService.create_account(account1)
        new_accounts = [BankAccount(2, "654321", "Jane Doe", 2000)]

        BankAccountService.initialize_accounts(new_accounts)

        assert len(BankAccountService.get_all_accounts()) == len(new_accounts)
