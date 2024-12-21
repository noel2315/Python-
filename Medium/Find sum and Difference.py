def find_sum_and_difference(lst, M, N):
    lst_sorted = sorted(lst)
    
    mth_max = lst_sorted[-M]
    
    nth_min = lst_sorted[N-1]
    
    total_sum = mth_max + nth_min
    difference = mth_max - nth_min
    
    return total_sum, difference

lst = [12, 3, 5, 7, 19, 2]
M = 2  
N = 3  

sum_result, difference_result = find_sum_and_difference(lst, M, N)
print("Sum:", sum_result)
print("Difference:", difference_result)
