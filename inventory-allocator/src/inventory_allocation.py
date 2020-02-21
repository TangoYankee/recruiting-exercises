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
            product_source = {}
            quantity_still_needed = quantity_ordered
            for warehouse in warehouses:
                quantity_in_warehouse = warehouse['inventory'].get(product)
                if quantity_in_warehouse:
                    # This warehouse would fulfill the whole order
                    if quantity_in_warehouse >= quantity_ordered:
                        # product_source[product] = { warehouse['name']: quantity_ordered }
                        product_source = { warehouse['name']: quantity_ordered }
                        quantity_still_needed = 0
                        break
                    # There are enough products to fill the rest of the order
                    elif quantity_in_warehouse >= quantity_still_needed:
                        # product_source[product][warehouse['name']] = quantity_still_needed
                        product_source[warehouse['name']] = quantity_still_needed
                        quantity_still_needed = 0
                        break
                    # There are not enough products to fill the rest of the order
                    elif quantity_in_warehouse < quantity_still_needed:
                        quantity_still_needed -= quantity_in_warehouse
                        # product_source[product][warehouse['name']] = quantity_in_warehouse
                        product_source[warehouse['name']] = quantity_in_warehouse
            # Any unfufilled products will be noted
            if quantity_still_needed >= 1:
                product_source['unfulfilled'] = quantity_still_needed

            # Add all warehouses into a single list, without regard as to wether they are aleady in the list
            for warehouse, quantity in product_source.items():
                # next(item for item in dicts if item)
                warehouse_for_product = {warehouse : {product: quantity}}
                if warehouse_fulfillment == []:                    
                    warehouse_fulfillment.append(warehouse_for_product)
                else:
                    warehouse_in_list = False
                    for warehouse_data in warehouse_fulfillment:
                        if warehouse in warehouse_data.keys():
                            warehouse_in_list=True
                            warehouse_data[warehouse][product]=quantity
                            break
                    if not warehouse_in_list:
                        warehouse_fulfillment.append(warehouse_for_product)

        return (warehouse_fulfillment)
