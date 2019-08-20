from random import shuffle
from random import randint
deck = []
diamonds = 'diamonds'
hearts = 'hearts'
spades = 'spades'
clubs = 'clubs'
cards = [diamonds, hearts, spades, clubs]


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color


class Deck:
    def __init__(self):
        self.contents = []
        self.contents = [Card(value, color) for value in range(1, 14) for color in cards]
        self.sum = 0
        self.dealer = 0

    def shuffle(self):
        shuffle(self.contents)
        for i in range(0, len(d1.contents)):
            print(self.contents[i].value)
            print(self.contents[i].color)

    def deal(self):
        deal = True
        random = randint(0, len(self.contents) - 1)
        print(f"You drew the {self.contents[random].value} of {self.contents[random].color}")
        self.sum += self.contents[random].value
        self.contents.remove(self.contents[random])
        random = randint(0, len(self.contents) - 1)
        print(f"You drew the {self.contents[random].value} of {self.contents[random].color}")
        self.sum += self.contents[random].value
        self.contents.remove(self.contents[random])
        print(f"Your sum is {self.sum}")
        if self.sum > 21:
            print("You have broke")
            deal = False
        while deal:
            decision = input("Would you like to hit or pass?")

            if decision.lower() == "hit":
                random = randint(0, len(self.contents) - 1)
                print(f"You drew the {self.contents[random].value} of {self.contents[random].color}")
                self.sum += self.contents[random].value
                self.contents.remove(self.contents[random])
                print(f"Your sum is {self.sum}")
                if self.sum > 21:
                    print("You have broke")
                    random = randint(0, len(self.contents) - 1)
                    print(f"{self.contents[random].value} of {self.contents[random].color}")
                    self.dealer += self.contents[random].value
                    random = randint(0, len(self.contents) - 1)
                    print(f"{self.contents[random].value} of {self.contents[random].color}")
                    self.dealer += self.contents[random].value
                    print(f"The dealer's total is {self.dealer}")

                    if self.dealer > self.sum:
                        print("You have lost!!")
                    break
            else:
                print(f"Your sum is {self.sum}")
                random = randint(0, len(self.contents) - 1)
                print("\nThe dealer drew:")
                print(f"{self.contents[random].value} of {self.contents[random].color}")
                self.dealer += self.contents[random].value
                random = randint(0, len(self.contents) - 1)
                print(f"{self.contents[random].value} of {self.contents[random].color}")
                self.dealer += self.contents[random].value
                print(f"The dealer has a total of {self.dealer}")

                if self.dealer > self.sum:
                    print("You lost!!")
                else:
                    print("You won!!")
                break


d1 = Deck()
d1.deal()
#d1.shuffle()



