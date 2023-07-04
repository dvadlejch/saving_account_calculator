from account import CurrencyConverter, Account
import pytest


@pytest.mark.parametrize(
    "currency,rate,converted_to_eur,converted_from_eur",
    [("CZK", 24.24272, 4.12, 2424.27), ("GBP", 0.88487, 113.01, 88.49)],
)
def test_currency_conversions(currency, rate, converted_to_eur, converted_from_eur):
    converter = CurrencyConverter()

    converter.add_exchange_rate(
        currency=currency,
        rate=rate,
    )

    assert converter.get_exchange_rate(currency) == rate

    assert (
        pytest.approx(converter.convert_to_eur(currency=currency, amount=100), abs=0.01)
        == converted_to_eur
    )
    assert (
        pytest.approx(
            converter.convert_from_eur(currency=currency, amount=100), abs=0.01
        )
        == converted_from_eur
    )

def test_negative_test():
    print(variable_that_doesnt_exist)
    pass

def test_account():
    RATE = 24.24272

    converter = CurrencyConverter()
    converter.add_exchange_rate(currency="CZK", rate=RATE)

    account = Account("test account", "CZK", 0.0, converter)

    account.deposit(100)
    account.deposit_in_eur(100)

    assert pytest.approx(account.get_balance(), abs=0.01) == 100 + 100 * RATE
    assert pytest.approx(account.get_balance_in_eur(), abs=0.01) == 100 / RATE + 100

    account.withdraw(100)
    account.withdraw_in_eur(100)

    assert pytest.approx(account.get_balance(), abs=0.01) == 0
    assert pytest.approx(account.get_balance_in_eur(), abs=0.01) == 0

    account.add_transaction(date="01.02.2023", description="test", amount=500)
    assert account.get_balance() == 500
