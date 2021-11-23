from abc import ABC, abstractmethod
import hangman
import random
import re

def guess_word_to_re(guess_word: list[str]) -> re.Pattern:
    """
    Converts a guess word into a regular expression.
    """
    guess_word = guess_word.copy()
    for i in range(len(guess_word)):
        if guess_word[i] is not None:
            guess_word[i] = re.escape(guess_word[i])
        else:
            guess_word[i] = '.'
    return re.compile('^' + ''.join(guess_word) + '$')

class Strategy(ABC):
    @abstractmethod
    def __init__(self, game: hangman.Hangman):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def play_round(self):
        pass

class RandomStrategy(Strategy):
    def __init__(self, game: hangman.Hangman):
        self.game = game

    def play(self):
        while not self.game.is_over():
            self.play_round()
        return (self.game.word, len(self.game.guesses), len(self.game.wrong_guesses))
        

    def play_round(self):
        self.game.guess(self.choose_random())
    
    def choose_random(self):
        return random.choice(hangman.LETTERS - self.game.wrong_guesses)

class PerfectStrategy(Strategy):
    def __init__(self, game: hangman.Hangman):
        self.game = game
        self.possible_words = [x for x in hangman.WORDS if len(x) == len(self.game.guessed_word)]
    
    def play(self):     
        letter = self.most_common_letter()
        while len(self.possible_words) > 1:
            self.game.guess(letter)
            letter = self.play_round()
        return (self.possible_words[0], len(self.game.guesses), len(self.game.wrong_guesses))

    def play_round(self):
        self.possible_words = [x for x in self.possible_words if not any(y in x for y in self.game.wrong_guesses)]        
        this_guess = guess_word_to_re(self.game.guessed_word)
        self.possible_words = [x for x in self.possible_words if this_guess.match(x)]
        return self.most_common_letter()
    
    def most_common_letter(self):
        frequencies = {x:0 for x in hangman.LETTERS}
        for x in self.possible_words:
            for y in x:
                frequencies[y] += 1
        frequencies = {k:v for k,v in frequencies.items() if k not in self.game.guesses}
        return max(frequencies, key=frequencies.get)
