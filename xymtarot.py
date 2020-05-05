#Created by Marc David
#05-05-2020

import random


minArcana = ['Wands', 'Pentacles', 'Cups', 'Swords']

majArcana = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'ZAWARUDO']

class TarotCard:
  def __init__(self, arcana, num):
    self.arcana = arcana
    self.num = num

  def flipCard(self):
    self.orientation = random.choice(['Upright', 'Reversed'])
    print(f"{self.orientation}, {self.arcana} of {self.num}")

class Deck:
  def __init__(self):
    self.newDeck = []
    self.generateDeck()

  def generateDeck(self):
    minorA = [TarotCard(minArcana, num) for minArcana in minArcana for num in range(1,15)]
    majorA = [TarotCard(majArcana, num) for majArcana, num in enumerate(majArcana)]
    generated = minorA + majorA
    for x in generated:
      self.newDeck.append(x)

  def shufflecards(self):
    random.shuffle(self.newDeck)

  def reveal(self):
    for c in self.newDeck:
      c.flipCard()

  def drawTarot(self):
    return self.newDeck.pop()
  
class Player:
  def __init__(self, username):
    self.username = username
    self.hand = []
  
  def playerDraw(self, deck):
    self.hand.append(deck.drawTarot())
    return self
  
  def showUserCard(self):
    for card in self.hand:
      card.flipCard()

  def playerHand(self, deck):
    self.hand.append(deck.drawTarot())
    self.hand.append(deck.drawTarot())
    self.hand.append(deck.drawTarot())
    return self

def main():
  playerDeck = Deck()
  playerDeck.shufflecards()
  print("Welcome to Xym Tarot Reading.")
  newplayer = input("Please enter your name: ")
  user = Player(newplayer)
  print(f"Hello {newplayer}. These are your Tarot readings for today: ")
  user.playerHand(playerDeck)
  user.showUserCard()
  print(f"Thank you for using our services, {newplayer}. May you have wonderful fortune.")

if __name__ == "__main__":
    main()
