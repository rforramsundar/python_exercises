import random

play_bjack = False #To come out of the Blackjack game itself
card_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
end_game = False #To end the current game

def sum_calc (list_to_sum):
  """This function calculates the sum of all items in a list and returns the sum value"""
  sum_of_list = 0
  for eachitem in range(0,len(list_to_sum)):
    sum_of_list += list_to_sum[eachitem]
  return sum_of_list

def add_card_to_list (list_to_add):
  """This function adds a card to the list that is sent as input. It also checks if the card is 11 and if so: it checks if the sum of the list is > 21 after adding that 11 card. If its > 21, it adds the card as 1 and NOT as 11. Returns appended cardlist"""
  next_number = random.choice(card_list)
  if (next_number == 11):
    temp_sum = sum_calc(list_to_add)
    if (temp_sum + next_number > 21):
      next_number = 1
  list_to_add.append(next_number)
  return list_to_add

def print_final_score():
  """This function is used to print the final scores"""
  print(f"Your final hand: {player_card_list}, final score: {sum_of_player_card_list}")
  print(f"Computers final hand: {computer_card_list}, final score: {sum_of_computer_card_list}")

if(input("Do you want to play Black Jack? Type 'y' or 'n'\n") == 'y'):
  play_bjack = True

while (play_bjack):
  #Initialize the lists for both player and computer
  player_card_list = []
  computer_card_list = []
  #Add 2 cards to the player and computer
  add_card_to_list(player_card_list)
  add_card_to_list(player_card_list)
  add_card_to_list(computer_card_list)
  add_card_to_list(computer_card_list)

  #As soon as the player decides to play black jack and enters 'y', then 2 cards are added as above and its summed and shown to the player
  sum_of_player_card_list = sum_calc(player_card_list)
  sum_of_computer_card_list = sum_calc(computer_card_list)
  print(f"Your cards {player_card_list}, current score: {sum_of_player_card_list}")
  print(f"Computers' first card: {computer_card_list[0]}")

  while (not end_game):
      #Ask the user if they want to choose a card or pass.
      choose_pass = input("\nType 'y' to choose another card or 'n' to pass\n")
      if (choose_pass == 'n'): #User chooses to pass. Make end game true.
        play_bjack = False
        end_game = True

        while (sum_of_computer_card_list < 17): 
          #If computer has sum of its list < 17, keep adding cards until its sum is > 17
          add_card_to_list(computer_card_list)
          sum_of_computer_card_list = sum_calc(computer_card_list)
        #End of while (sum_of_computer_card_list < 17)

        print_final_score()

        if (sum_of_computer_card_list == sum_of_player_card_list):
          print ("Match Draw")
        elif (sum_of_computer_card_list > sum_of_player_card_list and sum_of_computer_card_list < 22):
          print ("You Lose")
        else:
          print ("You Won!!")

      # End of if (choose_pass == 'n')

      else: #User chooses to pick a new card
        add_card_to_list(player_card_list)
        # Add to computer card list only if the sum of its contents is < 17
        if (sum_of_computer_card_list < 17): 
          add_card_to_list(computer_card_list)
        # Once cards are added, get the sum and then check the winning status
        sum_of_player_card_list = sum_calc(player_card_list)
        sum_of_computer_card_list = sum_calc(computer_card_list)

        if (sum_of_player_card_list > 21):
          play_bjack = False
          end_game = True
          print_final_score()
          print("You Lose")
        else:         
          #sum_of_player_card_list = sum_calc(player_card_list)
          #sum_of_computer_card_list = sum_calc(computer_card_list)
          print(f"Your cards {player_card_list}, current score: {sum_of_player_card_list}")
          print(f"Computers' first card: {computer_card_list}")
