#Problem 2: Guess the number game

guess=int(input("Hi human! Guess a number I am thinking between 1 and 100\n"))
guesses = 1 #loop counter start value

import random
num = random.randint(1,101)  # as upper boundery in randint is exclusive so 101

# print(num, "- is my number") for quick visual test of validity

while guess !=num:
  if guess > num:
    print("Your guess was too high.")
    guess=int(input("Have another guess or type exit to leave the game:\n")) 
    #print(num, "- is my number")
    guesses=guesses+1
  elif guess<num:
    print("Your guess was too low.")
    guess=int(input("Have another guess or type exit to leave the game:\n"))
    #print(num, "- is my number")
    guesses = guesses+1
  elif guess==str(guess) and guess=='exit':
    break
    print("You have exited the game.")

print("CONGRATULATIONS! You guessed it in only", guesses, "tries. Thanks for playing!")

