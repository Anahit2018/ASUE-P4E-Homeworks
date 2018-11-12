list_of_nums = list(map(int, input("Enter integers seperated by spaces: ").split()))

def find_max(list_of_nums):
    maximum=0
    for number in list_of_nums:
        if number>maximum:
            maximum=number
    return maximum
#print(find_max(list_of_nums))


def find_min(list_of_nums):
    minimum=float('inf') #denotion of infinatly big number
    for number in list_of_nums:
        if number<minimum:
           minimum=number
    return minimum

#print(find_min(list_of_nums))

diff=find_max(list_of_nums)-find_min(list_of_nums)

print((find_max(list_of_nums)), '-', (find_min(list_of_nums)),'=',diff)

