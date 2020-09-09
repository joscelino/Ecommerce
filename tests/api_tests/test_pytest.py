import requests


class ProductTest:

    headers = {'Authorization': 'Token d088fbb38dfcfeb35e737227f5523ea33a48971f'}
    url_base_products = 'http://127.0.0.1:8000/api/v1/product/'

    def test_get_products(self):
        response = requests.get(url=self.url_base_products, headers=self.headers)

        assert response.status_code == 200

    def test_get_product(self):
        response = requests.get(url=f'{self.url_base_products}5/', headers=self.headers)

        assert response.status_code == 200

    def test_post_product(self):
        new = {
            'name': 'Nintendo Switch with Neon Blue and Neon Red Joy‑Con - HAC-001(-01)',
            'short_description': 'Nintendo Switch with Neon Blue and Neon Red Joy‑Con - HAC-001(-01)',
            'long_description': '3 Play Styles: TV Mode, Tabletop Mode, Handheld Mode'
                                '6.2-inch, multi-touch capacitive touch screen \
                                4.5-9+ Hours of Battery Life *Will vary depending \
                                on software usage conditions \
                                Connects over Wi-Fi for multiplayer gaming; Up to 8 \
                                consoles can be connected for local wireless multiplayer \
                                Model number: HAC-001(-01)',
            'slug': '',
            'price': '655.99',
            'promotional_price': '645.00',
            'product_type': 'Simple',
            'active': 'True',
            'variations': '',
        }
        response = requests.get(url=self.url_base_products, headers=self.headers, data=new)
        assert response.status_code == 201
        assert response.json()['name'] == new['name']

    def test_put_product(self):
        updated = {
            'name': 'Nintendo Switch with Neon Blue and Neon Red Joy‑Con - HAC-001(-01)',
            'promotional_price': '600.00',
        }
        response = requests.get(url=f'{self.url_base_products}10/', headers=self.headers, data=updated)
        assert response.status_code == 200
        assert response.json()['name'] == updated['name'] \
               and response.json()['promotional_price'] == updated['promotional_price']

    def test_delete_product(self):
        response = requests.get(url=f'{self.url_base_products}10/', headers=self.headers)
        assert response.status_code == 204 and len(response.text) == 0

"""
Test instruction
>>> pytest pytest_test.py
"""
