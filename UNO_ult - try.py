
import random


###########################
#    CPU Moves Function   #
###########################


def cpu_moves(deck, cpu_cards, top_card, who_played, cards_taken):


    Others = ['Draw Two','Wild Draw 4','Wild']

    def take_card(deck, cpu_cards, cards_taken):
        new_card = random.choice(deck)
        #ADD card to deck
        cpu_cards.append(new_card)
        #Remove card from deck
        deck.remove(new_card)
        #Count cards
        cards_taken["CPU"] = i + 1
        return
        

    def play_card(top_card, available_card, cpu_cards, who_played):
        #TOP CARD change.
        top_card.append(available_card)
        top_card.pop(0)
        #TRACKING played cards
        who_played["CPU"] = top_card[0][1]
        #REMOVE card from CPU list
        cpu_cards.remove(available_card)
        return

    
        

    
    #CHECK what card is on of discard pile.
    for card in top_card:
        color, num = 0, 1

        
        #NORMAL
        if card[1] not in Others:
            for available_card in cpu_cards:
                color, num = 0, 1
                if available_card[num] == top_card[0][num] or available_card[color] == top_card[0][color] or available_card[color] == 0:
                    play_card(top_card, available_card, cpu_cards, who_played)
                    return
            for card in cpu_cards:
                color, num = 0, 1
                if card[num] != top_card[0][num] or card[color] != top_card[0][color]:
                    for i in range(1):
                        take_card(deck, cpu_cards, cards_taken)
                        return
                    
        #DRAW TWO
        elif card[num] == "Draw Two":
            #IF CPU played "Draw Two"
            if who_played["CPU"] == "Draw Two" or cards_taken["CPU"] == 2:
                for available_card in cpu_cards:
                    if card[color] == available_card[color]:
                        play_card(top_card, available_card, cpu_cards, who_played)
                        cards_taken["CPU"] = 0
                        return
                #CPU does not have card.
                for i in range(1):
                    take_card(deck, cpu_cards, cards_taken)
                    return
    
            #IF USER played "Draw Two"
            if who_played["USER"] == "Draw Two":
                for i in range(2):
                    take_card(deck, cpu_cards, cards_taken)
                return
            
        #WILD
        #####
        elif card[num] == "Wild":
            while True:
                #CPU
                if who_played["CPU"] == "Wild":
                    for available_card in cpu_cards:
                        play_card(top_card, available_card, cpu_cards, who_played)
                        return
                #USER
                elif who_played["USER"] == "Wild":
                    declared_color = input("Delare a color: ")
                    for available_card in cpu_cards:
                        if declared_color == available_card[color]:
                            play_card(top_card, available_card, cpu_cards, who_played)
                            return
                #CARD unavailable
                for available_card in cpu_cards:
                    if declared_color != available_card[color] and declared_color in ['red','yellow','green','blue']:
                        for i in range(1):
                            take_card(deck, cpu_cards, cards_taken)
                        return
                else:
                    print("Invalid color choice. Try again!")
                    print()
                    continue 

        #WILD DRAW 4
        ############
        elif card[num] == "Wild Draw 4":
            while True:
                #CPU
                if who_played["CPU"] == "Wild Draw 4":
                    for available_card in cpu_cards:
                        play_card(top_card, available_card, cpu_cards, who_played)
                        return
                
                #USER
                elif who_played["USER"] == "Wild Draw 4":
                    declared_color = input("Delare a color: ")
                    for available_card in cpu_cards:
                        if declared_color == available_card[color]:
                            play_card(top_card, available_card, cpu_cards, who_played)
                            return
                        
                #CARD unavailable
                for available_card in cpu_cards:
                    if declared_color != available_card[color] and declared_color in ['red','yellow','green','blue']:
                        for i in range(4):
                            take_card(deck, cpu_cards, cards_taken)
                        return
                else:
                    print("Invalid color choice. Try again!")
                    print()
                    continue

        #SKIP or REVERSE
        if top_card[0][1] == "Skip" or top_card[0][1] == "Reverse" and who_played["USER"] == "Skip" or who_played["USER"] == "Reverse":
            return




#________________________________________________________________________________________________#
##################################################################################################

###########################
#  User Moves Function    #
###########################

