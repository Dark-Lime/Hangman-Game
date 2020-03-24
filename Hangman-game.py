def hangman():
    hangman_combination = hangman_word_generator()

    hangman_word = hangman_combination[0]
    hangman_definition = hangman_combination[1]
    hangman_example = hangman_combination[2]

    blank_word = []
    blank = "_ "
    space = " "

    game_word = list(hangman_word)

    for word in game_word:
        if word != " ":
            blank_word.append(blank)
        elif word == " ":
            blank_word.append(space)

    blank_word_join = "".join(blank_word)
    print("An innocent man to a children of 8 is being held captive and the captors are threatening to murder him\n"
          "The only way to save him is with your knowledge of Urban Dictionary terms\n"
          "Guess one letter and press enter to see if the letter is inside the blank word(s).\nGuess wrong seven times and he dies\n"
          "Guess the correct word and he gets to go back home to his family.\nHis life is in your hands\n")

    print(blank_word_join)
    timer = []

    guesses_so_far = []

    while blank in blank_word_join:
        if len(timer) == 1:
            print('6 tries left')
        elif len(timer) == 2:
            print('5 tries left')
        elif len(timer) == 3:
            print("4 tries left")
        elif len(timer) == 4:
            print('3 tries left')
        elif len(timer) == 5:
            print('2 tries left')
        elif len(timer) == 6:
            print('1 try left. The innocent man is sweating buckets. Please do not let him die')
        elif len(timer) == 7:
            return ('He died a horrible death that you could have prevented. \nThe word(s) was ' + "\"" + hangman_word + "\"" +
                    ".\nDefinition -  " + hangman_definition +
                    "\nHere is how you would use it in a sentence " + "\"" + hangman_example + "\"")

        index = []
        x = -1
        guess = str(input("What is your letter?  ")).lower()

        if guess == "":
            print("you did not type anything")
            continue

        if guess in guesses_so_far:
            print('You guessed that already! Try again')
            print("".join(blank_word))
            continue

        guesses_so_far.append(guess)

        while True:
            if guess in game_word:
                for letter in game_word:
                    if letter == guess:
                        x = game_word.index(letter, x + 1)
                        index.append(x)

            else:
                print('That letter is not in the word(s)! Try again!')
                timer.append(0)
            break

        for i in index:
            blank_word[i] = guess

        print("".join(blank_word))

        print('These are the letters you have used: ' + str(guesses_so_far))

        if blank not in blank_word:
            return ("The word(s) is " + "\"" + ("".join(blank_word)) + "\"" + " which means " + hangman_definition +
                    "\nHere is how you would use it in a sentence " + "\"" + hangman_example + "\"" +
                    "\nCongrats you are a hero. You saved a family.")
