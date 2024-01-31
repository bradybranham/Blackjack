import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_prompt = input("Would you like to play a game of blackjack? Please type 'y' or 'n': ")
print("\n ----- \n")

def card_draw():
    card_num = random.randint(0, 12)
    return cards[card_num]

def player_start():
    add_card_p = card_draw()
    player_cards.append(add_card_p)
    add_card_p = card_draw()
    player_cards.append(add_card_p)

def dealer_start():
    add_card_d = card_draw()
    dealer_cards.append(add_card_d)
    print(f"Dealer: {dealer_cards}")
    add_card_d = card_draw()
    dealer_cards.append(add_card_d)

def hand_reveal():
    print(f"Your cards: {player_cards}")
    print(f"Dealer's cards: {dealer_cards}")

game_active = False

if game_prompt == "y":
    game_active = True
else:
    print("Then why even launch the game?")

while game_active == True:
    #Player
    player_cards = []
    dealer_cards = []
    player_count = 0
    player_start()
    print(f"Player: {player_cards}")
    for card in player_cards:
        player_count += card
    print(f"Your hand is equal to: {player_count}\n")
    dealer_start()
    print("")
    hand_ongoing = True
    player_count = 0
    while hand_ongoing == True:
        deal_req = input("Would you like to draw a card? Type 'hit' or 'stand': ")
        if deal_req == "hit":
            player_cards.append(card_draw())
            print("\n ----- \n")
            print(f"Reminder: The dealer has a {dealer_cards[0]} showing.")
            print("")
            print(f"Player: {player_cards}")
            for card in player_cards:
                player_count += card
            print(f"Your hand is equal to: {player_count}\n")
            if player_count > 21:
                print("\nYou busted! You lose :(")
                hand_ongoing = False
            else:
                player_count = 0
        else:
            hand_ongoing = False
        
        
    
    
    #Dealer
    dealer_cards = []
    hand_ongoing_dealer = True
    dealer_count = 0
    while hand_ongoing_dealer == True:
        for card in dealer_cards:
            dealer_count += card
        if dealer_count <= 16:
            dealer_cards.append(card_draw())
            dealer_count = 0
        elif dealer_count <= 21:
            hand_ongoing_dealer = False
        else:
            hand_ongoing_dealer = False

#comparison
    player_count = 0
    dealer_count = 0
    for card in player_cards:
        player_count += card
    for card in dealer_cards:
        dealer_count += card

    print("\n---- Game Finished ----\n")
    hand_reveal()
    
    if player_count < 22 :
        if player_count > dealer_count:  
            print("You win!")
        elif player_count == dealer_count:
            print("Tie game! Try again!")
        elif dealer_count > 21:
            print("You win!")
        else:
            print("You lose! :(")
            
    replay_req = input("\nWould you like to play again? Type 'y' or 'n': ")
    if replay_req == "n":
        game_active = False
    else:
        print("\n ---- New Game ---- \n")

