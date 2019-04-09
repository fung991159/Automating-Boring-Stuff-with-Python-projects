# 'Practice Projects - FANTASY GAME INVENTORY'

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print (str(v) + " " + k)
    print("Total number of items: " + str(item_total))

# displayInventory(stuff)

# 'List to Dictionary Function for Fantasy Game Inventory'
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inv[item] += 1   
        else:
            inv.setdefault(item,1)
    
addToInventory(inv, dragonLoot)
displayInventory(inv)