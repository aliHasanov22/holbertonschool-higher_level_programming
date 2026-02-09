#!/usr/bin/python3
"""flask application for displaying products from JSON or CSV files"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    """Read JSON file and return list of products"""
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return []
def read_csv():
    """Read CSV file and return list of products"""
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for x in reader:
                x['id'] = int(x['id'])
                x['price'] = float(x['price'])
                products.append(x)
    except (FileNotFoundError, ValueError, KeyError):
        return []
    return products
@app.route('/products')
def products():
    """Display list of products"""
    source = request.args.get('source','').lower()
    product_ids = request.args.get('id')

    products = []
    errors = None
    filtered_products = []

    if source == 'csv':
        products = read_csv()
    elif source == 'json':
        products = read_json()
    else:
        errors = "Wrong source"
        return render_template('product_display.html', source=source, products=[],errors=errors)

    if product_ids:
        try:
            product_ids = int(product_ids)
            for product in products:
                if product.get('id') == product_ids:
                    filtered_products = [product]
                    break
            if not filtered_products:
                errors = "Wrong product id"
        except ValueError:
            errors = "Wrong product id"
    else:
        filtered_products = products

    return render_template('product_display.html', source=source, products=filtered_products,errors=errors)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
