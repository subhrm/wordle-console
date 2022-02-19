from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import print_formatted_text as print
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError

from pyfiglet import Figlet
fig = Figlet(font='slant')

from .wordle_game import WordleGame
game = WordleGame(seed=2002)
wc = WordCompleter(game.possible_answers)

def bottom_toolbar():
    return game.get_state()

class GuessValidator(Validator):
    def validate(self, document):
        text = document.text.lower()

        if not game.validate_guess(text):
            raise ValidationError(message='Please enter a valid 5 letter word.',
                                  cursor_position=len(text)-1)

def cli():
    print(fig.renderText('WORDLE IN CONSOLE'))
    for i in range(6):
        guess = ""
        valid_guess = False
        guess = prompt(HTML(f"<b><style bg='blue'>Guess {i+1}: </style>Enter a 5 letter word - </b>"),
                       completer=wc,
                       validator=GuessValidator(),
                       bottom_toolbar=bottom_toolbar).lower()

        if game.check_answer(guess):
            print(fig.renderText(guess.upper()))
            print(HTML("<b><style bg='green'>Congratulations!! You have found the word !</style></b>"))
            print(fig.renderText('Winner'))
            break

        r = game.find_match(guess)
        print(f"Response : {r[0]}")
    
    if not game.is_solved:
        print(HTML("<b><style bg='red'>Sorry, you failed to solve it with 6 guesses!!</style></b>"))
        print(HTML(f"<b>The answer is : <style bg='red'>{game.secret}</style></b> "))

