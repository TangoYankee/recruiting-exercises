"""
Control the allocation of inventory
"""
from inventory_allocation import InventoryAllocation


def main():
  inv_allo = InventoryAllocation()
  warehouse_fulfillment = inv_allo.get_warehouse_fulfillment("order", "warehouses")
  return(warehouse_fulfillment)

if __name__ == "__main__":
  print (main())
  