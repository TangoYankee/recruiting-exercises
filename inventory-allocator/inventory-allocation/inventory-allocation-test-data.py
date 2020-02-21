"""
Test cases for various orders
"""

"""
Model warehouses for all test cases. (Holding this constant makes it easier to track changes in conditions)
"""
model_warehouses = [{ 
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
    'inventory': {'apple': 0, 'avocado': 4, 'banana': 6}
  }]

"""
Only first warehouse needed
"""
order_input = {'apple': 1, 'banana': 2 }
warehouse_output: [{ 
  'owd': { 'apple': 1, 'banana':2 }
  }]

"""
First and second warehouse needed
"""

"""
First, second, and third warehouse needed
"""

"""
Only second warehouse needed
"""

"""
Second and fourth warehouse needed
"""


"""
Flag not enough of an item
"""

