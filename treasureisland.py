# ------------- TREASURE ISLAND GAME -------------------

print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")
direction = input("You are at cross roads. Want to go 'left' or 'right'?\n")

if (direction.lower() != 'left'):
  print("Fall into a hole!! GAME OVER")
else:
  wait_or_swim = input(
      "You've come to a lake & there is an island in the middle of the lake. Do you want to 'swim' or 'wait' for the boat?\n"
  )
  if (wait_or_swim.lower() != 'wait'):
    print("Attacked by trout!! GAME OVER")
  else:
    door_colour = input(
        "You've arrived at the island unharmed! You see 3 doors in a house. One 'red', one 'yellow' and one 'blue'. Which colour do you choose?\n"
    )
    if (door_colour.lower() == 'blue'):
      print("Eaten by beasts!! GAME OVER")
    elif (door_colour.lower() != 'yellow'):
      print("GAME OVER")
    else:
      print("YOU WON!!!!!!!!!!!!!!!!")
