import hangman
import strategy
f = open('out.txt', 'w', encoding='utf-8')

for x in hangman.WORDS: 
    player = strategy.RandomStrategy(hangman.Hangman(x))
    x = str(player.play())
    print(x)
    f.write(x + '\n')
    f.flush()
f.close()