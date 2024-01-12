# black jack project
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_hand = []
dealer_hand = []
amount_of_mycards = 2
amount_of_dealercards = 2
game_on = True


def clear_the_game():
    my_hand.clear()
    dealer_hand.clear()
    clear()


def blackjack():
    global game_on
    want_to_play = input("Hello and welcome to the casino do you want to play? 'y' for yes 'n' for no: ").lower()
    if want_to_play == 'y':
        clear_the_game()
        draw_another_one = True
        for i in range(amount_of_mycards):
            my_hand.append(random.choice(cards))
        sum_my_hand = sum(my_hand)

        for i in range(amount_of_dealercards):
            dealer_hand.append(random.choice(cards))
        sum_dealer_hand = sum(dealer_hand)

        print(f"This is your cards: {my_hand}, current score: {sum_my_hand}\nDealer first card: {dealer_hand[0]}")
        while draw_another_one:
            draw_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if draw_card == 'y':
                for i in range(1):
                    my_hand.append(random.choice(cards))
                    sum_my_hand += my_hand[-1]
                    print(f"This is your new cards: {my_hand}, new score: {sum_my_hand}")
                    if sum_my_hand > 21:
                        print(
                            f"You got busted, current score : {sum_my_hand}, dealer's score: {sum_dealer_hand}. dealer wins")
                        draw_another_one = False
            else:
                draw_another_one = False

                while sum_dealer_hand < 17:
                    for i in range(1):
                        dealer_hand.append(random.choice(cards))
                        sum_dealer_hand += dealer_hand[-1]
                if sum_dealer_hand > 21:
                    print(f"Dealer got busted, his score:{sum_dealer_hand}, your score:{sum_my_hand}. YOU WIN")
                if sum_dealer_hand <= 21 and sum_my_hand <= 21:
                    if sum_my_hand == sum_dealer_hand:
                        print(f"Its a Draw, current score : {sum_my_hand}, dealer's score: {sum_dealer_hand} ")
                    elif sum_my_hand > sum_dealer_hand:
                        print(f"You win, current score : {sum_my_hand}, dealer's score: {sum_dealer_hand}")
                    else:
                        print(f"Dealer wins, current score : {sum_my_hand}, dealer's score: {sum_dealer_hand}")

    else:
        game_on = False
        print("Bye Bye")


print(logo)
while game_on:
    blackjack()
