import random

def deal_card():
    cards = [6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lost, opponent has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lost"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lost"
def play_game():
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    game_is_over = False
    while not game_is_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score == 0 or user_score > 21:
            game_is_over = True
        else:
            choice = input("Type 'y' to draw another card, 'n' to pass: ")
            if choice == "y":
                user_cards.append(deal_card())
            else:
                game_is_over = True
    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(compare(user_score, computer_score))
    print(computer_cards)
while input("Do you want to play again print 'y' if yes and 'n' if no ") == "y":
    play_game()



    
    