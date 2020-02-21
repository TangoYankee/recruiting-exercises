import unittest

from inventory_allocation import InventoryAllocation
from test_data import (
  model_warehouses,
  order_one,
  warehouse_fulfillment_one,
  order_two,
  warehouse_fulfillment_two,
  order_three,
  warehouse_fulfillment_three,
  order_four,
  warehouse_fulfillment_four,
  order_five,
  warehouse_fulfillment_five,
  order_six,
  warehouse_fulfillment_six
)

class TestWarehouseFulFillment(unittest.TestCase):
  inv_allo = InventoryAllocation()
  def test_one(self):
    """
    Only first warehouse needed
    """
    warehouse_fulfillment_result = self.inv_allo.get_warehouse_fulfillment(order_one, model_warehouses)
    self.assertEqual(warehouse_fulfillment_result, warehouse_fulfillment_one)

  def test_two(self):
    """
    First and second warehouse needed
    """
    warehouse_fulfillment_result = self.inv_allo.get_warehouse_fulfillment(order_two, model_warehouses)
    self.assertEqual(warehouse_fulfillment_result, warehouse_fulfillment_two)

  def test_three(self):
    """
    First, second, and fourth warehouse needed
    """
    warehouse_fulfillment_result = self.inv_allo.get_warehouse_fulfillment(order_three, model_warehouses)
    self.assertEqual(warehouse_fulfillment_result, warehouse_fulfillment_three)

  def test_four(self):
    """
    Only second warehouse needed
    """
    warehouse_fulfillment_result = self.inv_allo.get_warehouse_fulfillment(order_four, model_warehouses)
    self.assertEqual(warehouse_fulfillment_result, warehouse_fulfillment_four)

  def test_five(self):
    """
    Second and fourth warehouse needed
    """
    warehouse_fulfillment_result = self.inv_allo.get_warehouse_fulfillment(order_five, model_warehouses)
    self.assertEqual(warehouse_fulfillment_result, warehouse_fulfillment_five)

  def test_six(self):
    """
    Second and fourth warehouse needed
    """
    warehouse_fulfillment_result = self.inv_allo.get_warehouse_fulfillment(order_six, model_warehouses)
    self.assertEqual(warehouse_fulfillment_result, warehouse_fulfillment_six)

if __name__ == "__main__":
  unittest.main()
