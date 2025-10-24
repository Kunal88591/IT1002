# Que1 swap the two elements in given list
# such that first element swapped by last element and second element swapped by second last element 

l1 = [13, 11, 3 , 27, 10, 4]

n = len(l1)

for i in range(n // 2):  
    
    temp = l1[i]
    l1[i] = l1[n - i - 1]
    l1[n - i - 1] = temp

print("swapped :", l1)