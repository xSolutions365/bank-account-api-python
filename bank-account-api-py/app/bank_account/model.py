from typing import List


class BankAccount:
    def __init__(self, id: int, account_number: str, account_holder_name: str, balance: float):
        self.id = id
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount: float, transaction_type: str) -> None:
        if not transaction_type.endswith("Credit"):
            raise ValueError("Transaction type must be Credit.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float, transaction_type: str) -> None:
        if not transaction_type.endswith("Debit"):
            raise ValueError("Transaction type must be Debit.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount == self.balance:
            return
        self.balance -= amount

    def transfer(self, to_account: "BankAccount", amount: float) -> None:
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        to_account.balance += amount

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "accountNumber": self.account_number,
            "accountHolderName": self.account_holder_name,
            "balance": self.balance,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "BankAccount":
        return cls(
            id=data.get("id", 0),
            account_number=data.get("accountNumber", ""),
            account_holder_name=data.get("accountHolderName", ""),
            balance=data.get("balance", 0.0),
        )
