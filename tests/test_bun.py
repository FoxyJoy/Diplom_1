import pytest
from stellar_burgers.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("blue bun", 100),
    ("white bun", 200),
    ("green bun", 300),
])
def test_bun_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name

@pytest.mark.parametrize("name, price", [
    ("blue bun", 100),
    ("white bun", 200),
    ("green bun", 300),
])
def test_bun_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
