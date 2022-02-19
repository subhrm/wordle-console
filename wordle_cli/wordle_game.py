from string import ascii_lowercase 
import random

class WordleGame:

    def __init__(self, seed:int=-1):

        self.__load_vocab()
        random.seed(seed)
        self.secret = random.choice(self.possible_answers) 

        self.is_solved = False
        self.choices = [] 
        self.n_guesses = 0
        self.characters = list(ascii_lowercase)

    def get_remaining_chars(self):
        return " ".join(self.characters)

    def validate_guess(self, g:str) -> bool:
        if (len(g) != 5) or (g not in self.possible_guesses):
            return False

        return True


    def check_answer(self, g:str) -> bool:
        if g == self.secret:
            self.is_solved = True
            return True

        return False

    def find_match(self, guess):
        self.n_guesses += 1
        match = list("*****")

        for i,(a,b) in enumerate(zip(self.secret, guess)):
            if a == b:
                match[i] = a

        has = set(self.secret).intersection(set(guess))
        excluding = set(guess).difference(set(self.secret))

        for c in list(excluding):
            if c in self.characters:
                self.characters.remove(c)

        return match, has, excluding 

    def __load_vocab(self):
        guesses_file = "data/wordle-allowed-guesses.txt"
        possible_answers_file = "data/wordle-answers-alphabetical.txt"

        with open(guesses_file) as fin:
            _possible_guesses = list(fin.read().split("\n"))

        with open(possible_answers_file) as fin:
            self.possible_answers = list(fin.read().split("\n"))

        _possible_guesses.extend(self.possible_answers)
        self.possible_guesses = set(_possible_guesses)

    def get_state(self):
        return f"Number of guesses : {self.n_guesses}, Remaining characters : {self.get_remaining_chars()}"
        
