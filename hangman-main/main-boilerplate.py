from hangman_words import word_list
from hangman_art import stages, logo
import random

#choose a random word out of the list of words
random_word=random.choice(word_list)

#get the length of the word into a variable
word_length=len(random_word)

#change game-end = False and lives = 6
game_end = False
lives = 6

#print logo
print(logo)
#choose an empty list and populate it with '_' for all the chars in the word
display = []
for _ in range(word_length):
    display += "_"

#start the game by using while loop and game_end variable
while(not game_end):
    #ask for a guess and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    #if guess is in display, print a message affirming the guess already done.
    if guess in display:
        print("The letter is already guessed.")
    

    #for all the chars in chosen_word, check if it equal to guess and if it is then put that char in display list.
    for i in range(word_length):
        v = random_word[i]
        if v == guess:
            display[i] = guess

    #if guess not in chosen word then print a message stating wrong guess and deduct one life.
    if guess not in random_word:
        print("Wrong guess")
        lives -=1
        

    # if lives become 0, game_end = True and the message that you lost, the word was this {}
    if lives == 0:
        game_end=True
        print(f" You have lost. The word was {random_word}")

    #print the display string with one space between
    display_str = " ".join(display)
    print(display_str)
    #if "_" not in dsiplay, then game_end = True and message goes you win.
    if "_" not in display:
        game_end = True
        print("Wow! You have won. The word was {random_word}")

    #print stages of hangman indexed via lives
    print(stages[lives])
