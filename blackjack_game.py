#Welcome to the game of Blackjack!
print("\nWelcome to the game of Blackjack!")
print("What is your name?")
name = input()
print(f"\nWelcome to the game of Blackjack, {name}! \nTry to win as many games in a row as you can!\n")

#initializing game statistics
game_number = 0
player_1_wins = 0
player_2_wins = 0
player_1_consecutive_wins = 0
player_1_consecutive_wins_max = 0
player_1_percentage_wins = "N/A"

def calculate_win_percentage(player_1_wins, game_number):
            if game_number > 0:
                return (player_1_wins / game_number) * 100
            else:
                return "N/A"

import random
from tabulate import tabulate

#initializing game loop
def blackjack_round():
    global game_number, player_1_wins, player_2_wins, player_1_consecutive_wins, player_1_consecutive_wins_max, player_1_percentage_wins
    #the sacred deck of cards
    deck = ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades']

    # Extract the first word of each item
    pure_deck  = [item.split(" ")[0] for item in deck]

    # Deal the cards
    Player_1_card_1 = random.choice(deck)
    deck.remove (Player_1_card_1) # Remove the card from the deck to prevent duplicates
    Player_1_card_2 = random.choice(deck)
    deck.remove (Player_1_card_2) # Remove the card from the deck to prevent duplicates
    Player_2_card_1 = random.choice(deck)
    deck.remove (Player_2_card_1) # Remove the card from the deck to prevent duplicates
    Player_2_card_2 = random.choice(deck)
    deck.remove (Player_2_card_2) # Remove the card from the deck to prevent duplicates


    readable_hand_1 = [Player_1_card_1, Player_1_card_2]
    readable_hand_2 = [Player_2_card_1, Player_2_card_2]

    print(tabulate(
    [
        [name, readable_hand_1],  # Player 1's row
        ['', ''],                # Empty row for spacing
        ['Player 2', f'[{Player_2_card_1}]\n']  # Player 2's row with brackets
    ],
    headers=['Player', 'Card'], tablefmt="grid"
))

    print(f"\n{name}, would you like to hit or stand?\n")

    hand_1 = [card.split(' ')[0] for card in readable_hand_1]

    hand_2 = [card.split(' ')[0] for card in readable_hand_2]

    #hand_1_value_function
    def hand_1_value(hand_1):
        hand_1 = [10 if str(x) in ['King', 'Queen', 'Jack'] else 11 if str(x) == 'Ace' else int(x) for x in hand_1]
        sum_hand_1 = sum(hand_1)
        count_A_hand_1 = hand_1.count(11)
        while sum_hand_1 > 21 and count_A_hand_1 > 0:
            sum_hand_1 -= 10
            count_A_hand_1 -= 1
        return sum_hand_1

    sum_hand_1 = hand_1_value(hand_1)

    # Check for blackjack
    if sum_hand_1 == 21 and len(hand_1) == 2:
        print(f"{name} has been dealt a blackjack, great work!")
    else:
        # Getting player input to hit or stand
        choice = input("Enter 'h' or 's': ")

        while choice == 'h':
            Player_1_new_card = random.choice(deck)
            deck.remove (Player_1_new_card) # Remove the card from the deck to prevent duplicates
            readable_hand_1.append(Player_1_new_card)
            hand_1 = [card.split(" ")[0] for card in readable_hand_1]  # Recalculate hand_1
            sum_hand_1 = hand_1_value(hand_1)  # Update hand_1 value
            print(f"\nNew card:\n{Player_1_new_card}")
            print(tabulate(
        [
            [name, readable_hand_1],  # Player 1's row
        ],
        headers=['Player', 'Card'], tablefmt="grid"
    ))
            print('\n')
            if sum_hand_1 == 21:
                print(f"{name} has a total of 21, great work!")
                break

            if sum_hand_1 > 21:
                print(f"{name} has gone bust with a total of {sum_hand_1}.")
                break

            choice = input("Enter 'h' or 's': ")

        else:
            print(f"\n{name} has stood with the hand: {readable_hand_1}, total = {sum_hand_1}\n")

    #Hand 2 hit or stand logic
    #print hand 2 second card
    print(f"Player 2 has been dealt:\n{readable_hand_2}\n")

    #hand_2_value function
    def hand_2_value(hand_2):
        hand_2 = [10 if str(x) in ['King', 'Queen', 'Jack'] else 11 if str(x) == 'Ace' else int(x) for x in hand_2]
        sum_hand_2 = sum(hand_2)
        count_A_hand_2 = hand_2.count(11)
        while sum_hand_2 > 21 and count_A_hand_2 > 0:
            sum_hand_2 -= 10
            count_A_hand_2 -= 1
        return sum_hand_2

    sum_hand_2 = hand_2_value(hand_2)

    #logic for hand 2 if no Ace
    if hand_2.count('Ace') == 0:
        while sum_hand_2 <= 16:
            Player_2_new_card = random.choice(deck)
            deck.remove(Player_2_new_card)  # Remove the card from the deck to prevent duplicates
            readable_hand_2.append(Player_2_new_card)
            hand_2 = [card.split(" ")[0] for card in readable_hand_2]  # Recalculate hand_2
            sum_hand_2 = hand_2_value(hand_2)  # Update hand_2 value
            print(f"Player 2 drew: {Player_2_new_card}")
            print(tabulate(
    [
        ['Player 2', f'[{readable_hand_2}]']  # Player 2's row with brackets
    ],
    headers=['Player', 'Card'], tablefmt="grid"
))

    #logic for hand 2 if 1 Ace
    if hand_2.count('Ace') == 1:
        while sum_hand_2 <= 17:
            Player_2_new_card = random.choice(deck)
            deck.remove(Player_2_new_card)  # Remove the card from the deck to prevent duplicates
            readable_hand_2.append(Player_2_new_card)
            hand_2 = [card.split(" ")[0] for card in readable_hand_2]  # Recalculate hand_2
            sum_hand_2 = hand_2_value(hand_2)  # Update hand_2 value
            print(f"Player 2 drew: {Player_2_new_card}")
            print(tabulate(
    [
        ['Player 2', f'[{readable_hand_2}]']  # Player 2's row with brackets
    ],
    headers=['Player', 'Card'], tablefmt="grid"
))

    def blackjack_hand_greater_than(hand_1, hand_2):
        # Convert face cards to 10
        hand_1 = [10 if str(x) in ['King', 'Queen', 'Jack'] else 11 if str(x) == 'Ace' else int(x) for x in hand_1]
        hand_2 = [10 if str(x) in ['King', 'Queen', 'Jack'] else 11 if str(x) == 'Ace' else int(x) for x in hand_2]

        # Calculate the sums
        sum_hand_1 = sum(hand_1)
        sum_hand_2 = sum(hand_2)

        # Adjust for Aces in hand_1
        count_A_hand_1 = hand_1.count(11)
        while sum_hand_1 > 21 and count_A_hand_1 > 0:
            sum_hand_1 -= 10
            count_A_hand_1 -= 1

        # Adjust for Aces in hand_2
        count_A_hand_2 = hand_2.count(11)
        while sum_hand_2 > 21 and count_A_hand_2 > 0:
            sum_hand_2 -= 10
            count_A_hand_2 -= 1

        # Return True if hand_1 beats hand_2, and False otherwise
        if sum_hand_1 <= 21 and (sum_hand_1 > sum_hand_2 or sum_hand_2 > 21):
            if sum_hand_2 <= 21:
                print(f"{name} wins with a total of {sum_hand_1}, beating Player 2 with a total of {sum_hand_2}.\n")
            elif sum_hand_2 > 21:
                print(f"{name} wins with a total of {sum_hand_1}, beating Player 2 who went bust.\n")
            return True
        elif sum_hand_1 == sum_hand_2 and sum_hand_1 <= 21:
            print(f"It is a draw with both players having a total of {sum_hand_1}.\n")
            return None
        elif sum_hand_1 > 21 and sum_hand_2 > 21:
            print(f"Both players went bust! \n {name} total = {sum_hand_1} \n Player 2 total = {sum_hand_2}\n")
            return None
        else:
            if sum_hand_1 <= 21:
                print(f"Player 2 (House) wins with a total of {sum_hand_2}, beating {name} with a total of {sum_hand_1}.\n\n")
            elif sum_hand_1 > 21:
                print(f"Player 2 (House) wins with a total of {sum_hand_2}, beating {name} who went bust.\n\n")
            return False
    
    
    #Call function once and store the result
    result = blackjack_hand_greater_than(hand_1, hand_2)

    # Do not print the result
    # print(result)

    #Update game statistics
    if result == True:
        game_number += 1
        player_1_wins += 1
        player_1_consecutive_wins += 1
        if player_1_consecutive_wins > player_1_consecutive_wins_max:
            player_1_consecutive_wins_max = player_1_consecutive_wins
    elif result == False:
        game_number += 1
        player_2_wins += 1
        player_1_consecutive_wins = 0
    elif result == None:
        game_number += 1
        player_1_consecutive_wins = 0

    #Update win percentage
    player_1_percentage_wins = calculate_win_percentage(player_1_wins, game_number)
        
#Game loop
while True:
    answer = input("\n\nWould you like to play a round? Enter 'y' or 'n': \n")
    if answer == 'y' or answer == 'yes' or answer == 'Yes' or answer == 'Y':
        print('\n')
        if game_number > 0:
            print(tabulate([
            ('Game number', game_number),
            (f'{name} wins', player_1_wins),
            (f'{name} consecutive wins', player_1_consecutive_wins),
            (f'{name} consecutive wins max', player_1_consecutive_wins_max),
            (f'{name} win percentage', f'{player_1_percentage_wins}%')
            ], headers=['Statistic', 'Value'], tablefmt="grid"))
            print("\n\n")
        blackjack_round()
    elif answer == 'n' or answer == 'no' or answer == 'No' or answer == 'N':
        print(tabulate([
        ('Game number', game_number),
        (f'{name} wins', player_1_wins),
        (f'{name} consecutive wins', player_1_consecutive_wins),
        (f'{name} consecutive wins max', player_1_consecutive_wins_max),
        (f'{name} win percentage', f'{player_1_percentage_wins}%')
        ], headers=['Statistic', 'Value'], tablefmt="grid"))
        print(f"Thank you for playing {name}! Goodbye!")
        break
    else:
        print("dont understand")