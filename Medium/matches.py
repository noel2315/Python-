def matches(str1, str2):
    min_length = min(len(str1), len(str2))

    match_count = 0
    for i in range(min_length):
        if str1[i] == str2[i]:
            match_count += 1
    
    return match_count
