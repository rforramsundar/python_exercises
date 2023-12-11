import higherlower_gamedata
import higherlower_art
import random

#Initialize and get the data list
game_data = []
game_data = higherlower_gamedata.data
current_score = 0
first_question = True
end_game = False
compare_a = {}
compare_b = {}

# First print the art logo
print(higherlower_art.logo1)

#Get the random choice for A and B. If A and B are the same value, get a new random value for B.


def get_random_choice():
  global first_question
  global compare_a
  global compare_b
  if (first_question):
    compare_a = random.choice(game_data)
    first_question = False
  else:
    compare_a = compare_b
  compare_b = random.choice(game_data)
  while (compare_a == compare_b):
    compare_b = random.choice(game_data)
  # print(compare_a)
  return [compare_a, compare_b]


def print_compare():
  print(
      f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}"
  )

  print(higherlower_art.logo2)

  print(
      f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}"
  )


while (not end_game):
  get_random_choice()
  print_compare()
  user_input = input("\nWho has more followers? Type 'A' or 'B':")
  if ((user_input == 'A'
       and compare_a['follower_count'] > compare_b['follower_count'])
      or (user_input == 'B'
          and compare_a['follower_count'] < compare_b['follower_count'])):
    current_score += 1
    print(f"\n You are right! Current Score: {current_score}")
  else:
    print(f"Sorry that's wrong. Final Score: {current_score}")
    end_game = True
