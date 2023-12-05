def add(first_num, second_num):
  return (first_num + second_num)


def sub(first_num, second_num):
  return (first_num - second_num)


def mult(first_num, second_num):
  return (first_num * second_num)


def div(first_num, second_num):
  return (first_num / second_num)


calc_fn_call = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}


def calculator():
  first_number = int(input("What's the first number?\n"))
  continue_flag = True

  while (continue_flag):
    next_num = int(input("What's the next number\n"))
    operator = input("Pick an operator\n + \n - \n * \n / \n")
    fn_to_call = calc_fn_call[operator]
    final_value = fn_to_call(first_number, next_num)
    print(f"{first_number}  {operator} {next_num} = {final_value}")
    first_number = final_value
    cont_input = input(
        "Do you want to continue? Type 'y' to continue or 'n' to start a new calculation or any other letter to exit \n"
    )
    if (cont_input == ('n')):
      print("Thank you!! Lets start with a new calculation \n")
      calculator()
    elif (cont_input != ('y')):
      continue_flag = False
      print("\n Thank you for using my calculator!")
      exit()

calculator()
