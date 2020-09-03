def price_formatted(val) -> str:
    return f'R$ {val:.2f}'.replace('.', ',')


def total_quantity_cart(cart):
    return sum([item['quantity'] for item in cart.values()])


def cart_total(cart):
    return sum(
        [
            item.get('quantitative_promotional_price')
            if item.get('quantitative_promotional_price')
            else item.get('quantitative_price')
            for item in cart.values()
        ]
    )