def user_moves(user_cards, top_card, deck, who_played, cards_taken_from_deck, cards_taken):
    print("")
    print("Enter '0' to draw card from pile")
    print("Enter number to play card")
    print('Play your card!')
    print('')
    cpu_request = []
    Others = ['Draw Two','Wild Draw 4','Wild']

    def take_card(deck, user_cards, cards_taken):
        new_card = random.choice(deck)
        #ADD new card to USER list
        user_cards.append(new_card)
        #Remove card from deck
        deck.remove(new_card)
        #Count cards
        cards_taken["USER"] = i + 1

    def play_card(card, top_card, who_played, user_cards):
        #Placing card on TOP.
        top_card.append(card)
        top_card.pop(0)
        #TRACKING played cards
        who_played["USER"] = top_card[0][1]
        #Removing the CARD from the USER's card list.
        user_cards.remove(card)

    
    #NORMAL MOVE
    ############
    if top_card[0][1] not in Others:
        while True:
            move = int(input('Card Number: '))
            #Draw card
            if move == 0:
                for i in range(1):
                    take_card(deck, user_cards, cards_taken)
                    return
            #Invalid Move
            elif move > len(user_cards):
                print("Not a valid choice,Try again!")
                continue
            #Success
            elif user_cards[move-1][0] == top_card[0][0] or user_cards[move-1][1] == top_card[0][1] or user_cards[move-1][0] == 0:
                #Looping through USER's Cards. (To find the card that will be TOP.
                for card in user_cards:
                    #If a CARD matches the USER mover.
                    if card == user_cards[move-1]:
                        play_card(card, top_card, who_played, user_cards)
                        return
            #Failure      
            elif user_cards[move-1][0] != top_card[0][0] or user_cards[move-1][1] != top_card[0][1]:
                print()
                print("Your card Colour or Number does not match the Colour or Number on top of pile Try again")
                continue   
    
    #DRAW TWO
    #########
    elif top_card[0][1] == "Draw Two":
        #CPU
        if who_played["CPU"] == "Draw Two" and cards_taken["USER"] != 2:
            print('The top card is Draw Two')
            print("Enter 'd' to draw your TWO cards")
            while True:
                answer = input("Action: ")
                if answer.lower() == 'd':
                    for i in range(2):
                        take_card(deck, user_cards, cards_taken)
                    return
                else:
                    print()
                    print("Invalid answer, Try again.")      
        #USER         
        elif who_played["USER"] == "Draw Two" or cards_taken["USER"] == 2:
            while True:
                move = int(input('Card Number: '))
                #INVALID CARD NUMBER      
                if move > len(user_cards):
                    print()
                    print("Invalid move Try again!")
                    continue
                #DRAW
                elif move == 0:
                    for i in range(1):
                        take_card(deck, user_cards, cards_taken)
                        return
                #PLAY
                elif user_cards[move-1][0] == top_card[0][0] or user_cards[move-1][1] == top_card[0][1]:
                    #Looping through USER's Cards. (To find the card that will be TOP.
                    for card in user_cards:
                        #If a CARD matches the USER mover.
                        if card == user_cards[move-1]:
                            play_card(card, top_card, who_played, user_cards)
                            cards_taken["USER"] = 0
                            return
                        
                elif user_cards[move-1][0] != top_card[0][0] or user_cards[move-1][1] != top_card[0][1]:
                    print()
                    print("Your card Colour or Number does not match the Colour or Number on top of pile Try again")
                    print("Remember: You can ENTER '0' to draw a new card if you don't have the colour")
                    continue



    #WILD DRAW 4 TRY
    ################
    elif top_card[0][1] == "Wild Draw 4":

        #USER
        if who_played["USER"] == "Wild Draw 4":
            while True:
                move = int(input('Card Number: '))
                #INVALID CARD NUMBER      
                if move > len(user_cards):
                    print()
                    print("Invalid move Try again!")
                    continue
                #DRAW
                elif move == 0:
                    for i in range(1):
                        take_card(deck, user_cards, cards_taken)
                        return
                #PLAY
                elif top_card[0][0] == 0:
                    #Looping through USER's Cards. (To find the card that will be TOP.
                    for card in user_cards:
                        #If a CARD matches the USER mover.
                        if card == user_cards[move-1]:
                            play_card(card, top_card, who_played, user_cards)
                            return
                        
                elif user_cards[move-1][0] != top_card[0][0] or user_cards[move-1][1] != top_card[0][1]:
                    print()
                    print("Your card Colour or Number does not match the Colour or Number on top of pile Try again")
                    print("Remember: You can ENTER '0' to draw a new card if you don't have the colour")
                    continue

        #CPU
        elif who_played["CPU"] == "Wild Draw 4":
            #GET color request from CPU.
            while True:
                cpu_request.append(random.choice(deck))
                if cpu_request[0][0] not in ['red','green','blue','yellow']:
                    cpu_request = []
                    continue
                else:
                    break
            
            while True:
                print('The top card is Wild Draw 4')
                print("Enter 'draw' to draw your FOUR cards")
                print("Enter 'play' if you have the the requested colour")
                answer = input("Action: ")
                #PLAY
                if answer.lower() == 'play':
                    while True:
                        print()
                        print(f'Card colour requested: {cpu_request[0][0]}')
                        print()
                        move = int(input('Card Number: '))
                        #INVALID CARD NUMBER      
                        if move > len(user_cards) or user_cards[move-1][0] == 0:
                            print()
                            print("Invalid move Try again!")
                            continue
                        #VALID CARD NUMBER
                        run = 0
                        for card in user_cards:
                            run += 1
                            #Success!
                            if card[0] == user_cards[move-1][0] and cpu_request[0][0] == user_cards[move-1][0]:
                                play_card(card, top_card, who_played, user_cards)
                                cpu_request = []
                                return
                            #Failure!
                            elif card[0][0] != user_cards[move-1][0] and cpu_request[0][0] != user_cards[move-1][0] and len(user_cards) == run:
                                print('The colour does not match requested colour')
                                print()
                                go_again = input('Try again? (y/n) :')
                                break
                        if go_again == 'y':
                            continue
                        elif go_again == 'n':
                            break
                #DRAW
                elif answer.lower() == 'draw':
                    for i in range(4):
                        take_card(deck, user_cards, cards_taken)
                    return
                


    #WILD
    #####
    elif top_card[0][1] == "Wild":
        #USER
        if who_played["USER"] == "Wild":
            while True:
                move = int(input('Card Number: '))
                #Draw card
                if move == 0:
                    for i in range(1):
                        take_card(deck, user_cards, cards_taken)
                        return
                #Success
                if top_card[0][0] == 0:
                    #Looping through USER's Cards. (To find the card that will be TOP.
                    for card in user_cards:
                        #If a CARD matches the USER mover.
                        if card == user_cards[move-1]:
                            play_card(card, top_card, who_played, user_cards)
                            return
                #Failure      
                elif user_cards[move-1][0] != top_card[0][0] or user_cards[move-1][1] != top_card[0][1]:
                    print()
                    print("Your card Colour or Number does not match the Colour or Number on top of pile Try again")
                    continue
                
        #CPU
        elif who_played["CPU"] == "Wild":
            while True:
                cpu_request.append(random.choice(deck))
                if cpu_request[0][0] not in ['red','green','blue','yellow']:
                    cpu_request = []
                    continue
                else:
                    break
            
            while True:
                print('The top card is Wild')
                print("Enter 'draw' to draw your card")
                print("Enter 'play' if you have the the requested colour")
                answer = input("Action: ")
                #PLAY
                if answer.lower() == 'play':
                    while True:
                        print()
                        print(f'Card colour requested: {cpu_request[0][0]}')
                        print()
                        move = int(input('Card Number: '))
                        #INVALID CARD NUMBER      
                        if move > len(user_cards):
                            print()
                            print("Invalid move Try again!")
                            continue
                        #VALID CARD NUMBER
                        run = 0
                        for card in user_cards:
                            run += 1
                            #Success!
                            if card[0] == user_cards[move-1][0] and cpu_request[0][0] == user_cards[move-1][0]:
                                play_card(card, top_card, who_played, user_cards)
                                cpu_request = []
                                return
                            #Failure!
                            elif card[0][0] != user_cards[move-1][0] and cpu_request[0][0] != user_cards[move-1][0] and len(user_cards) == run:
                                print('The colour does not match requested colour')
                                print()
                                go_again = input('Try again? (y/n) :')
                                break
                        if go_again == 'y':
                            continue
                        elif go_again == 'n':
                            break
                #DRAW
                elif answer.lower() == 'draw':
                    for i in range(1):
                        take_card(deck, user_cards, cards_taken)
                    return

    #SKIP or REVERSE
    if top_card[0][1] == "Skip" or top_card[0][1] == "Reverse" and who_played["CPU"] == "Skip" or who_played["CPU"] == "Reverse":
        return
                


