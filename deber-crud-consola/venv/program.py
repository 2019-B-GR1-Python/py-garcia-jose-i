print("INutil")
search_product("ddd")


def search_product(product_name):
    list_companies = read_file(".index")

    for company in list_companies:
        products_list = read_file(company)
        print(products_list)
        for product in products_list:
            product_attributes = product.split()
            try:
                return company, product_attributes.index(product_name.strip())

            except ValueError:
                pass

    return False