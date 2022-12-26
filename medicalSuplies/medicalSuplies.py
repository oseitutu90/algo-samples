import csv

def read_inventory(filename):
    # Read the data from the CSV file and store it in a list of dictionaries
    inventory = []

    with open('/home/otamoabin2/algo-samples/medicalSuplies/inventory.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            inventory.append(row)
    return inventory

def add_equipment(inventory, type, manufacturer, model, serial, quantity):
    # Add a new piece of equipment to the inventory
    equipment = {
        'Type': type,
        'Manufacturer': manufacturer,
        'Model': model,
        'Serial': serial,
        'Quantity': quantity
    }
    inventory.append(equipment)
    # Write the updated inventory to the CSV file
    # take values from thre command line
    type = input("Enter the type of equipment: ")
    Manufacturer = input("Enter the manufacturer of equipment: ")
    
    
    with open('/home/otamoabin2/algo-samples/medicalSuplies/inventory.csv', 'r') as file:
        writer = csv.DictWriter(file, fieldnames=['Type', 'Manufacturer', 'Model', 'Serial', 'Quantity'])
        writer.writeheader()
        for equipment in inventory:
            writer.writerow(equipment)

def remove_equipment(inventory, serial):
    # Remove a piece of equipment from the inventory
    for i, equipment in enumerate(inventory):
        if equipment['Serial'] == serial:
            del inventory[i]
            break
    # Write the updated inventory to the CSV file
    with open('/home/otamoabin2/algo-samples/medicalSuplies/inventory.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Type', 'Manufacturer', 'Model', 'Serial', 'Quantity'])
        writer.writeheader()
        for equipment in inventory:
            writer.writerow(equipment)

def update_quantity(inventory, serial, quantity):
    # Update the quantity of a piece of equipment in the inventory
    for equipment in inventory:
        if equipment['Serial'] == serial:
            equipment['Quantity'] = quantity
            break
    # Write the updated inventory to the CSV file
    with open('inventory.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Type', 'Manufacturer', 'Model', serial, quantity])
        writer.writeheader()
        for equipment in inventory:
            writer.writerow(equipment)

def main():
    # Read the inventory from the CSV file
    inventory = read_inventory('inventory.csv')
    # Add a new piece of equipment to the inventory
    add_equipment(inventory, 'Type', 'Manufacturer', 'Model', 'Serial', 'Quantity')
    # Remove a piece of equipment from the inventory
    remove_equipment(inventory, 'Serial')
    # Update the quantity of a piece of equipment in the inventory
    update_quantity(inventory, 'Serial', 'Quantity')
    
if __name__ == '__main__':
    main()
    
    
    
            
        
