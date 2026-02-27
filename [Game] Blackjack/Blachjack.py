from random import*
from pickle import*
print("Welcome to Blackjack!")
print("This program simulates a game of Blackjack.")
def play():
    money=5000
    while not money<=0:
        print("You have $",money)
        print("How much would you like to bet?")
        bet=input()
        if bet.upper()=="QUIT" or bet.upper()=="EXIT" or bet.upper()=="STOP" or bet.upper()=="Q":
            print("Thanks for playing! Goodbye.")
            return
        bet=int(bet)
        while bet>money:
            print("You cannot bet more than you have. Please enter a valid bet.")
            bet=int(input())
        print("You bet $",bet)
        print("Dealing cards...")
        serving()
        file_play=open("cards.txt","rb")
        data=load(file_play)
        file_play.close()
        player_hand=[data[0],data[1]]
        sum_player=0
        for cards in player_hand:
            sum_player+=cards["value"]
        serving()
        file_play=open("cards.txt","rb")
        data=load(file_play)
        dealer_hand=[data[0],data[1]]
        sum_dealer=0
        for card in dealer_hand:
            sum_dealer+=card["value"]
        file_play.close()
        print("Your hand:",player_hand)
        print("Dealer's hand:",dealer_hand[0])
        if sum_player==21:
            print("Blackjack! You win!")
            money+=bet*2
            print("You now have $",money)
            return
        if sum_player>21:
            print("Bust! You lose.")
            money-=bet
            print("You now have $",money)
            return
        while sum_player<21:
            print("Do you want to hit 'H' or stand 'S' ?")
            action=input()
            while action.upper()!="HIT" and action.upper()!="H" and action.upper()!="STAND" and action.upper()!="S":
                print("Invalid input. Please enter 'hit' or 'stand' or 'H' or 'S'.")
                action=input()
            if action.upper()=="HIT" or action.upper()=="H":
                deal_card()
                file_deal=open("deal_cards.txt","rb")
                data=load(file_deal)
                dealed_card=data
                file_deal.close()
                player_hand.append(dealed_card)
                print("Your hand:",player_hand)
                sum_player+=player_hand[-1]["value"]
                for card in player_hand:
                    sum_player+=card["value"]
            elif action.upper()=="STAND" or action.upper()=="S":
                break
        if sum_player>21:
            print("Bust! You lose.")
            money-=bet
            print("You now have $",money)
            return
        print("Dealer's hand:",dealer_hand)
        while sum_dealer<17:
            file_deal=open("deal_cards.txt","rb")
            data=load(file_deal)
            dealed_card=data[0]
            file_deal.close()
            dealer_hand.append(dealed_card)
            print("Dealer's hand:",dealer_hand)
            sum_dealer+=dealer_hand[-1]["value"]
            for card in dealer_hand:
                sum_dealer+=card["value"]
        if sum_dealer>21:
            print("Dealer busts! You win!")
            money+=bet*2
            print("You now have $",money)
            return
        if sum_player>sum_dealer:
            print("You win!")
            money+=bet*2
            print("You now have $",money)
        elif sum_player<sum_dealer:
            print("You lose.")
            money-=bet
            print("You now have $",money)
        else:
            print("It's a tie! Your bet is returned.")
            print("You now have $",money)
card=["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
value=[2,3,4,5,6,7,8,9,10,10,10,10,11]
card_suit=["Hearts","Diamonds","Clubs","Spades"]
def serving():
    file=open("cards.txt","wb")
    card_detail=dict()
    for i in range(2):
        value_num=value[randint(0,12)]
        card_detail[i]={"value":value_num,"card":card[value_num-2],"suit":card_suit[randint(0,3)]}
        card_detail[i]["card"]=card[value_num-2]
        card_detail[i]["suit"]=card_suit[randint(0,3)]
    dump(card_detail,file)
    file.close()
def deal_card():
    file=open("deal_cards.txt","wb")
    card_detail=dict()
    value_num=value[randint(0,12)]
    card_detail={"value":value_num,"card":card[value_num-2],"suit":card_suit[randint(0,3)]}
    card_detail["card"]=card[value_num-2]
    card_detail["suit"]=card_suit[randint(0,3)]
    dump(card_detail,file)
    file.close()
play()