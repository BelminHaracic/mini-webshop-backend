from flask import Flask, jsonify, request
import json
import os
from datetime import datetime
from flask_cors import CORS
from email_utils import email_service


app = Flask(__name__)
CORS(app)

PRODUCTS_FILE = 'products.json'
ORDERS_FILE = 'orders.json'

def load_data(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    with open(filename, 'r') as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

products = load_data(PRODUCTS_FILE)
orders = load_data(ORDERS_FILE)

def get_next_id(data_list):
    if not data_list:
        return 1
    return max(item['id'] for item in data_list) + 1

# Root endpoint
@app.route('/')
def index():
    return "Mini Webshop API is running"

# --- PROIZVODI ---

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    for product in products:
        if product['id'] == id:
            return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = {
        'id': get_next_id(products),
        'name': data['name'],
        'description': data.get('description', ''),
        'price': float(data['price']),
        'image': data.get('image', ''),
        'quantity': int(data['quantity']),
        'date_added': datetime.now().isoformat()
    }
    products.append(new_product)
    save_data(PRODUCTS_FILE, products)
    return jsonify(new_product), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    for product in products:
        if product['id'] == id:
            product.update({
                'name': data.get('name', product['name']),
                'description': data.get('description', product['description']),
                'price': float(data.get('price', product['price'])),
                'image': data.get('image', product['image']),
                'quantity': int(data.get('quantity', product['quantity'])),
            })
            save_data(PRODUCTS_FILE, products)
            return jsonify({'message': 'Product updated'})
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [p for p in products if p['id'] != id]
    save_data(PRODUCTS_FILE, products)
    return jsonify({'message': 'Product deleted'})

# --- NARUDŽBE ---

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    for order in orders:
        if order['id'] == id:
            return jsonify(order)
    return jsonify({'error': 'Order not found'}), 404

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    
    # Validacija
    required_fields = ['first_name', 'last_name', 'address', 'phone']
    if not all(field in data['customer'] for field in required_fields):
        return jsonify({
            'status': 'error',
            'message': 'Nedostaju obavezni podaci o kupcu',
            'required_fields': required_fields
        }), 400
    
    new_order = {
        'id': get_next_id(orders),
        'items': data['items'],
        'created_at': datetime.now().strftime('%d.%m.%Y %H:%M'),
        'accepted_at': None,
        'customer': {
            'first_name': data['customer']['first_name'],
            'last_name': data['customer']['last_name'],
            'address': data['customer']['address'],
            'phone': data['customer']['phone'],
            'email': data['customer'].get('email', '')
        },
        'status': 'Pending'
    }
    
    orders.append(new_order)
    save_data(ORDERS_FILE, orders)

    # Pošalji email adminu
    email_service.send_order_confirmation(new_order)
    
    return jsonify({
        'status': 'success',
        'message': 'Narudžba uspješno kreirana',
        'order_id': new_order['id'],
        'order': new_order
    }), 201


@app.route('/orders/<int:id>', methods=['PUT'])
def update_order_status(id):
    data = request.json
    status = data.get('status')
    
    valid_statuses = ['Pending', 'Accepted', 'Completed', 'Rejected']
    if status not in valid_statuses:
        return jsonify({
            'status': 'error',
            'message': 'Nevažeći status narudžbe',
            'valid_statuses': valid_statuses
        }), 400
    
    for order in orders:
        if order['id'] == id:
            previous_status = order['status']
            order['status'] = status
            
            if status == 'Accepted':
                order['accepted_at'] = datetime.now().strftime('%d.%m.%Y %H:%M')
            
            save_data(ORDERS_FILE, orders)
            
            # Pošalji obavijest kupcu ako se status promijenio
            if previous_status != status:
                email_service.send_status_update(order)
            
            return jsonify({
                'status': 'success',
                'message': 'Status narudžbe ažuriran',
                'order_id': id,
                'new_status': status,
                'previous_status': previous_status
            })
    
    return jsonify({
        'status': 'error',
        'message': 'Narudžba nije pronađena'
    }), 404

import os

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


