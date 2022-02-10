import random
input_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"));
computer_result = random.randint(0,2);
print(f"You chose:")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
if input_value == 0:
    print(rock);
elif input_value == 1:
    print(paper);
elif input_value == 2:
    print(scissors);
if computer_result == 0:
    print(f"Computer chose {rock}.");
elif computer_result == 1:
    print(f"Computer chose {paper}.");
elif computer_result == 2:
    print(f"Computer chose {scissors}.")
if input_value == computer_result:
    print("It's a draw!");
if input_value == 0 and computer_result == 1:
    print("You lose, Computer wins!");
elif input_value == 0 and computer_result == 2:
    print("You win, Computer loses!")
if input_value == 1 and computer_result == 2:
    print("You lose, Computer wins!");
elif input_value == 1 and computer_result == 0:
    print("You win, Computer loses!")
if input_value == 2 and computer_result == 0:
    print("You lose, Computer wins!");
if input_value == 2 and computer_result == 1:
    print("You win, Computer loses!");