from string import ascii_lowercase
import random
from dataclasses import dataclass

from .vocab import load_vocab


class WordleGame:
    def __init__(self):
        self.possible_answers, self.possible_guesses = load_vocab()
        self.secret = random.choice(list(self.possible_answers))
        self.word_list = list(self.possible_answers.union(self.possible_guesses))

        self.is_solved = False
        self.guesses = []
        self.remaining_characters = list(ascii_lowercase)

    def play(self, g: str) -> bool:
        g = g.lower()
        
        if not self.validate_guess(g):
            return False

        score = [0] * 5
        if g == self.secret:
            self.is_solved = True
            score = [1] * 5
        else:
            score = self.evaluate_guess(g)

        self.guesses.append((g, score))
        return True

    def validate_guess(self, g: str) -> bool:
        return (g in self.possible_guesses) or (g in self.possible_answers)

    def evaluate_guess(self, guess) -> list[int]:
        score = [0] * 5

        for i, (a, b) in enumerate(zip(self.secret, guess)):
            if a == b:
                score[i] = 1
            elif b in self.secret:
                score[i] = 2

        return score

    def get_state(self):
        return f"Number of guesses : {self.n_guesses}, Remaining characters : {self.get_remaining_chars()}"
