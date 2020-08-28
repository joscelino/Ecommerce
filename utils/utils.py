def price_formatted(val) -> str:
    return f'R$ {val:.2f}'.replace('.', ',')


def total_quantity_cart(cart):
    return sum([item['quantity'] for item in cart.values()])
