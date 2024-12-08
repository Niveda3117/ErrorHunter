'''Write a program to reverse a given list without using built-in functions'''
def reverse_list(lst):
 
    return lst[::-1]
lst=[1,2,3,4,5]
print(reverse_list(lst))
 
    start = 0
    end = len(lst)-1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    
    return lst
 
input_list = [1, 2, 3, 4, 5]
print("Original list:", input_list)

reversed_list = reverse_list(input_list)
print("Reversed list:", reversed_list)
 