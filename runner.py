import hangman
import strategy


for x in hangman.WORDS: 
    player = strategy.PerfectStrategy(hangman.Hangman(x))
    print(player.play())