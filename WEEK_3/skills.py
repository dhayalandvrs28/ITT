required_skills = {"Python", "SQL", "Machine Learning", "Communication"}
applicant_skills = {"SQL", "Communication"}
outdated_skills = "Machine Learning"

outdated_set = {outdated_skills}

missing_skills = (required_skills - applicant_skills) - outdated_set

print("Missing required skills (excluding outdated):", missing_skills)
[24bcs167@mepcolinux WEEK_3]$cat  store.py
total_catalog = {"Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"}
sold_products = {"Mouse", "Monitor"}

in_stock = total_catalog - sold_products
print("Products still in stock:", in_stock)

sold_out = total_catalog & sold_products
print("Products that have been sold out:", sold_out)