from flask import jsonify, request

from db import product_records


def add_product():
   post_data = request.form if request.form else request.json

   product = {}

   product['product_id'] = post_data['product_id']
   product['product_name'] = post_data['product_name']
   product['description'] = post_data['description']
   product['price'] = post_data['price']
   product['active'] = post_data['active']

   product_records.append(product)

   return jsonify({"message" : "product added", "result" : product}), 201



def get_all_products():
    return jsonify({"message" : "products found", "results" : product_records }), 200

def products_active_true():
    active_products_list = []

    for product in product_records:
        if product['active'] == True:
            active_products_list.append(product)
    
    return jsonify({"message" : "products found", "results" : active_products_list}), 200


def get_product_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
         return jsonify({"message" : "product found", "result": product}), 200
    
    return jsonify({"message" : "product not found"}), 404


def update_product_by_id(product_id):
    post_data = request.form if request.form else request.json

    product = {}

   
    for record in product_records:
        if record['product_id'] == int(product_id):
            product = record
    
    product['product_name'] = post_data.get('product_name', product['product_name'])
    product['description'] = post_data.get('description', product['description'])
    product['price'] = post_data.get('price', product['price'])
   
    return jsonify({'message' : "product updated", "result": product }), 200

def update_active_by_id(product_id):

    product = {}

    for record in product_records:
        if record['product_id'] == int(product_id):
            product = record
    
    product['active'] = not product['active']
    return jsonify({'message' : "product updated", "result": product }), 200

def delete_by_id(product_id):

    for record in product_records:
        if record['product_id'] == int(product_id):
            product_records.remove(record)
        return jsonify({'message' : "Product deleted", "result": record }), 200
    return jsonify({"message" : "product not found"}), 404
    