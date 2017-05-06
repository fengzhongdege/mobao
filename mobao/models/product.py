PRODUCT = [
    {
        "id": 1,
        "name": 1,
        "image": "p1.jpg",
        "price": 1000
    },
    {
        "id": 2,
        "name": 2,
        "image": "p2.jpg",
        "price": 2000
    },
]


def get_product_all():
    return PRODUCT


def get_product_by_id(id):
    for product in PRODUCT:
        if product.get('id') == id:
            return product

    return None
