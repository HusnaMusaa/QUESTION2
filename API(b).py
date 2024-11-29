def products_handler():
    if request.method == 'POST':
        try:
            data = request.get_json()
            name = data['name']
            description = data['description']
            price = float(data['price'])

            #Validate data

            new_product = Product(name, description, price)
            products.append(new_product)

            return jsonify(new_product), 201  # Created

        except (KeyError, ValueError):
            return jsonify({'error': 'Invalid product data'}), 400  # Bad Request

    else:
        return jsonify(products)