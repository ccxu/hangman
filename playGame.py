import webapp2
import cgi
import os
import jinja2
import wordFunctions

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

newGame = True
gameWord = ""
gameBlack = ""
life = 6  #life points, will decrease upon incorrect guesses
gameDone = False

class PlayGame(webapp2.RequestHandler):        
    def post(self):
        global newGame
        global usedLetter
        global gameWord
        global gameBlank
        global life
        global gameDone
        
        if newGame:
            usedLetter = []
            gameWord = wordFunctions.getWord() #getting the word rand
            gameBlank = wordFunctions.createBlank(gameWord)

        if gameDone:
            pass
        else:
            pageVar = {'blank': wordFunctions.printBlank(gameBlank)}
            page = JINJA_ENVIRONMENT.get_template('playGame.html')
            self.response.write(page.render(pageVar))
            newGame = False
        
        userInput = cgi.escape(self.request.get('letterGuess'))
        if userInput in usedLetter:
            self.response.write("\nYou already used that letter")
        elif userInput in gameWord:
            gameBlank = wordFunctions.updateBlank(userInput, gameWord, gameBlank)
        else:
            life -=1
        usedLetter.append(userInput)

        if '_' not in gameBlank:
            gameDone = True
                   
        



