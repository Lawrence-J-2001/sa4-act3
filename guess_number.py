number = 10
print("I'm thinking of a number...")
number = str(number)

guess = input("What number am I thinking of? ")

while 1:
    if guess != number:
        if guess < number:
            guess = input("Sorry, your guess was lower than the number. Try again: ")
        else:
            guess = input("Sorry, your guess was higher than the number. Try again: ")
    
    if guess == 'q':
        print(f"The correct number was {number}")
        break
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break