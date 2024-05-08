import random
words = ['hello', 'another', 'world', 'geeks', 'new', 'other']
word = random.choice(words)
turns = 5
while turns >= 0:
    guess = input("Guess a word:")
    if guess == word:
        print("You Won\nThe word is {}".format(word))
        break
    else:
        print("You Lose\nTry Again ")
        turns -= 1
        print("You left with  {} chances".format(turns))