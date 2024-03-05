# 1
from random import randrange
from json import load

file_json = "products.json"

with open(file_json, "r") as file:
    products = load(file)


# 2
products_lenght = len(products)
product_index = randrange(0, products_lenght)
ordered_product = products[product_index]

# 3
formatted_product = f"name={ordered_product['name']};discount={ordered_product['discount']};price={ordered_product['price']};quantity={ordered_product['quantity']}"

# 4
split_properties = formatted_product.split(";")
product_name_key = split_properties[0].split("=")[0]
product_name_value = split_properties[0].split("=")[1]
product_discount_key = split_properties[1].split("=")[0]
product_discount_value = split_properties[1].split("=")[1]
product_price_key = split_properties[2].split("=")[0]
product_price_value = split_properties[2].split("=")[1]
product_quantity_key = split_properties[3].split("=")[0]
product_quantity_value = split_properties[3].split("=")[1]


recreated_product = {
    product_name_key: product_name_value,
    product_discount_key: product_discount_value,
    product_price_key: product_price_value,
    product_quantity_key: product_quantity_value
}

# 5

product_discount = int(
    product_discount_value) / 100 * int(product_price_value)
product_price_with_discount = int(
    product_price_value) - int(product_discount)

# 6
total_price_with_discount = product_price_with_discount * \
    int(product_quantity_value)

# 7

print("--- Tu Factura ---")
print(f"Producto: {recreated_product['name']}")
print(f"Descuento: {recreated_product['discount']} %")
print(f"Precio Original: {recreated_product['price']}")
print(f"Precio Con Descuento: {product_price_with_discount}")

# 8

recreated_product["quantity"] -= 1
if recreated_product["quantity"] == 0:
    products.pop(product_index)
