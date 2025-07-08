import random
from data import bun_names, bun_prices, ingredient_names, ingredient_prices

def random_bun_names():
    return random.choice(bun_names)

def random_bun_price():
    return random.choice(bun_prices)

def random_ingredient_names():
    return random.choice(ingredient_names)

def random_ingredient_prices():
    return random.choice(ingredient_prices)
