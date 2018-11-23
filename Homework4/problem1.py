import random
count_wins = 0
count_loses = 0
count_switch = 0
count_iteration = 0
count_loses_by_switch = 0
count_wins_by_switch = 0

n = int(input("How many times would you like to play? "))
print("\n")
while n != count_iteration:
    x = random.randint(1, 3)  # x=contestant
    y = random.randint(1, 3)  # y=prize
    z = random.randint(1, 3)  # z=host
    while z == x or z == y:
        z = random.randint(1, 3)
    x_c = random.randint(1, 3)
    while x_c == z:
        x_c = random.randint(1, 3)

    if x_c == y:
        count_wins += 1
        count_iteration += 1
        if x_c != x:
            count_switch += 1
            count_wins_by_switch += 1
            print("Prize is behind door", y)
            print("Contestant chooses door", x)
            print("Host opens door", z)
            print("Contestant switches from door", x, "to door", x_c)
            print("Contestant Won!\n")
        else:
            print("Prize is behind door", y)
            print("Contestant chooses door", x)
            print("Host opens door", z)
            print("Contestant doesn't switch the door")
            print("Contestant Won!\n")

    if x_c != y:
        count_loses += 1
        count_iteration += 1
        if x_c == x:
            count_loses_by_switch += 1
            print("Prize is behind door", y)
            print("Contestant chooses door", x)
            print("Host opens door", z)
            print("Contestant doesn't swtich the door")
            print("Contestant Lost!\n")
        else:
            print("Prize is behind door", y)
            print("Contestant chooses door", x)
            print("Host opens door", z)
            print("Contestant switches from door", x, "to door", x_c)
            print("Contestant Lost!\n")

print("Number of iterations:", count_iteration)
print('Number of wins:', count_wins)
print("Number of loses:", count_loses)
print("Number of switches:", count_switch)
print("Number of loses due to switching:", count_loses_by_switch)
print("Number of wins due to switching:", count_wins_by_switch)
prob_of_win_by_switching = count_wins_by_switch/count_wins*100
prob_of_not_win_by_switching = 100-prob_of_win_by_switching
print("Probability of winning when switching:",
      (round((prob_of_win_by_switching), 2)), "%")
print("Probability of winning when NOT switching:",
      (round((prob_of_not_win_by_switching), 2)), "%")
