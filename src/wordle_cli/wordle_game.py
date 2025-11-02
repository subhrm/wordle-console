from string import ascii_lowercase
import random

from .vocab import load_vocab


class WordleGame:
    def get_hints(self):
        # Start with all possible answers
        candidates = set(self.possible_answers)
        for guess, score in self.guesses:
            new_candidates = set()
            for word in candidates:
                match = True
                # Track used positions for yellow
                used_positions = set()
                # First pass: handle greens
                for i, (g_char, s) in enumerate(zip(guess, score)):
                    if s == 1:
                        if word[i] != g_char:
                            match = False
                            break
                        used_positions.add(i)
                if not match:
                    continue
                # Second pass: handle yellows and grays
                for i, (g_char, s) in enumerate(zip(guess, score)):
                    if s == 2:
                        # Must be present but not in this position
                        if g_char not in word or word[i] == g_char:
                            match = False
                            break
                    elif s == 0:
                        # Absent: must not be present anywhere unless already marked yellow/green
                        if g_char in word:
                            # But allow if the letter is green/yellow elsewhere
                            # Count how many times g_char appears in guess as yellow/green
                            required = sum(1 for idx, (gc, sc) in enumerate(zip(guess, score)) if gc == g_char and sc in (1, 2))
                            actual = word.count(g_char)
                            if actual > required:
                                match = False
                                break
                if match:
                    new_candidates.add(word)
            candidates = new_candidates
        return sorted(candidates)

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
