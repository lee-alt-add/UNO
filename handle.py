#Handle

import random, time

numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'Skip','Skip','Draw Two','Draw Two','Reverse','Reverse']
colors = ['red', 'yellow', 'green', 'blue']
others = [[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4']]
deck = [[color,number] for color in colors for number in numbers] + others
random.shuffle(deck)

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
        self.inhand = [card for ind, card in enumerate(deck) if ind < 7]
        removing4rmDeck = [deck.remove(card) for card in self.inhand]
        return self.inhand

    #TOP CARD - The card at top of discard pile.
    def top_card(self):
        self.top_card = [[random.choice(colors), random.choice(range(10))]]
        removing4rmDeck = deck.remove(self.top_card[0])
        return self.top_card

    #VIEW the Top Card
    def top_card_view(self, top_card):
        print('         Top Card            ')
        print('=============================')
        print(f"        {self.top_card[0][0]}: '{self.top_card[0][1]}'        ")
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
    def PLAY_user(self):
        self.dealer()
        user_cards, cpu_cards = self.hand(), self.hand()
        top_card = self.top_card()

        def play_card(card, top_card, player_cards):
            player_cards.remove(card)
            top_card.append(card)
            top_card.pop(0)
            
        def take_card(player_cards, deck):
            player_cards.append(deck[0])
            deck.remove(deck[0])

        def wild_card(top_card, player_cards, declared_color):
            matches = []
            #WILDS
            if top_card[1] == "Wild":
                matches = [card for card in player_cards if card[0] == declared_color]
                if matches == []:
                    take_card(player_cards, deck)
            #WILD DRAW 4
            elif top_card[1] == "Wild Draw 4":
                matches = [card for card in player_cards if card[0] == declared_color]
                if matches == []:
                    for i in range(4):
                        take_card(player_cards, deck)
                        print("Took 4 cards")
            return matches
            
            
        
        #USER
        while True:
            #NORMAL play
            move = int(input("Card Number: ... "))
            if move < 0 or move > len(user_cards):
                print("Invalid choice, try again")
                continue
                    
            elif top_card[0][0] != user_cards[move-1][0] or top_card[0][1] != user_cards[move-1][1]:
                print("Card unplayable, Try a different card or draw if you don't have one")
                continue
            elif move == 0:
                take_card(user_cards, deck)
                
            elif top_card[0][0] == user_cards[move-1][0] or top_card[0][1] == user_cards[move-1][1] or top_card[0][color] == 0:
                play_card(wild_list[0], top_card, user_cards)
                if top_card[0][1] in ["Reverse", "Skip"]:
                    continue 
            #DRAW TWO
            elif top_card[0][1] == "Draw Two":
                for i in range(2):
                    take_card(user_cards, deck)
                    
            #WILD CARDS
            elif top_card[0][1] in ['Wild', 'Wild Draw 4']:
                cpu_choice = random.choice(colors)
                while True:
                    print(f"CPU: I want the color '{cpu_choice}'")
                    move int(input("Card Number: ... "))
                    if move not in range(1,len(user_cards)+1) or top_card[0][0] != user_cards[move-1]:
                        print('Error, pick a valid card')
                        continue
                    elif move == 0:
                        wild_card(top_card, player_cards, user_cards[move-1][0])
                        break
                    else:
                        play_card(card, top_card, user_cards[move-1])
                        break

            #CPU
            ####
            while True:
                cards_matching = [card for card in user_cards for identity in card if identity in top_card[0]]
        
        
        
                
        
        
        
    


        #NORMAL MOVE
        ############
        while True:
            color, value = 0,1

            if top_card[0][value] not in ["Draw Two",'Wild Draw 4',"Wild"]:

                #Wild Draw 4
                for card in player_cards:
                    if top_card[0][1] == "wild draw 4" and who_played["USER"]:
                            for i in range(4):
                                take_card(player_cards, deck)
                            return
                #Wild
                for card in player_cards:
                    if top_card[0][1] == "wild" and who_played["USER"]:
                        take_card(player_cards, deck)
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
                        take_card(player_cards, deck)
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
                        take_card(player_cards, deck)
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

            
    
                

game = cards()
game.dealer()
user_cards = game.hand()
cpu_cards = game.hand()
top_card = game.top_card()
print()
print()
game.top_card_view(top_card)
print(len(deck))
print()
print()
game.view(user_cards)
print(f"CPU cards: {len(cpu_cards)}")
print("Enter '0' to draw or pick a card number above to play")
while True:
    
    if len(user_cards) == 0:
        print("Hooray, YOU WON!!")
        break
    elif len(cpu_cards) == 0:
        print("Ooopps! YOU LOSE!")
        break
    
    game.PLAY_user(user_cards, top_card, who_played)
    game.PLAY_cpu(cpu_cards, top_card, who_played)
    game.top_card_view(top_card)
    game.view(user_cards)
    print(len(deck))
    print(f"CPU cards: {len(cpu_cards)}")










        
