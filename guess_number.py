number = 10
print("I'm thinking of a number...")
number = str(number)

while 1:
    guess = input("What number am I thinking of? ")
    
    if guess != number:
        guess = input("Sorry! Try again: ")
    
    if guess == 'q':
        print(f"The correct number was {number}")
        break
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break