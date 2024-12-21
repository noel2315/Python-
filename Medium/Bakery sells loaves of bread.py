def bakery_pricing():
    regular_price = 185.0
    discount_rate = 0.60

    day_old_loaves = int(input("Enter the number of day-old loaves: "))

    regular_cost = day_old_loaves * regular_price
    discount = regular_cost * discount_rate
    total_price = regular_cost - discount

    print(f"\nRegular price:  ₹{regular_cost:10.2f}")
    print(f"Discount:       ₹{discount:10.2f}")
    print(f"Total price:    ₹{total_price:10.2f}")

bakery_pricing()
