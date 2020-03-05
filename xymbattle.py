import random


def xyrpg():
  enemies = ["Pandymanz", "Raverlart", "Norato", "Borger", "1 Pawnch", "Sexyboi", "Botmon", "Bubbletea"]
  enemy = random.choice(enemies)
  enemyhp = 100
  hp = 100
  print("Welcome to Xym Battle.")
  name = input("What is your name, hero? ")
  print(f"Hello {name}, let us begin the battle!")
  print(f"Your challenger is: {enemy}! Prepare to fight.")
  while((hp > 0) and (enemyhp > 0)):
    attack = input("What is your attack? kick or punch? ")
    enemyattack = (f"{enemy} attacked you and you have {hp} hp left!")
    hurt = random.randrange(10,20)
    if attack == 'kick':
      enemyhp = enemyhp - 20
      print(f"You kicked {enemy} in the shin dealing 20 damage. {enemy} has {enemyhp} hp left.")
      hp = hp - hurt
      print(enemyattack)
    elif attack == 'punch':
      enemyhp = enemyhp - random.randrange(10, 30)
      print(f"You punched {enemy} in the face and {enemy} has {enemyhp} left!")
      hp = hp - hurt
      print(enemyattack)
    elif attack == 'LOL':
      enemyhp = enemyhp - 40
      print(f"YOU HAVE DEALT CRITICAL DAMAGE. Your enemy has {enemyhp} hp remaining and you have {hp} hp.")
      hp = hp - 5
      print(f"{enemy} stumbled and only dealt 5 damage.")
    else:
      hp = hp - 10
      print("Wrong move! You stumbled and took extra damage!")
      hp = hp - hurt
      print(enemyattack)

  if hp > enemyhp:
    print(f"Your hp is {hp} and {enemy} hp is {enemyhp}.")
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
