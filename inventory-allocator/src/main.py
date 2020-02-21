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
  order = {'apple': 4, 'banana': 13}
  inv_allo = InventoryAllocation()
  warehouse_fulfillment = inv_allo.get_warehouse_fulfillment(order, warehouses)
  return(warehouse_fulfillment)

if __name__ == "__main__":
#   output = [
#   {
#     'owd': { 'banana': 4 }
#   },
#   {
#     'dm': {'apple': 4, 'banana': 4 }
#   },
#   {
#     'exotic': {'banana': 6}
#   },
#   {
#     'unfulfilled': {'banana': 1}
#   }
# ]
#   for item in output:
#     for key, value in item.items():
#       print(key)
#       print(value)
#     print (item)
  print (main())
  