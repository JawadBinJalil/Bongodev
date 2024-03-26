def Guessinggame(guess):
    num=int(input("Enter a number between 1-9: "))
    if num<g:
        print("your guess is almost there")
    elif num>g:
        print("your guess is higher")
    elif num==g:
        print("Your Guess Is Correct!")

g=int(input("Guess a number between 1-9: "))
Guessinggame(g)
