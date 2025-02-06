
import random, time

numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'Skip','Skip','Draw Two','Draw Two','Reverse','Reverse']
colors = ['red', 'yellow', 'green', 'blue']
others = [[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4']]
deck = [[color,number] for color in colors for number in numbers] + others

who_played = {"CPU": '',"USER": 'Draw Two'}
cards_taken = {"CPU": 0,"USER": 0}



class cards():

    #DEALER - Choose who will deal
    def dealer(self):
        while True:
            pick = input('Action: ')
            if pick.lower() == 'd':
                user_card = [random.choice(colors),random.choice(range(10))]
                cpu_card = [random.choice(colors),random.choice(range(10))]
                if user_card[1] > cpu_card[1]:
                    print(f"your card is: {user_card[0]}: '{user_card[1]}'")
                    print(f"My card is: {cpu_card[0]}: '{cpu_card[1]}'")
                    print("That makes you the dealer. please Deal")
                    break
                elif user_card[1] < cpu_card[1]:
                    print(f"your card is: {user_card[0]}: '{user_card[1]}'")
                    print(f"My card is: {cpu_card[0]}: '{cpu_card[1]}'")
                    print("That makes ME the dealer. Here!")
                    break
                else:
                    print("It was a draw, Let's go again")
            else:
                print('Invalid action, enter d to Deal!')
        proceed = input('Press any key to continue: ...')
            
    #HAND - the cards given to player.
    def hand(self):
        inhand = []
        for x in range(1):
            ucard = random.choice(deck)
            inhand.append(ucard)
            if ucard in deck:
                deck.remove(ucard)
        return inhand

    #TOP CARD - The card at top of discard pile.
    def top_card(self):
        top_card = []
        while True:
            top_card.append(random.choice(deck))
            if top_card[0][1] not in ['Draw Two','Wild Draw 4','Wild']:
                break
            else:
                continue
        if top_card[0] in deck:
            deck.remove(top_card[0])
        return top_card

    #VIEW the Top Card
    def top_card_view(self, top_card):
        self.top_card = top_card
        print('         Top Card            ')
        print('=============================')
        print(f"        {top_card[0][0]}: '{top_card[0][1]}'        ")
        print('_____________________________')

    #VIEW the User Cards
    def view(self, user_cards):
        self.user_cards = user_cards
        print('')
        print('=============================')
        print('=        Your Cards         =')
        print('_____________________________')
        print('=___________________________=')
        
        for num in range(len(user_cards)):
            print(f"= {num+1}. {user_cards[num][0]}: '{user_cards[num][1]}'")
        print('=___________________________=')
        print('')

    

        
    #PLAY - The game being played.
    def PLAY_user(self, player_cards, top_card, who_played):
        self.player_cards = player_cards
        self.top_card = top_card
        self.who_played = who_played
        requested = [0]
        ineffective = ['wild', 'wild draw 4']

        def take_card(deck,player_cards,cards_taken):
            new_card = random.choice(deck)
            #ADD new card to USER list
            player_cards.append(new_card)
            #Remove card from deck
            deck.remove(new_card)
            #Count cards
            cards_taken["USER"] = 1

        def play_card(move, top_card, who_played, player_cards):
            #Placing card on TOP.
            top_card.append(player_cards[move-1])
            top_card.pop(0)
            #TRACKING played cards
            who_played["USER"] = top_card[0][1]
            #Removing the CARD from the USER's card list.
            player_cards.remove(player_cards[move-1])
            
        
        #NORMAL MOVE
        ############
        while True:
            if top_card[0][1] not in ["Draw Two",'Wild Draw 4',"Wild"]:
                while True:
                    while True:
                        move = int(input("Card Number: ..."))
                        if move > len(player_cards):
                            print("Not a valid choice, Try again")
                            continue
                        else:
                            break
                    #DRAW
                    if move == 0:
                        if top_card[0][1] == "wild draw 4" and who_played["CPU"]:
                            for i in range(4):
                                take_card(deck,player_cards,cards_taken)
                            return
                        else:
                            take_card(deck,player_cards,cards_taken)
                            print('Took')
                            return

                    #MOVE
                    elif player_cards[move-1][0] == top_card[0][0] or player_cards[move-1][1] == top_card[0][1] or player_cards[move-1][0] == 0:
                        play_card(move, top_card, who_played, player_cards)
                        if who_played["USER"] == "Reverse" or who_played["USER"] == "Skip":
                            print(f"Playing another card, because my card is '{top_card[0][1]}'")
                            time.sleep(4)
                            continue
                        print('Played')
                        return

                    #Request
                    elif player_cards[move-1][0] == requested[0] or top_card[0][1] in ineffective:
                        play_card(move, top_card, who_played, player_cards)
                        print('Played')
                        return
                        
                    else:
                        print('Invalid baba!')
                        continue

            #DRAW TWO
            #########
            elif top_card[0][1] == "Draw Two":
                
                if who_played["CPU"] == "Draw Two":
                    while True:
                        print("CPU played a Draw Two card")
                        time.sleep(4)
                        answer = input("Enter 'd' to draw 2 cards: ... ")
                        if answer == 'd':
                            break
                        else:
                            print('Invalid answer, Try again')
                            continue
                    for i in range(2):
                        take_card(deck,player_cards,cards_taken)
                    top_card.append([top_card[0][0], "draw two"])
                    top_card.pop(0)
                    print('Took')
                    return

            #WILD
            #####
            elif top_card[0][1] == "Wild":
                if who_played["CPU"] == "Wild":
                    requested.append(random.choice(colors))
                    requested.pop(0)
                    top_card.append([top_card[0][0], "wild"])
                    top_card.pop(0)
                    print()
                    print(f"CPU is asking for {requested}")
                    continue
                elif who_played["USER"] == "Wild":
                    top_card.append([top_card[0][0], "wild"])
                    top_card.pop(0)
                    continue

            #WILD DRAW FOUR
            ###############
            elif top_card[0][1] == "Wild Draw 4":
                if who_played["CPU"] == "Wild Draw 4":
                    requested.append(random.choice(colors))
                    requested.pop(0)
                    top_card.append([top_card[0][0], "wild draw 4"])
                    top_card.pop(0)
                    print()
                    print(f"CPU is asking for {requested}")
                    continue
                elif who_played["USER"] == "Wild Draw 4":
                    top_card.append([top_card[0][0], "wild draw 4"])
                    top_card.pop(0)
                    continue


    #PLAY - CPU player
    def PLAY_cpu(self, player_cards, top_card, who_played):
        self.player_cards = player_cards
        self.top_card = top_card
        self.who_played = who_played
        requested = [0]
        ineffective = ['wild', 'wild draw 4']

        def take_card(deck,player_cards,cards_taken):
            new_card = random.choice(deck)
            #ADD new card to USER list
            player_cards.append(new_card)
            #Remove card from deck
            deck.remove(new_card)
            #Count cards
            cards_taken["CPU"] = 1

        def play_card(card, top_card, who_played, player_cards):
            #Placing card on TOP.
            top_card.append(card)
            top_card.pop(0)
            #TRACKING played cards
            who_played["CPU"] = top_card[0][1]
            #Removing the CARD from the USER's card list.
            player_cards.remove(card)



        #NORMAL MOVE
        ############
        while True:
            color, value = 0,1

            if top_card[0][value] not in ["Draw Two",'Wild Draw 4',"Wild"]:

                #Wild Draw 4
                for card in player_cards:
                    if top_card[0][1] == "wild draw 4" and who_played["USER"]:
                            for i in range(4):
                                take_card(deck,player_cards,cards_taken)
                            return
                #Wild
                for card in player_cards:
                    if top_card[0][1] == "wild" and who_played["USER"]:
                        take_card(deck,player_cards,cards_taken)
                        return
                

                #PLAY
                for card in player_cards:
                    if card[value] == top_card[0][value] or card[color] == top_card[0][color] or top_card[0][color] == 0:
                        play_card(card, top_card, who_played, player_cards)
                        if who_played["CPU"] == "Reverse" or who_played["CPU"] == "Skip":
                            print(f"Playing another card, because my card is '{top_card[0][1]}'")
                            time.sleep(4)
                            continue
                        return

                #DRAW
                for card in player_cards:
                    #No Match on Main 
                    if card[value] != top_card[0][value] or card[color] != top_card[0][color]:
                        take_card(deck,player_cards,cards_taken)
                        return
            
                #Request
                for card in player_cards:
                    if card[1] == requested[0] or top_card[0][1] in ineffective:
                        play_card(move, top_card, who_played, player_cards)
                        print('Played')
                        return


                

            #DRAW TWO
            #########
            elif top_card[0][value] == "Draw Two":
                if who_played['USER'] == "Draw Two":
                    for i in range(2):
                        take_card(deck,player_cards,cards_taken)
                    top_card.append([top_card[0][0], "draw two"])
                    top_card.pop(0)
                    print('Took 2 Cards')
                    return

            #WILD
            #####
            elif top_card[0][value] == "Wild":
                if who_played["USER"] == "Wild":
                    while True:
                        answer = input("Declare colour: ... ")
                        if answer in colors:
                            break
                        else:
                            print("Invalid colour, choose 'red, green, blue or yellow")
                            continue
                    requested.append(answer)
                    requested.pop(0)
                    top_card.append([top_card[0][0], "wild"])
                    top_card.pop(0)
                    print()
                    continue
                elif who_played["CPU"] == "Wild":
                    top_card.append([top_card[0][0], "wild"])
                    top_card.pop(0)
                    continue

            #WILD DRAW FOUR
            ###############
            elif top_card[0][1] == "Wild Draw 4":
                if who_played["USER"] == "Wild Draw 4":
                    while True:
                        answer = input("Declare colour: ... ")
                        if answer in colors:
                            break
                        else:
                            print("Invalid colour, choose 'red, green, blue or yellow")
                            continue
                    requested.append(answer)
                    requested.pop(0)
                    top_card.append([top_card[0][0], "wild draw 4"])
                    top_card.pop(0)
                    print()
                    print(f"CPU is asking for {requested}")
                    continue
                elif who_played["CPU"] == "Wild Draw 4":
                    top_card.append([top_card[0][0], "wild draw 4"])
                    top_card.pop(0)
                    continue      
