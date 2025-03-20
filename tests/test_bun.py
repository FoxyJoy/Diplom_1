import pytest
from stellar_burgers.bun import Bun

@pytest.mark.parametrize("name, price", [("blue bun", 100),
    ("white bun", 200),
    ("green bun", 300),
])
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
    assert bun.get_name() == name