list1 = [i for i in range(1,11)]
first5 = list1[:5]
reversed = sorted(first5,reverse= True)
print("Original list: {}".format(list1))
print("Extracted first five elements: {}".format(first5))
print("Reversed extracted elements: {}".format(reversed))