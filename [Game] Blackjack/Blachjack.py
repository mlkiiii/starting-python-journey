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
        for card in player_hand:
            sum_player+=card["value"]
        serving()
        file_play=open("cards.txt","rb")
        data=load(file_play)
        dealer_hand=[data[0],data[1]]
        sum_dealer=0
        for card in dealer_hand:
            sum_dealer+=card["value"]
        print("Your hand:",player_hand)
        print("Total value of your hand:",sum_player)
        print("Dealer's hand:",dealer_hand[0])
        print("Total value of dealer's hand:",data[0]["value"])
        file_play.close()
        if sum_player==21:
            print("Blackjack! You win!")
            money+=bet
            print("You now have $",money)
        else: 
            if sum_player>21:
                print("Bust! You lose.")
                money-=bet
                print("You now have $",money)   
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
                    dealt_card=data
                    file_deal.close()
                    player_hand.append(dealt_card)
                    print("Your hand:",player_hand)
                    sum_player+=dealt_card["value"]
                    print("Total value of your hand:",sum_player)
                    print("Dealer's hand:",dealer_hand)
                    print("Total value of dealer's hand:",sum_dealer)
                elif action.upper()=="STAND" or action.upper()=="S":
                    break            
            if sum_player>21:
                print("Bust! You lose.")
                money-=bet
                print("You now have $",money)
            else: 
                print("Dealer's hand:",dealer_hand)
                print("Total value of dealer's hand:",sum_dealer)
                while sum_dealer<17 and sum_player>sum_dealer and sum_dealer<21:
                    file_deal=open("deal_cards.txt","rb")
                    data=load(file_deal)
                    dealt_card=data
                    file_deal.close()
                    dealer_hand.append(dealt_card)
                    print("Dealer hits.")
                    print("Dealer's hand:",dealer_hand)
                    print("Total value of dealer's hand:",sum_dealer)
                    sum_dealer+=dealt_card["value"]
                if sum_dealer>21:
                    print("Dealer busts! You win!")
                    money+=bet
                    print("You now have $",money)       
                elif sum_player>sum_dealer:
                    print("You win!")
                    money+=bet
                    print("You now have $",money)
                elif sum_player<sum_dealer:
                    print("You lose.")
                    money-=bet
                    print("You now have $",money)    
                else:
                    print("It's a tie! Your bet is ed.")
                    print("You now have $",money)
        if money>0:
            print("Do you want to play again? (Y/N)")
            play_again=input()
            while play_again.upper()!="YES" and play_again.upper()!="Y" and play_again.upper()!="NO" and play_again.upper()!="N":
                print("Invalid input. Please enter 'yes' or 'no' or 'Y' or 'N'.")
                play_again=input()
            if play_again.upper()=="NO" or play_again.upper()=="N":
                print("Thanks for playing! Goodbye.")
                break
    print("You have run out of money. Game over.")
    print("Thanks for playing! Goodbye.")
card=["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
value=[2,3,4,5,6,7,8,9,10,10,10,10,11]
card_suit=["♥️","♦️","♣️","♠"]
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