def print_pattern(start, max_lines):
    for i in range(max_lines):
        print(f"{start + i:.1f}" * (i + 1))

start = float(input("Enter the starting number: "))
max_lines = int(input("Max number of lines printed: "))
print_pattern(start, max_lines)
