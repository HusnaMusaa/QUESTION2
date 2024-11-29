import requests
import json

#API endpoint URL
api_url = 'http://localhost:5000/products'

#Data for a new product
product_data = {
    'name': 'New Product',
    'description': 'This is a new product',
    'price': 19.99
}

#Send POST request to create a product
response = requests.post(api_url, json=product_data)

if response.status_code == 201:
    print(f"Product created successfully: {response.json()}")
else:
    print(f"Error creating product: {response.text}")

# Send GET request to retrieve products
response = requests.get(api_url)

if response.status_code == 200:
    products = response.json()
    for product in products:
        print(product)
else:
    print(f"Error retrieving products: {response.text}")