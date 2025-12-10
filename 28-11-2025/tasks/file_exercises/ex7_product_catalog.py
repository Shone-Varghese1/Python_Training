# 7. Product Catalog Formatter
# Read a text file products.txt with product names and prices.
# Generate a formatted catalog file catalog.txt with alignment.
# Example format:
# Product Price
# Laptop 55000
# Mouse 800

# def catalog_writer(product1,price1):
#     with open("./textfiles/product_catalog.txt","w") as f:
#         str1=" product   "
with open("./textfiles/product_catalog.txt","a") as f:
    f.write("  Product                 price\n")

with open("./textfiles/products.txt",'r') as f:
    for line in f:
        product1,price1=line.split()
        with open("./textfiles/product_catalog.txt", "a") as f:
            f.write(f"  {product1:<10}               {price1:<6}\n")




