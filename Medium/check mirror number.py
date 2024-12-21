def check_mirror_number():
    number = input("Enter the number: ")
    
    reversed_number = number[::-1]
    if number == reversed_number:
        print("Yes")
    else:
        print("No")
check_mirror_number()
