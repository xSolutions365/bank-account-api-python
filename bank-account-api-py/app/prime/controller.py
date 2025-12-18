from fastapi import APIRouter
from .service import PrimeService

router = APIRouter(prefix="/api/prime", tags=["Prime"])


@router.get("/{number}", response_model=bool)
def is_prime(number: int):
    return PrimeService.is_prime(number)
