import pytest

@pytest.mark.parametrize(
    "product",
    [
        {"name": "Phone", "price": 500, "stock": 3},
        {"name": "Laptop", "price": 1500, "stock": 0},
        {"name": "Mouse", "price": 50, "stock": 10}
    ]
)

def test_product_price(product):
    assert product["price"] > 0

def test_product_stock(product):
   assert product["stock"] >= 0

def test_product_name(product):
    assert product["name"] is not None
    assert product["name"] != ""




#def test_product_price(product):
 #   assert product["price"] > 0
#def test_product_in_stock(product):
  #  assert product["stock"] > 0

