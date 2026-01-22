from flask import Blueprint

import controllers

product = Blueprint('product', __name__)

@product.route('/product', methods=['POST'])
def add_product_route():
    return controllers.add_product()

@product.route('/product/<product_id>', methods=['GET'])
def get_product_by_id_route(product_id):
    return controllers.get_product_by_id(product_id)

@product.route('/products', methods=['GET'])
def get_all_products_route():
    return controllers.get_all_products()

@product.route('/products/active', methods=['GET'])
def products_active_true():
    return controllers.products_active_true()
    

@product.route('/product/<product_id>', methods=['PUT', 'POST'])
def update_product_by_id_route(product_id):
    return controllers.update_product_by_id(product_id)

@product.route('/product/active/<product_id>', methods=['PATCH'])
def update_active_by_id(product_id):
    return controllers.update_active_by_id(product_id)

@product.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_by_id(product_id):
    return controllers.delete_by_id(product_id)