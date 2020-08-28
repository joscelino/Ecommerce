import requests

headers = {'Authorization': 'Token 9072fffaf70a425a774e18ab80aa377b81a7bd65'}

""" API tests using requests library """

# GET - Variations
variations = requests.get(url='http://localhost:8000/api/v1/variations/', headers=headers)

print(variations.status_code)

# GET - Response
variations_response = variations.json()

print(type(variations_response))

print(variations_response)


# GET - Product
product = requests.get(url='http://localhost:8000/api/v1/product/', headers=headers)


print(product.status_code)

# GET - Response
product_response = product.json()

print(type(product_response))

print(product_response)



