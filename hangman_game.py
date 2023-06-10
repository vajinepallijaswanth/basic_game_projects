import random
import demo
word_list = ['apple','beautiful','potato']
lives = 6
choosen_word = random.choice(word_list)
if choosen_word == word_list[0]:
    print("It is an symbol for mobile company")
elif choosen_word == word_list[1]:
    print("This word is used to impress otheres")
elif choosen_word == word_list[2]:
    print("With this one we can make a food in that food name country namewill be there")
display = []
for i in range(len(choosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    gussed_letter = input("Guess a letter: ").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == gussed_letter:
            display[position] = gussed_letter
    print(display)
    if gussed_letter not in choosen_word:
        lives -= 1
        print("Wrong word")
        print(lives,"lives left")
        if lives == 0:
            game_over = True
            print("You loose..")

    if '_' not in display:
        game_over = True
        print("You Win...")
    #print(demo.images[lives])
