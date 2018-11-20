import random
#import sys
count_wins=0
count_loses=0
count_switch=0
count_iteration=0
count_loses_by_switch=0
count_wins_by_switch=0

n=int(input("How many times would you like to play? "))

while n !=count_iteration:
  x=int(input("Pick a door: ")) # x=contestant
  y=random.randint(1,3) #y=prize
  print("Prize is behind:",y)
  #if x==y:
      #print("YOU WON!")
     # sys.exit()  # option to stop game if u guess door at once
  
  z=random.randint(1,3) #z=host
  while z==x or z==y:
    z=random.randint(1,3)
  print("Host opened:",z)
 
  print("Do you still want to open door",x,end=' ')
  x_c=int(input('or pick a different door? '))
  if x_c==y:
    count_wins +=1
    count_iteration +=1
    if x_c!=x:
      count_switch +=1
      count_wins_by_switch +=1
    print("YOU WON!!! Prize WAS behind door number",y, "\n")
  if x_c==z:
    print("Door", z, "is already open.")
  if x_c!=y:
    count_loses +=1
    count_iteration +=1
    if x_c==x:
      count_loses_by_switch +=1
    print("You lost\n")

print("Number of iterations:", count_iteration)
print('Number of wins:', count_wins)
print("Number of loses:", count_loses)
print("Number of switches:", count_switch)
print("Number of loses due to switching:", count_loses_by_switch)
print("Number of loses due to switching:", count_wins_by_switch)
prob_of_win_by_switching = count_wins_by_switch/count_wins*100
prob_of_not_win_by_switching = 100-prob_of_win_by_switching
print("Probability of winning when switching:",prob_of_win_by_switching, "%")
print("Probability of winning when NOT switching:",prob_of_not_win_by_switching,"%")
