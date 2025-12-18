import pytest
from app.prime.service import PrimeService


class TestPrimeService:
    @pytest.fixture
    def service(self):
        return PrimeService()

    def test_return_true_for_prime_numbers(self, service):
        assert service.is_prime(3) is True

    def test_return_false_for_non_prime_numbers(self, service):
        assert service.is_prime(4) is False
