from main import Product, Basket
import pytest

test_sum = [([Product('Чак-чак', 1500), Product('Чэй', 50), Product('Пельмени', 250)], 1800)]
test_title = [([Product('Чак-чак', 1500)], 'Чак-чак'), ([Product('Пельмени', 250)], 'Пельмени')]
test_price = [([Product('Чак-чак', 1500)], 1500), ([Product('Пельмени', 250)], 250)]

chak = Product('Чак-чак', 1500)
chay = Product('Чэй', 50)
pelm = Product('Пельмени', 250)

add_test = [([chak, chay, pelm],
             [chak, chay], pelm)]

rem_test = [([chak, chay, pelm],
            [chak, chay], pelm)]

@pytest.mark.parametrize('products, summa', test_sum)
def test_basket(products, summa):
    basket = Basket()
    for prod in products:
        basket.add(prod)
    assert summa == basket.count_sum()


@pytest.mark.parametrize('title, price', test_title)
def test_name(title, price):
    product = Product(title, price)
    assert product.title == title


@pytest.mark.parametrize('title, price', test_price)
def test_price(title, price):
    product = Product(title, price)
    assert product.price == price

@pytest.mark.parametrize('products, products_two, products_thr', add_test)
def test_add_bask(products, products_two, products_thr):
    basket = Basket(products_two)
    basket.add(products_thr)
    assert basket.basket == products

@pytest.mark.parametrize('products, products_two, products_thr', rem_test)
def test_bask_rem(products, products_two, products_thr):
    basket = Basket(products)
    basket.remove(products_thr)
    assert basket.basket == products_two