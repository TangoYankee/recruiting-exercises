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
One:
Only first warehouse needed
"""
order_one = {'apple': 1, 'banana': 2 }
warehouse_fulfillment_one = [
  { 
  'owd': { 'apple': 1, 'banana':2 }
  }
]

"""
Two:
First and second warehouse needed
"""
order_two =  {'apple': 8, 'banana': 4, 'oranges': 6}
warehouse_fulfillment_two = [
  { 
  'owd': { 'apple': 1, 'banana':4, 'oranges': 6 }
  }, 
  {
    'dm' : { 'apple': 7 }
  }
  ]

"""
Three:
First, second, and fourth warehouse needed
"""
order_three =  {'apple': 8, 'avocado': 2, 'banana': 7}
warehouse_fulfillment_three = [
    {
    'exotic' : {'avocado': 2, 'banana': 1}
  },
  { 
  'owd': { 'apple': 1, 'banana':4 }
  }, 
  {
    'dm' : { 'apple': 7, 'banana': 2 }
  }
  ]

"""
Four:
Only second warehouse needed
"""
order_four = {'apple': 7}
warehouse_fulfillment_four = [
  {
    'dm': { 'apple':7 }
    }
]

"""
Five:
Second and fourth warehouse needed
"""
order_five = {'apple': 4, 'avocado': 4}
warehouse_fulfillment_five = [
    {
    'exotic': {'avocado': 4}
  },
  {
    'dm' : {'apple': 4}
  }

]

"""
Six:
Flag not enough of an item 
- This diverges from the provided test case of an unfulfilled order
- My assumption is that another class/function would actually execute the order
- It would be better if this fulfillment function provided as much feedback on the best way to fulfill an order,
  and also how to act on a shortfall of an item.
- The 'order execution' function could check for the 'unfulfilled' key and respond accordingly.
"""
order_six = {'apple': 4, 'banana': 13}
warehouse_fulfillment_six = [
    {
    'dm': {'apple': 4, 'banana': 2 }
  },  {
    'exotic': {'banana': 6}
  },
  {
    'owd': { 'banana': 4 }
  },
  {
    'unfulfilled': {'banana': 1}
  }
]
