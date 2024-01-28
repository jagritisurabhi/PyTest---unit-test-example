import pytest
from shoppingcart import ShoppingCart


# Scenario 1: Possible to add items to a shopping cart
def test_can_add_items_to_cart():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert cart.size() == 1


# Scenario 2: Added item is in the cart, we use method get_items() to check
def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()


# Scenario 3: Adding test case to test an Exception by checking around max size
def test_when_add_more_than_max_items_should_fail():
    cart = ShoppingCart(5)
    for _ in range(5):
        cart.add("apple")
        # Happy flow, saying it is possible to add 5 items since max_size is 5

    with pytest.raises(OverflowError):
        cart.add("apple")
        # Failure flow, caught error adding above threshold(max_size)


# Scenario 4: Getting the price of items in the cart
