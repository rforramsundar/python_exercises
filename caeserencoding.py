import caecerart
print(caecerart.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encoder_decoder(direction, shiftnumber):
  shifted_alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  while (shiftnumber>0):
    if (direction == 'encode'):
      shifted_alphabet.insert(0,shifted_alphabet.pop())
    else:
      shifted_alphabet.insert(len(shifted_alphabet)-1,shifted_alphabet.pop(0))
    shiftnumber -= 1
  encoded_message = ""
  for each_char in text:
    if (each_char in shifted_alphabet):
      position = shifted_alphabet.index(each_char)
      encoded_message += alphabet[position]
    else:
      encoded_message += each_char
  print (f"Your {direction}d message is: " + encoded_message)

go_again = True
while (go_again):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  encoder_decoder(direction, shift)
  try_again =input("Type 'yes' if you want to go again, else type 'no'\n")
  if (try_again == 'yes'):
    go_again = True
  else:
    go_again = False
print("Goodbye!")
