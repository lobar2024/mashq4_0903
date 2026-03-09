def sum_nested(lst):
    total = 0
    
    for sub in lst:
        for num in sub:
            total += num
            
    return total

# misol
print(sum_nested([[1,2],[3,4],[5,6]]))
