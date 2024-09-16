import random
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def current_cards(your_cards, computer_cards):
    print(f"Your Cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's first card: {computer_cards[0]}\n")

def final_cards(your_cards, computer_cards):
    print(f"\nYour Cards: {your_cards}, final score: {sum(your_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score {sum(computer_cards)}")

while True:
    # os.system('cls')
    print("Do you want to play a game of Blackjack?")
    choice = input("Type 'y' or 'n': ")

    if choice == 'n': break
    elif choice != 'y':
        print("Please select a valid option!", end="\n\n")
        continue

    your_cards = [random.choice(cards) for i in range(2)]
    computer_cards = [random.choice(cards) for i in range(2)]
    current_cards(your_cards, computer_cards)

    while True:

        # primary checkings!
        if sum(your_cards) == 21:
            result = "You've got Blackjack, you win!"
            break

        elif sum(computer_cards) == 21:
            result = "Lose, opponent has Blackjack!"

        condition = 'y'
        while condition == 'y':
            if sum(computer_cards) < 21:
                computer_cards.append(random.choice(cards))
            
            if(sum(your_cards) < 21):
                condition = input("Type 'y' to get another card, type 'n' to pass: ")
                if condition == 'y':
                    your_cards.append(random.choice(cards))
                    current_cards(your_cards, computer_cards)
            else: break
        
        # main checking conditions!
        if sum(your_cards) < 21 and sum(computer_cards) < 21:
            if sum(your_cards) == sum(computer_cards):
                result = "Draw.."

            elif sum(your_cards) < sum(computer_cards):
                result = "You lose :("

            elif sum(your_cards) > sum(computer_cards):
                result = "You win :D"
        
        elif sum(your_cards) > 21 or sum(computer_cards) > 21:
            if sum(your_cards) > sum(computer_cards):
                result = "You've got more cards!\nYou lose :("
            elif sum(computer_cards) > sum(your_cards):
                result = "Computer got more cards!\nYou win :D"
        
        break

    final_cards(your_cards, computer_cards)
    print(result + "\n")
    