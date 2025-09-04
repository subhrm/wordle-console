from string import ascii_lowercase
import random

from .vocab import load_vocab


class WordleGame:
    def __init__(self):
        self.possible_answers, self.possible_guesses = load_vocab()
        self.secret = random.choice(list(self.possible_answers))

        self.is_solved = False
        self.guesses = []
        self.remaining_characters = list(ascii_lowercase)

    def play(self, guess: str) -> bool:
        guess = guess.lower()

        if (guess not in self.possible_guesses) and (guess not in self.possible_answers):
            return False

        score = [0] * 5
        if guess == self.secret:
            self.is_solved = True
            score = [1] * 5
        else:
            for i, (a, b) in enumerate(zip(self.secret, guess)):
                if a == b:
                    score[i] = 1
                elif b in self.secret:
                    score[i] = 2
        self.guesses.append((guess, score))
        return True
