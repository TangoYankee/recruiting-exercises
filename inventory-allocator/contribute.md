## Assumptions:
1) List of warehouses is sorted based on cost, in ascending order (least to most expensive)
2) It is preferable to ship from only one warehouse, even if some inventory exists in a less
expensive warehouse. 
  - Example) 
    - cheap warehouse has 2 of an item. expensive warehouse has 5.
    - order calls for 4 items
    - solution is to ship all from the expensive warehouse
3) Orders will be split when there is not enough inventory in a single warehouse to fufill an order.
   - Assume that it is best to get all of the items from the less expensive warehouse before moving on to the next warehouse
4) No data structures are corrupted (ie. missing expected keys)

## Strategy:
1) For each product, iterate through the sorted list of warehouses
2) Use the map of each warehouse to fill as much of the order as possible
- Track how many of the items still need to be retrieved
3) If the order is filled, stop searching for that item
4) If the order is not filled, check the next warehouse
5) If the next warehouse can fill the whole order, allocate all of the fulfillment to that warehouse/remove other warehouses
   - If it can fill only part of it, fill that part
6) Once all of the orders are filled, exit the iteration
7) If not all orders can be fulfilled, return as many as possible and flag 'unfulfilled'
   - Diverges from example but provides more information to system

## Language
- Python v3.6.9

## Code direcorty
`inventory-allocator/src`

## Virtual Environment with Bash
 `sudo apt-get update`
 `sudo apt-get install python3-venv`

### Create environment
 `python3 -m venv inv-all-env`

### Enter environment
 `source inv-all-env/bin/activate`

### Install requirements
`pip install -r requirements.txt`  
*current requirements are 'black' for linting. No other need to install requirements*

### Exit environment
 `deactivate`

### Help
`python3 -h venv`

## Linting
Python black

`black {source_file_or_directory}`

## Testing
`python3 -m unittest test`

# Running
A case is already loaded into the main function.  
View results by executing `python3 main.py`  
*ensure you are in inventory-allocator/src*
