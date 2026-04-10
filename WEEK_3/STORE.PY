total_catalog = {"Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"}
sold_products = {"Mouse", "Monitor"}

in_stock = total_catalog - sold_products
print("Products still in stock:", in_stock)

sold_out = total_catalog & sold_products
print("Products that have been sold out:", sold_out)