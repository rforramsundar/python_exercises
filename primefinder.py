# Write your code below this line 👇


def prime_checker(number):
  upper_limit = round(number / 2)
  reminder_zero = False
  for divisor in range(2, upper_limit):
    reminder = number % divisor
    if (reminder == 0):
      print(f"divisor: {divisor}")
      reminder_zero = True
      break
  if (reminder_zero):
    print("It's not a prime number.")
  else:
    print("It's a prime number.")


# Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
