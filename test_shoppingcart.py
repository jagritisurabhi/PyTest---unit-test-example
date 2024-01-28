import pytest
from shoppingcart import ShoppingCart


@pytest.fixture
def cart():
    """All setup code here, needed to run unit tests"""
    return ShoppingCart(5)


"""Scenario 1: Possible to add items to a shopping cart"""


def test_can_add_items_to_cart(cart):
    # cart = ShoppingCart(5) - REPLACED BY FIXTURE
    cart.add("apple")
    assert cart.size() == 1


"""Scenario 2: Added item is in the cart, we use method get_items() to check"""


def test_when_item_added_then_cart_contains_item(cart):
    # cart = ShoppingCart(5) - REPLACED BY FIXTURE
    cart.add("apple")
    assert "apple" in cart.get_items()


"""Scenario 3: Adding test case to test an Exception by checking around max size"""


def test_when_add_more_than_max_items_should_fail(cart):
    # cart = ShoppingCart(5) - REPLACED BY FIXTURE
    for _ in range(5):
        cart.add("apple")
        # Happy flow, saying it is possible to add 5 items since max_size is 5

    with pytest.raises(OverflowError):
        cart.add("apple")
        # Failure flow, caught error adding above threshold(max_size)


"""Scenario 4: Getting the price of items in the cart"""


def test_can_get_total_price(cart):
    # cart = ShoppingCart(5) - REPLACED BY FIXTURE
    cart.add("pineapple")
    cart.add("watermelon")

    # price_map: Mentioned in shopping cart, we define it here as a Dictionary object
    price_map = {"apple": 1.00, "orange": 1.00, "pineapple": 2.00, "watermelon": 1.95}
    assert cart.get_total_price(price_map) == 3.95
