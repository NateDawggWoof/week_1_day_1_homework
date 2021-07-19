# Guess my number, a 2 player game.

p1_number = "one"

while type(p1_number) == str:
    try:
        p1_number = int(input("Player 1 please type your secret number with digits. "))
    except:
        print("Please use digits only")
 
    


p1_number = int(p1_number)
p2_guess = 0
lives = 5
while p2_guess != p1_number:
    if lives == 0:
        print("Player 2 has 0 lives left, Player 2 you lose. \n Player 1 is the winner!")
        break
    else:
        p2_guess = int(input("Player 2 what is your guess? "))
        if p2_guess == p1_number and lives > 0:
            print("correct answer, you have won Player 2!")
        elif p2_guess < p1_number and lives > 0:
            lives = lives - 1
            print(f"Guess higher, you have {lives} lives left")
        else:
            lives = lives - 1
            print(f"Guess lower, you have {lives} lives left")
