import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in
    lettersGuessed;
    False otherwise
    '''
    secretWord = set(secretWord)
    lettersGuessed = set(lettersGuessed)
    return secretWord.issubset(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    list = [word if word in lettersGuessed else '_' for word in secretWord]
    return ''.join(list)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = set(string.ascii_lowercase)
    lettersGuessed = set(lettersGuessed)
    availableLetters = alphabet.difference(lettersGuessed)
    return ''.join(sorted(availableLetters))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    count = 0
    lettersGuessed = []
    print('Welcome to the game Hangman!\n'
          'I am thinking of a word that is ' + str(len(secretWord)) +
          ' letters long\n'
          '-----------')

    while count < 8:
        if '_' not in getGuessedWord(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break

        print('You have ' + str(8 - count) + ' guesses left\n'
              'Available Letters: '
              + getAvailableLetters(lettersGuessed)
              )
        guess = input('Please guess a letter: ').lower()

        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: "
                  + getGuessedWord(secretWord, lettersGuessed) + '\n'
                  '-----------')

        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
                  + '\n' '-----------')
        else:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word: '
                  + getGuessedWord(secretWord, lettersGuessed) + '\n'
                  '-----------')
            count += 1

    if '_' in getGuessedWord(secretWord, lettersGuessed):
        print('Sorry, you ran out of guesses. The word was ' + secretWord
              + '.')


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
