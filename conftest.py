from unittest.mock import Mock
import pytest
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE
from helpers import random_bun_price, random_bun_names, random_ingredient_names, random_ingredient_prices

@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = random_bun_names()
    mock_bun.price = random_bun_price()
    return mock_bun

@pytest.fixture
def ingredient_mock():
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient.name = random_ingredient_names()
    mock_ingredient.price = random_ingredient_prices()
    return mock_ingredient

