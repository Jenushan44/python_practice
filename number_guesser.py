import random 

number = random.randint(1,10)

user_input = input("Guess: ")

while int(user_input) != number: 
  if int(user_input) < number: 
    print("too low") 
  else: 
    print("too high") 

  user_input = input("Guess again: ")

print("correct")