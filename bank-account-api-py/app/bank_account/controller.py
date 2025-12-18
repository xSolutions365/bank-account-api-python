from typing import List
from fastapi import APIRouter, HTTPException, Response, status
from .service import BankAccountService
from .model import BankAccount

router = APIRouter(prefix="/api/BankAccount", tags=["BankAccount"])


@router.get("", response_model=List[dict])
def get_all_accounts():
    accounts = BankAccountService.get_all_accounts()
    return [account.to_dict() for account in accounts]


@router.get("/{id}", response_model=dict)
def get_account_by_id(id: int):
    account = BankAccountService.get_account_by_id(id)
    return account.to_dict()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_account(account: dict):
    bank_account = BankAccount.from_dict(account)
    BankAccountService.create_account(bank_account)
    return None


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def update_account(id: int, account: dict):
    bank_account = BankAccount.from_dict(account)
    if id != bank_account.id:
        raise HTTPException(status_code=400, detail="Account ID mismatch")
    BankAccountService.update_account(bank_account)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_account(id: int):
    BankAccountService.delete_account(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
