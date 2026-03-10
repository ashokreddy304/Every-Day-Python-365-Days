def reverse_list(l):
    return l,l[::-1]

l = [1,2,3,4,5,6]
original_list,reverse_list1 = reverse_list(l)
print("original list is {} and revere list is {}".format(original_list,reverse_list1))