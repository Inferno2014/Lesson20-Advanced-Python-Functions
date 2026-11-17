items = {'Pencil','Eraser'}
stock = {12,0}
inventory = {item: count for item, count in zip(items,stock)}
print(inventory)