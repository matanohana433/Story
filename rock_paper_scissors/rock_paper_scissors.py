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

import random

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_dec = random.randint(0, 2)
# your opportunities options:
if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)
elif choose < 0 or choose > 2:
    print("This is an invalid option try again.")

# computer decisions options:
if comp_dec == 0:
    print(f'''computer choose:\n {rock}''')
elif comp_dec == 1:
    print(f'''computer choose:\n {paper}''')
elif comp_dec == 2:
    print(f'''computer choose:\n {scissors}''')

# results opportunities:
if choose == comp_dec:
    print("it is a Draw!")
elif (choose == 1 and comp_dec == 0) or (choose == 2 and comp_dec == 1) or (choose == 0 and comp_dec == 2):
    print("You win")
else:
    print("You lose")
