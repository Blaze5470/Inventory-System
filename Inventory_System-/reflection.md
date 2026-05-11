# Reflection

## What part of the project was hardest?
I struggled most with figuring out how to split the code across several files without breaking the connections between them. At the start, deciding which functions belonged in which script felt like a puzzle. I had to separate the menu logic, business rules, and reporting functions to keep the whole thing readable and organized. On top of that, getting class objects to save and load correctly using JSON was much trickier than I expected.

## What bug took the longest to solve?
One bug that really slowed me down involved purchase orders being "received" multiple times. Every time I ran the command, the inventory counts would jump, even if that specific order was already finished. It made the stock numbers a total mess. I eventually solved it by building in a status check; now, the system looks at the order first to prevent any duplicate inventory updates from happening.

## How did you organize your code across multiple files?
I decided to break the project down by responsibility to keep the code clean. The main.py script handles the menus and the general program flow. I put the Product, Vendor, and PurchaseOrder classes into models.py. Most of the heavy lifting—like adding items, searching, and handling shipments—happens in inventory_manager.py. Meanwhile, file_manager.py takes care of the JSON saving, and reports.py is dedicated to generating stock and low-inventory summaries.

## How does your save/load system work?
To make the data stick around after the program closes, I built a save system using JSON files. When saving, I use a to_dict method to turn every object into a dictionary. Then, when the app boots back up, it reads those files and uses from_dict methods to rebuild the original Product, Vendor, and PurchaseOrder objects. That’s how the program remembers everything even after you exit the terminal.

## What would you improve if you had another week?
If I had seven more days, I’d focus on making the interface look better. I really wanted to build formatted tables for the inventory screens and reports. I also think it would be cool to track vendor performance and let users export reports directly to text files. Finally, I’d probably look into adding basic security, like a login screen or password protection for the admin features.
