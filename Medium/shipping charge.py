def calculate_shipping_charge(number_of_items):
    if number_of_items <= 0:
        return 0

    if number_of_items > 1:
        shipping_charge += (number_of_items - 1) * 200
    
    return shipping_charge

number_of_items = int(input("Enter the number of items in the order: "))

charge = calculate_shipping_charge(number_of_items)

print(f"The shipping charge is: {charge:.2f}")
