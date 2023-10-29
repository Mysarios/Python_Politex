def find_product(product_list, product_name):
    for i in range(0, len(product_list)):
        if (product_list[i] == product_name):
            return i
    return None


product_list = ["A", "B", "C", "D", "C", "D"]
product_name = "B"

print("Index of this product = ", find_product(product_list, product_name))
