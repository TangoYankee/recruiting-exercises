## Assumptions:
1) List of warehouses is sorted based on cost, in ascending order (least to most expensive)
2) It is preferable to ship from only one warehouse, even if some inventory exists in a less
expensive warehouse. 
  - Example) 
    - cheap warehouse has 2 of an item. expensive warehouse has 5.
    - order calls for 4 items
    - solution is to ship all from the expensive warehouse
3) Orders will be split when there is not enough inventory in a single warehouse to fufill an order.
   - Assume that is best to get all of the items from the less expensive warehouse before moving on to the next warehouse

## Strategy:
1) Iterate through the sorted list of warehouses
2) Use the map of each warehouse to fill as much of the order as possible
- Track how many of the items still need to be retrieved
3) If the order is filled, stop searching for that item
4) If the order is not filled, check the next warehouse
5) If the next warehouse can fill the whole order, allocate all of the fulfillment to that warehouse/remove other warehouses
   - If it can fill only part of it, fill that part
6) Once all of the orders are filled, exit the iteration

## Language
- Python v3.6.9

## Virtual Environment with Bash
 sudo apt-get update
 sudo apt-get install python3-venv

### Create environment
 python3 -m venv inv-all-env

### Enter environment
 source inv-all-env/bin/activate

### Install requirements
pip install -r requirements.txt

### Exit environment
 deactivate

### Help
python3 -h venv

## Linting
Python black

black {source_file_or_directory}