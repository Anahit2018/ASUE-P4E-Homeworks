#SOLUTION APPROACH
# (1) sort entered elements
# (2) slice sorted list, leave only last (largest) item
# (3) slice sorted list, leave only first (smallest) item
# (4) translate largest(smallest)_num [list] with single item into an integer using 'sum' function
# (5) calculate the difference

list_of_nums = list(map(int, input("Enter integers seperated by spaces: ").split()))

list_of_nums_sorted=sorted(list_of_nums) #(1)

largest_num = list_of_nums_sorted[(len(list_of_nums_sorted)-1):] #(2)
smallest_num = list_of_nums_sorted[:1] #(3)

largest_value=sum(largest_num) #(4)
smallest_value=sum(smallest_num) #(4)

diff=largest_value - smallest_value #(5)

#print("Sorted list: {}".format(list_of_nums_sorted))
#print("Number of items: {}".format(len(list_of_nums_sorted)))
#print("Largest number: {}".format(largest_value))
#print("Smallest number: {}".format(smallest_value))
print("Difference: {}".format(diff))
