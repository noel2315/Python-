def sum_of_nth_row(n):
    return 2 ** n

n = int(input("Enter the row number n: "))

print("Sum of elements in the", n, "th row of Pascal's Triangle is:", sum_of_nth_row(n))
