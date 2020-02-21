"""
Control the allocation of inventory
"""
from inventory_allocation import InventoryAllocation


def main():
  warehouses = [
    { 
  'name': 'owd', 
  'inventory': { 'apple': 1, 'banana': 4, 'oranges':10 } 
  }, {
   'name': 'dm',
   'inventory': { 'apple': 7, 'banana': 2, 'oranges':0 } 
  }, {
    'name': 'empty',
    'inventory': {}
  }, {
    'name': 'exotic',
    'inventory': {'apple': 1, 'avocado': 4, 'banana': 6}
  }
]
  order = {'apple': 8, 'banana': 4, 'oranges': 6}
  inv_allo = InventoryAllocation()
  warehouse_fulfillment = inv_allo.get_warehouse_fulfillment(order, warehouses)
  return(warehouse_fulfillment)

if __name__ == "__main__":
  print (main())
  