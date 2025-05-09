__author__ = 'Chigozie Nnani, cfnnani@unc.edu, Onyen = cfnnani'

import random

# Generate card values for player & dealer
def deal_card():
    # Values 1-9 have a single chance, 10 has four chances (10, J, Q, K)
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_values)

# Get player's score & ask if they want to HIT or STAY
def get_player_score():
    player_cards = [deal_card(), deal_card()]
    player_score = sum(player_cards)
    print(f"Your hand of two cards has a total value of {player_score}.")
    print("Would you like to take another card? (y/n)", end=' ')

    while player_score < 21:
        action = input().lower()
        if action == 'y':
            new_card = deal_card()
            player_score += new_card
            print(f"Your hand now has a total value of {player_score}.")
            if player_score < 21:
                print("Would you like to take another card? (y/n)", end=' ')
        elif action == 'n':
            print(f"You have stopped taking more cards with a hand value of {player_score}.")
            break

    if player_score > 21:
        print(f"You BUSTED with a total value of {player_score}!")

    return player_score

# Dealer's score & turn simulation (draw cards until at least 16)
def get_dealer_score():
    dealer_cards = [deal_card(), deal_card()]
    dealer_score = sum(dealer_cards)
    while dealer_score < 16:
        dealer_cards.append(deal_card())
        dealer_score = sum(dealer_cards)
    return dealer_score

def main():
    while True:
        player_score = get_player_score()
        if player_score > 21:
            print("\n** You lose. **\n")
        else:
            dealer_score = get_dealer_score()
            if dealer_score > 21:
                print(f"The dealer BUSTED with a value of {dealer_score}!")
                print("\n** You win! **\n")
            else:
                print(f"The dealer was dealt a hand with a value of {dealer_score}.")
                if dealer_score > player_score:
                    print("\n** You lose! **\n")
                elif dealer_score < player_score:
                    print("\n** You win! **\n")
                else:
                    print("\n** It's a draw! **\n")

        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()