import pytest
from app.bank_account.model import BankAccount


class TestBankAccountModel:
    @pytest.fixture
    def account(self):
        return BankAccount(1, "123456", "John Doe", 1000)

    def test_deposit_money_correctly(self, account):
        account.deposit(500, "ATM Credit")
        assert account.balance == 1500

    def test_deposit_with_wrong_transaction_type(self, account):
        with pytest.raises(ValueError, match="Transaction type must be Credit."):
            account.deposit(500, "ATM Debit")

    def test_withdraw_money_correctly(self, account):
        account.withdraw(500, "ATM Debit")
        assert account.balance == 500

    def test_withdraw_more_than_balance(self, account):
        with pytest.raises(ValueError, match="Insufficient funds."):
            account.withdraw(2000, "ATM Debit")

    def test_transfer_money_correctly(self, account):
        another_account = BankAccount(2, "654321", "Jane Doe", 500)
        account.transfer(another_account, 300)
        assert account.balance == 700
        assert another_account.balance == 800

    def test_to_dict(self, account):
        result = account.to_dict()
        assert result == {
            "id": 1,
            "accountNumber": "123456",
            "accountHolderName": "John Doe",
            "balance": 1000,
        }

    def test_from_dict(self):
        data = {
            "id": 1,
            "accountNumber": "123456",
            "accountHolderName": "John Doe",
            "balance": 1000,
        }
        account = BankAccount.from_dict(data)
        assert account.id == 1
        assert account.account_number == "123456"
        assert account.account_holder_name == "John Doe"
        assert account.balance == 1000
