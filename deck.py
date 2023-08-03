import random
diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D"]
hand = []

while diamonds:
    print("Current Hand", hand)
    print("Remaining Cards", diamonds)
    user_input = input("Draw a card by enter or press 'Q' and enter to quit: ")

    if user_input.upper() == 'Q':
        break

random_card = random.choice(diamonds)
diamonds.remove(random_card)
hand.append(random_card)

print("Diamonds", diamonds)
print("hand", hand)

if not diamonds:
    print("There are no diamonds left")
