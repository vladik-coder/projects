many_lists=[1, 2, [2, 4, [[7, 8], 4, 6]]]

def sum_list(many_lists,sum=0): 
    for i in many_lists:
        if type(i)==list:
            sum+=sum_list(i) 
        else:
            sum+=i 
    return sum


print('sum of elements', sum_list(many_lists))
