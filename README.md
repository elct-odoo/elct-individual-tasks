# [elct] - [Materiales Castelar: Warehouse shouldn't receive more than ordered quantity]
[Link](url) to task

## Steps to complete the dev
- [X] Step 1: Created a new db -> personal1
- [X] Step 2: Set password and login for db
- [X] Step 3: Created a module under the inventory category named Quantity Manager
- [X] Step 4: Install the applications that I think will be necessary for this task in my fresh database
            Apps: Inventory, Purchase Dependencies: "stock", "purchase"

- [X] Step 5: Now since I have a base to work from I will try to understand the task by going through the work flow
- [X] Step 6.) What currently happens when you enter a quantity larger than the demand? This is what we need to alter.
- [X] Step 7: After doing some testing it looks like after your create a purchase order it creates a receipt through the inventory application
- [X] Step 8: Currently when you validate after making the 'Done' quantity larger than the demand it successfully validates.
- [X] Step 9: Validate Button -> Where is this? Button Validate is in Stock.Picking (Transfers) Makes sense since stock.picking is the main object for internal moves
- [X] Step 10: Overwrite this button in the stock.picking model

## Issues/Blocking Points
- [X] Issue #1

## Topics I need clarification on
- [X] Topic #1
      
## Interns who helped me
None
## Interns I helped
None
