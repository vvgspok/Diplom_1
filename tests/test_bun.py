from practicum.bun import Bun
from helpers import random_bun_price, random_bun_names
from conftest import bun_mock

class TestBun:

    def test_get_name_bun(self, bun_mock):
        bun_name = random_bun_names()
        bun_price = random_bun_price()
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    def test_get_price_bun(self):
        bun_name = random_bun_names()
        bun_price = random_bun_price()
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price
