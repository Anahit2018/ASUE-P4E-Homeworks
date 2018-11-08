import random

number= random.randint(1, 101)
guess=0
count=0

while guess !=number and guess != "exit":
  guess=input("Guess a number or type exit to leave:\n")
  
  if guess=="exit":
    break

  guess=int(guess)
  count +=1

  if guess<number:
    print("You guessed too low")
  elif guess>number:
    print("You guessed too high")
  else:
    print("Congratulations! You got it! And it only took you", count, "tries!")
