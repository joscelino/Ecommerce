import requests
import jsonpath

headers = {'Authorization': 'Token d088fbb38dfcfeb35e737227f5523ea33a48971f'}

""" API tests using jsonpath library """

# GET - Variations
variations = requests.get(url='http://localhost:8000/api/v1/variations/', headers=headers)

variations_result = jsonpath.jsonpath(variations.json(), 'results')
print(variations_result)

# GET - Product
product = requests.get(url='http://localhost:8000/api/v1/product/', headers=headers)

product_result = jsonpath.jsonpath(product.json(), 'results')
print(product_result)

products = jsonpath.jsonpath(product.json(), 'results[*].name')
print(products)