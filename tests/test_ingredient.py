from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from helpers import random_ingredient_prices, random_ingredient_names
import pytest

class TestIngredient:

    def test_get_name_ingredient(self):
        ingredient_name = random_ingredient_names()
        ingredient_price = random_ingredient_prices()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name

    def test_get_price_ingredient(self):
        ingredient_name = random_ingredient_names()
        ingredient_price = random_ingredient_prices()
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING
        ]
    )
    def test_get_ingredient_type(self, ingredient_type):
        ingredient_name = random_ingredient_names()
        ingredient_price = random_ingredient_prices()
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type





