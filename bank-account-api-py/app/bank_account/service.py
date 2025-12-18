from typing import List
from fastapi import HTTPException
from .model import BankAccount


class BankAccountService:
    _accounts: List[BankAccount] = []

    @classmethod
    def get_all_accounts(cls) -> List[BankAccount]:
        return cls._accounts

    @classmethod
    def get_account_by_id(cls, id: int) -> BankAccount:
        account = next((acc for acc in cls._accounts if acc.id == id), None)
        if not account:
            raise HTTPException(status_code=404, detail=f"Account with ID {id} not found")
        return account

    @classmethod
    def add_account(cls, account: BankAccount) -> None:
        cls._accounts.append(account)

    @classmethod
    def create_account(cls, account: BankAccount) -> None:
        account.id = len(cls._accounts) + 1
        cls._accounts.append(account)

    @classmethod
    def update_account(cls, updated_account: BankAccount) -> None:
        index = next((i for i, a in enumerate(cls._accounts) if a.id == updated_account.id), None)
        if index is None:
            raise HTTPException(
                status_code=404, detail=f"Account with ID {updated_account.id} not found"
            )
        cls._accounts[index] = updated_account

    @classmethod
    def delete_account(cls, id: int) -> None:
        try:
            index = next((i for i, a in enumerate(cls._accounts) if a.id == id), None)
            if index is None:
                raise HTTPException(status_code=404, detail=f"Account with ID {id} not found")
            cls._accounts.pop(index)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Could not delete account: {str(e)}")

    @classmethod
    def initialize_accounts(cls, accounts: List[BankAccount]) -> None:
        cls._accounts = accounts