#________________________________________________________________________________________________#
##################################################################################################




###########################
#  Cards View Function    #
###########################


def user_cards_view(user_cards):
    print('')
    print('=============================')
    print('=        Your Cards         =')
    print('_____________________________')
    print('=___________________________=')

    count = 1
    total = 0
    
    #Looping through cards to show.
    for x in range(len(user_cards)):
        print(f"= {count}. {user_cards[x][0]}: '{user_cards[x][1]}'")
        count += 1
        
    print('=___________________________=')
    print('')    

#________________________________________________________________________________________________#
##################################################################################################

###########################
#  Top Card View Function #
###########################
def top_card_view(deck, top_card):
    while True:
        top_card.append(random.choice(deck))
        if top_card[0][1] not in ['Draw Two','Wild Draw 4','Wild']:
            break
        else:
            continue
    print('')
    print('')
    print('')
    print('')
    print('')
    print('         Top Card            ')
    print('=============================')
    print(f"        {top_card[0][0]}: '{top_card[0][1]}'        ")
    print('_____________________________')
    for card in deck:
        if card == top_card[0]:
            deck.remove(card)   


#________________________________________________________________________________________________#
##################################################################################################


###########################
#     Dealer Function     #
###########################
def dealer_picker(numbers,colors):
     #Player moves
    while True:
         pick = input('Action: ')

         if pick.lower() == 'd':
             user_card = [random.choice(colors), random.choice(numbers)]

             if type(user_card[1]) != int:
                print('')
                print(f"your card is: {user_card[0]}: '{user_card[1]}'")
                print("Your card is not a number, please try again!")
                continue
             else:
                print('')
                print('')
                print(f"your card is: {user_card[0]}: '{user_card[1]}'")
                print('')
                break

    #CPU moves
    while True:
        cpu_card = [random.choice(colors), random.choice(numbers)]
        if type(cpu_card[1]) != int:
            continue
        else:
            break
    if user_card[1] == cpu_card[1]:
        print(f"your card is: {user_card[0]}: '{user_card[1]}'")
        print(f"My card is: {cpu_card[0]}: '{cpu_card[1]}'")
        print("That makes you the dealer. please Deal")
        print("We need to pick again")
        dealer_picker(numbers,colors)

    elif user_card[1] > cpu_card[1]:
        print(f"your card is: {user_card[0]}: '{user_card[1]}'")
        print(f"My card is: {cpu_card[0]}: '{cpu_card[1]}'")
        print("That makes YOU the dealer. please Deal")
        print('')
        print('')
        while True:
            print("Enter - 'd' - to Deal")
            user_deal = input('Action: ')
            if user_deal.lower() == 'd':
                print('Here!:')
                break
            else:
                print("Invalid action... enter 'd' to deal")
    elif user_card[1] < cpu_card[1]:
        print(f"your card is: {user_card[0]}: '{user_card[1]}'")
        print(f"My card is: {cpu_card[0]}: '{cpu_card[1]}'")
        print("That makes ME the dealer. Here!")
        print('')
        print('')

