from src.wallet import Wallet, BalanceInsuficiente
import pytest


@pytest.fixture
def wallet_vacio():
    return Wallet()


@pytest.fixture
def wallet():
    return Wallet(20)


def test_monto_ini_cero(wallet_vacio):
    assert wallet_vacio.balance == 0


def test_wallet_no_vacio(wallet):
    assert wallet.balance > 0


def test_wallet_gasto(wallet):
    wallet.gastar(5)
    assert wallet.balance == 15


def test_wallet_agregar(wallet):
    wallet.agregar(80)
    assert wallet.balance == 100


def test_wallet_vacio_gastar_sale_error(wallet_vacio):
    with pytest.raises(BalanceInsuficiente):
        wallet_vacio.gastar(100)
