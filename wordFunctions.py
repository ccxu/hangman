import random

def getWord():
    word = ["cat", "dog", "raccoon", "ferret", "pig", "hamster", "bird", "dragon", "pheonix", "rabbit", "iguana",
            "beaver", "whale", "dolphin", "shark", "crocodile", "alligator", "squirrel", "hippotamus", "lizard", 
            "gopher", "hedgehog", "echindna", "wolf", "fox", "chameleon", "lion", "tiger", "falcon", "pizza", 
            "chocolate", "carrots", "bread", "hummus", "pasta", "spaghetti", "steak", "bacon", "biscuit", "pie",
            "cookies", "cake", "pancakes", "salad", "milk", "oranges", "apples", "meatballs", "nuts", "chicken", 
            "lamb", "fruit", "fudge", "brownies", "celery", "lollipop", "strawberries", "blackberries", "cherries"]   
    return random.choice(word)

def createBlank(word): #creates the blanks to show the player based on the length of the word, returns the blank
    blank = ""
    for let in word:
        blank += '_'
    return blank

def getTurnNeed(word): #gets the unique occurence of a letter, returns the length of the array
    letInWord = []     #NOTE: for example, raccoon has a turns needed of 5 since c and o occur twice
    for let in word:
        if let not in letInWord:
            letInWord.append(let)
    return len(letInWord)

def printBlank(blank): #prints those blanks with spaces so that the user can see the number of spaces
    showWord = ""
    for let in blank:
        showWord += (let + ' ')
    return showWord

def updateBlank(guess, word, blank): #when the player guesses a correct letter, the blanks are updated, returns the updated blank
    newBlank = ""
    for pos in range(0, len(word)): #NOTE: since word and blank are the same length, either or would word for this for loop
        if guess == word[pos]: #only replaces the blank with the letter guessed when the letter occurs in the word
            newBlank += word[pos]
        else:                  #otherwise, replace with the what is already in the blank
            newBlank += blank[pos]
    return newBlank
