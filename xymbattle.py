import random


def xyrpg():
  enemies = ["Benji", "Raverlart", "Thor", "Bogart", "Botmon"]
  enemy = random.choice(enemies)
  enemyhp = 100
  hp = 100
  print("Welcome to Xym Battle.")
  name = input("What is your name, challenger? ")
  print(f"Hello {name}, let us begin the battle.")
  print(f"Your challenger is: {enemy}! Prepare to fight.")
  while((hp > 0) and (enemyhp > 0)):
    attack = input("What is your attack? kick or punch? ")
    enemyattack = (f"The enemy attacked you and you have {hp} hp left!")
    if attack == 'kick':
      enemyhp = enemyhp - 20
      print(f"You hit {enemy} with a kick dealing 20 damage. The enemy has {enemyhp} hp left.")
      hp = hp - random.randrange(10,20)
      print(enemyattack)
    elif attack == 'punch':
      enemyhp = enemyhp - random.randrange(10, 30)
      print(f"You punched the enemy and the enemy has {enemyhp} left!")
      hp = hp - random.randrange(10,20)
      print(enemyattack)
    else:
      hp = hp - 10
      print("Wrong move! You stumbled and took extra damage!")
      hp = hp - random.randrange(10,20)
      print(enemyattack)

  if hp > enemyhp:
    print(f"Your hp is {hp} and the enemy hp is {enemyhp}.")
    x = (f"Congratulations! The winner is {name}!")
    print(x)
  elif hp == enemyhp:
    print(f"You both have 0 hp. It is a draw.")
  else: 
    print(f"You have {hp} hp and {enemy} has {enemyhp} hp left.")
    y = (f"You are already dead.")
    print(y)
  return -1



if __name__ == "__main__":
  while True:
    if xyrpg() == -1:
      print("Thank you for playing!")
      break

