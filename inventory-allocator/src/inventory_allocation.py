"""
Optimize which warehouses from which to ship ordered items.
"""


class InventoryAllocation:
    def get_warehouse_fulfillment(self, order, warehouses):
        """
        Accept a map of an order. Output a list of warehouses
        mapped with inventory to ship from them.
        """
        "product fulfilled by map"
        warehouse_fulfillment = []
        products_sources = []
        for product, quantity_ordered in order.items():
            product_source = {product: {}}
            print(product)
            print(quantity_ordered)
            for warehouse in warehouses:
                quantity_in_warehouse = warehouse['inventory'].get(product)
                if quantity_in_warehouse:
                    if quantity_in_warehouse >= quantity_ordered:
                        # Then this is the only source for this product!!!!
                        product_source[product] = {warehouse['name']: quantity_ordered }
                        break
                    elif quantity_in_warehouse < quantity_ordered: 
                        product_source[product][warehouse['name']] = quantity_in_warehouse
            products_sources.append(product_source)
            print(product_source)
        print(products_sources)



        # product_fulfilled_by_map = {}
        # unfulfilled_products = {'unfulfilled' : order}
        # warehouse_fulfillment = []
        # warehouse = warehouses[0]


        # this_warehouse_fulfillment['name'] = warehouse_name
        # this_warehouse_fulfillment[]

        # for product, quantity_unfulfilled in unfulfilled_products['unfulfilled'].items():
        #     print(product)
        #     quantity_in_warehouse = warehouse['inventory'].get(product)
        #     if (quantity_in_warehouse):
        #         ordered_quantity = order[product]
        #         # If it has enough to fulfill the order, it will be the only warehouse to fill the order
        #         if quantity_in_warehouse >= ordered_quantity:
        #             # Remember its name
        #             warehouse_name = warehouse['name']
        #             # Add it to the list of fulfilling warehouses
        #             # add the full quantity to its map

        #             # warehouse_fulfillment[warehouse_name][product] = ordered_quantity
        #             # 
        #             print(warehouse_fulfillment)
        #     else:
        #         print (False)
        # for warehouse in warehouses:
        #     print(warehouse)
        return (warehouse_fulfillment)
