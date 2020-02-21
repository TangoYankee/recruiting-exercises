"""
Test cases for various orders
"""

"""
Model warehouses for all test cases. (Holding this constant makes it easier to track changes in conditions)
"""
model_warehouses = [
  { 
  'name': 'owd', 
  'inventory': { 'apple': 1, 'banana': 4, 'oranges':10 } 
  }, 
  {
   'name': 'dm',
   'inventory': { 'apple': 7, 'banana': 2, 'oranges':0 } 
  }, 
  {
    'name': 'empty',
    'inventory': {}
  }, 
  {
    'name': 'exotic',
    'inventory': {'apple': 1, 'avocado': 4, 'banana': 6}
  }
]

"""
Only first warehouse needed
"""
order = {'apple': 1, 'banana': 2 }
warehouse_fulfillment = [
  { 
  'owd': { 'apple': 1, 'banana':2 }
  }
]

"""
First and second warehouse needed
"""
order =  {'apple': 8, 'banana': 4, 'oranges': 6}
warehouse_fulfillment = [
  { 
  'owd': { 'apple': 1, 'banana':4, 'oranges': 6 }
  }, 
  {
    'dm' : { 'apple': 7 }
  }
  ]

"""
First, second, and fourth warehouse needed
"""
order =  {'apple': 8, 'avocado': 2, 'banana': 7}
warehouse_fulfillment = [
  { 
  'owd': { 'apple': 1, 'banana':4 }
  }, 
  {
    'dm' : { 'apple': 7, 'banana': 2 }
  },
  {
    'exotic' : {'avacado': 2, 'banana': 1}
  }
  ]

"""
Only second warehouse needed
"""
order = {'apple': 7}
warehouse_fulfillment = [
  {
    'dm': { 'apple':7 }
    }
]

"""
Second and fourth warehouse needed
"""
order = {'apple': 4, 'avocado': 4}
warehouse_fulfillment = [
  {
    'dm' : {'apple': 4}
  },
  {
    'exotic': {'avocado': 4}
  }
]

"""
Flag not enough of an item 
- This diverges from the provided test case of an unfulfilled order
- My assumption is that another class/function would actually execute the order
- It would be better if this fulfillment function provided as much feedback on the best way to fulfill an order,
  and also how to act on a shortfall of an item.
- The 'order execution' function could check for the 'unfulfilled' key and respond accordingly.
"""
order = {'apple': 4, 'banana': 13}
warehouse_fulfillment = [
  {
    'owd': { 'banana': 4 }
  },
  {
    'dm': {'apple': 4, 'banana': 4}
  },
  {
    'exotic': {'banana': 6}
  }
  {
    'unfulfilled': {'banana': 1}
  }
]
