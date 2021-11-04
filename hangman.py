from pathlib import Path
from random import choice

words_str = Path('words.txt').read_text('utf-8')
LETTERS = {x for x in words_str}
LETTERS.remove('\n')
WORDS = words_str.splitlines()

class Hangman:
    def __init__(self, word: str = None):
        self.word = word or choice(WORDS)
        self.guesses = set()
        self.wrong_guesses = set()
        self.guessed_word = [None] * len(self.word)
    
    def guess(self, letter):
        if letter in self.guesses:
            return False
        self.guesses.add(letter)
        if letter in self.word:
            for i, c in enumerate(self.word):
                if c == letter:
                    self.guessed_word[i] = c
        else:
            self.wrong_guesses.add(letter)
            return False
        return True

    def guess_word(self, word):
        if word == self.word:
            self.guessed_word = list(word)
            return True
        return False