#________________________________________________________________________________________________#
##################################################################################################

###########################
#      Deal Function      #
###########################

def deal(deck, user_cards, cpu_cards):
    for x in range(1,8):
        #USER cards.
        ucard = random.choice(deck)
        user_cards.append(ucard)

        #CPU cards.
        ccard = random.choice(deck)
        cpu_cards.append(ccard)

        #Remove from deck.
        for card in deck:
            if card == ucard or card == ccard:
                deck.remove(card)
#________________________________________________________________________________________________#
##################################################################################################

def cards():
    
    numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'Skip','Skip','Draw Two','Draw Two','Reverse','Reverse']
    colors = ['red', 'yellow', 'green', 'blue']
    others = [[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4']]
    deck = [[color,number] for color in colors for number in numbers] + others
    user_cards = []
    cpu_cards = []
    top_card = []
    who_played = {"CPU": '',"USER": ''}
    cards_taken = {"CPU": 0,"USER": 0}
    cards_taken_from_deck = [1]
    

    #Functions
    dealer_picker(numbers,colors)
    deal(deck, user_cards, cpu_cards)
    user_cards_view(user_cards)
    top_card_view(deck, top_card)
    while True:
        print()
        cpu_moves(deck, cpu_cards, top_card, who_played, cards_taken)
        print(cpu_cards)
        print('')
        print('')
        print('')
        print('')
        print('')
        print('         Top Card            ')
        print('=============================')
        print(f"        {top_card[0][0]}: '{top_card[0][1]}'        ")
        print('_____________________________')
        print('')
        print('')
        print('')
        print('')
        print('')
        
        user_cards_view(user_cards)
        
        user_moves(user_cards, top_card, deck, who_played, cards_taken_from_deck, cards_taken)
        print(cpu_cards)
        if user_cards == []:
            return "Hooray!! You win."
        elif cpu_cards == []:
            return "Agh shame! YOU LOSE!! :("

    

     

   

        
cards()
