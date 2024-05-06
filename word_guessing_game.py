import random
words = ['hello', 'another', 'world', 'geeks', 'new', 'other']
word = random.choice(words)
guess = input("Guess a word:")
if guess == word:
    print("You Won\nThe word is {}".format(word))
else:
    print("You Lose\nThe word is {}".format(word))
