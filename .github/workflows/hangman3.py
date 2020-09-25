givenWord = "google" # given word
rightGuesses = 0 # right guesses
wrongGuesses = 0 # wrong guesses
guessLimit = 6 # guess limit

givenArray = [] # given word array
guessedArray = [] # guessed word
guessedLetters = [] # guessed letters

# create an array with letter in the given
for letter in givenWord:
  givenArray.append(letter)
  guessedArray.append("_")

#print(givenArray)
print(guessedArray)

while(wrongGuesses < guessLimit and rightGuesses < len(givenWord)):
  guess = input("Guess a letter: ")

  if guess in guessedArray: # if already guessed, restart
    pass
  else:
    guessedLetters.append(guess)
    if guess in givenWord: 
      print("Correct!")

      for i in range(len(givenArray)):
        if guess == givenWord[i]:
          rightGuesses += 1
          guessedArray[i] = guess



    else:
      print("Wrong!")
      wrongGuesses += 1

    


    #print(givenArray)
    print(guessedArray)
    print("Guessed Letters: ", guessedLetters)
    print("Right guesses are: ", rightGuesses)
    print("Wrong guesses: ", wrongGuesses)

if wrongGuesses == guessLimit:
  print("You've lost!")
else:
  print("You win!")
