import random
import hangmanstages

word_list = ["mercury", "baboon", "camel", "science", "picture"]
chosen_word = random.choice(word_list)
#print(chosen_word)
stage = hangmanstages.stage

guess_word = []
for letter in chosen_word:
  guess_word += "_"
print(guess_word)

game_over = False
life_counter = 6  #Go for a max of 6 lives. so until this var = 6
# print(stage[slice(1)]) slice starts from 1, where it picks from index 0

while (game_over is False):
  guess_variable = input("Enter your guess letter\n")

  if (guess_variable in guess_word):
    print(
        "Letter you have entered is already guessed. Retry with a new letter\n"
    )
  elif (chosen_word.find(guess_variable) == -1):
    print("Your letter is not there in the word\n")
    print(stage[life_counter])
    life_counter -= 1

  else:
    counter = 0
    for i in chosen_word:
      if (i == guess_variable):
        #print("yes")
        guess_word[counter] = i
      counter += 1
  print(f"\n   Guess Word Progress: {' '.join(guess_word)}\n")
  print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")

  if ("_" not in guess_word):
    print("Game Over! You Win!!")
    game_over = True
  elif (life_counter < 0):
    print("Game Over! You Lose!!")
    game_over = True
