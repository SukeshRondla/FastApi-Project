import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds

class TestCalculations:
    @pytest.mark.parametrize("num1, num2, expected", [
        (3, 2, 5),
        (7, 1, 8),
        (12, 4, 16)
    ])
    def test_add(self, num1, num2, expected):
        assert add(num1, num2) == expected

    def test_subtract(self):
        assert subtract(9, 4) == 5

    def test_multiply(self):
        assert multiply(4, 3) == 12

    def test_divide(self):
        assert divide(20, 5) == 4

class TestBankAccount:
    @pytest.fixture
    def zero_bank_account(self):
        return BankAccount()

    @pytest.fixture
    def bank_account(self):
        return BankAccount(50)

    def test_bank_set_initial_amount(self, bank_account):
        assert bank_account.balance == 50

    def test_bank_default_amount(self, zero_bank_account):
        assert zero_bank_account.balance == 0

    def test_withdraw(self, bank_account):
        bank_account.withdraw(20)
        assert bank_account.balance == 30

    def test_deposit(self, bank_account):
        bank_account.deposit(30)
        assert bank_account.balance == 80

    def test_collect_interest(self, bank_account):
        bank_account.collect_interest()
        assert round(bank_account.balance, 6) == 55

    @pytest.mark.parametrize("deposited, withdrew, expected", [
        (200, 100, 100),
        (50, 10, 40),
        (1200, 200, 1000)
    ])
    def test_bank_transaction(self, zero_bank_account, deposited, withdrew, expected):
        zero_bank_account.deposit(deposited)
        zero_bank_account.withdraw(withdrew)
        assert zero_bank_account.balance == expected

    def test_insufficient_funds(self, bank_account):
        with pytest.raises(InsufficientFunds):
            bank_account.withdraw(200)
