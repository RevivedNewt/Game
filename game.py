def playGame():
    print("Do you want to play a game? Y/N")
    answer = input()
    if answer == "N":
        print("Maybe later.")

    else:

        def selectGame():
            print("Okay! Let's play! Which do you want to play? ")
            print("1) Mad Lib")
            print("2) Random Number Guesser")

            game = input()
            if game == str("1"):
                print("Mad Lib. You got it!")
                print('Lets start with an adjective: ')
                adjOne = input()

                print('Okay, another adjective: ')
                adjTwo = input()

                print("Let's shake it up, name a bird: ")
                birdOne = input()

                print("Name a room in your house")
                roomOne = input()

                print('Can you give me a past tense verb?: ')
                verbOne = input()

                print('Can I have a regular verb, please?: ')
                verbTwo = input()

                print("Family member's name?: ")
                familyOne = input()

                print("Name one noun")
                nounOne = input()

                print('Name a liquid, any liquid: ')
                liquidOne = input()

                print('Come up with a verb ending in ing')
                ingOne = input()

                print("Can you give me give me a plural body part?: ")
                bodyOne = input()

                print('Almost done! I need a plural noun:')
                nounTwo = input()

                print("Two more. Verb ending in ing: ")
                ingTwo = input()

                print("Last one! You made it! Can I have a noun, please?")
                nounThree = input()

                #input words into madlib
                print(f"It was a {adjOne}, cold November day. I woke up to the {adjTwo} smell of {birdOne} roasting in the {roomOne} downstairs.")
                print(f"I {verbOne} down the stairs to see if I could help {verbTwo} the dinner. My mom said, ")
                print(f'"See if {familyOne} needs a fresh {nounOne}". So I carried a tray of glasses full of {liquidOne} into the {ingOne} room.')
                print(f"When I got there, I couldn't believe my {bodyOne}! There were {nounTwo} {ingTwo} on the {nounThree}!")
                
            elif game == str("2"):
                print("Random Number Guesser? Get ready!")
                
                import random
                ranNumber = random.randint(1, 100)
                print("Can you guess the number I am thinking? :")
                #testing number, delete later
                print(ranNumber)

                def guessNumber(ranNumber):
                    guesses = 10
                    while guesses > 0:
                        guessNum = int(input("Guess: "))
                        if ranNumber > guessNum:
                            print("Too low, try again")
                            if (ranNumber - guessNum) > 0 and (ranNumber - guessNum) <= 5:
                                print("On FIRE")
                            elif (ranNumber - guessNum) > 5 and (ranNumber - guessNum) <= 10:
                                print("You're hot")
                            elif (ranNumber - guessNum) > 10 and (ranNumber - guessNum) <= 20:
                                print("Getting warmer")                            
                            else:
                                print("ice cold")
                        elif ranNumber < guessNum:
                            print("Too high, try again")
                            if (guessNum - ranNumber) > 0 and (guessNum - ranNumber) <= 5:
                                print("On FIRE")
                            elif (guessNum - ranNumber) > 5 and (guessNum - ranNumber) <= 10:
                                print("You're hot")
                            elif (guessNum - ranNumber) > 10 and (guessNum - ranNumber) <= 20:
                                print("Getting warmer")
                            else:
                                print("ice cold")
                        else:
                            print("You got it! Your score is " + str(guesses))
                        return guessNum
                    guesses -= 1
                    print("Your score is " + str(guesses))
                print("Out of guesses! Too bad. Number was: " + str(ranNumber))
            guessNumber(ranNumber)
        selectGame()
    print("Do you want to play again? Y/N: ")
    answer = input()
    if answer == "N":
        print ("Ok! It was fun playing with you!")
    else:
        selectGame()

playGame()