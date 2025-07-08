from practicum.burger import Burger
from practicum.bun import Bun
from practicum.ingredient import Ingredient
from unittest.mock import Mock
from conftest import bun_mock, ingredient_mock
from helpers import random_bun_price, random_bun_names, random_ingredient_names, random_ingredient_prices
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestBurger:

    def test_get_price_burger(self, ingredient_mock, bun_mock):
        price_bun = bun_mock.get_price.return_value = random_bun_price()
        price_ingredient = ingredient_mock.get_price.return_value  = random_ingredient_prices()
        total_price  = (price_bun*2)+price_ingredient
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == total_price

    def test_set_buns_burger(self, bun_mock):
        burger = Burger()
        assert burger.set_buns(bun_mock) is None and burger.bun == bun_mock

    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        assert burger.add_ingredient(ingredient_mock) is None and burger.ingredients == [ingredient_mock]

    def test_remove_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert burger.remove_ingredient(0) is None and burger.ingredients == []

    def test_move_ingredient(self, ingredient_mock):
        ingredient_1 = ingredient_mock
        ingredient_2 = Mock()
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        before_list_ingredients = burger.ingredients.copy()
        burger.move_ingredient(0, 1)
        after_list_ingredients = burger.ingredients
        assert before_list_ingredients == list(reversed(after_list_ingredients))

    @pytest.mark.parametrize(
        'ingredient_type, ingredient ',
        [
            (INGREDIENT_TYPE_SAUCE, 'sauce'),
            (INGREDIENT_TYPE_FILLING, 'filling')
        ]
    )
    def test_get_receipt(self, bun_mock, ingredient_mock, ingredient_type, ingredient):
        name_bun = bun_mock.get_price.return_value = random_bun_names()
        price_bun = bun_mock.get_price.return_value = random_bun_price()
        name_ingredient = ingredient_mock.get_price.return_value = random_ingredient_names()
        price_ingredient = ingredient_mock.get_price.return_value = random_ingredient_prices()
        bun = Bun(name_bun, price_bun)
        ing = Ingredient(ingredient_type, name_ingredient, price_ingredient)
        total_price = (price_bun*2)+price_ingredient
        burger = Burger()
        burger.add_ingredient(ing)
        burger.set_buns(bun)

        expected_receipt = (
            f'(==== {bun.name} ====)\n'
            f'= {ingredient} {ing.name} =\n'
            f'(==== {bun.name} ====)\n\n'
            f'Price: {total_price}'
        )
        assert burger.get_receipt() == expected_receipt
