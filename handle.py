#Handle

import random, time

numbers = [0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,'Skip','Skip','Draw Two','Draw Two','Reverse','Reverse']
colors = ['red', 'yellow', 'green', 'blue']
others = [[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4'],[0,'Wild'], [0,'Wild Draw 4']]
deck = [[color,number] for color in colors for number in numbers] + others
random.shuffle(deck)


    

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
        self.inhand = [card for ind, card in enumerate(deck) if ind < 1]
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
        print('')
        print('')
        print('')
        print('')

    #VIEW the User Cards
    def view(self, user_cards):
        self.user_cards = user_cards
        print('=        Your Cards         =')
        print('=___________________________=')
        
        for num in range(len(user_cards)):
            print(f"= {num+1}. {user_cards[num][0]}: '{user_cards[num][1]}'")
        print('=___________________________=')
        print('')

        
    #PLAY - The game being played.
    def PLAY_Game(self):
        top_card = self.top_card()
        user_cards, cpu_cards = self.hand(), self.hand()

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
            if top_card[0][1] == "Wild":
                matches = [card for card in player_cards if card[0] == declared_color]
                if matches == []:
                    take_card(player_cards, deck)
            #WILD DRAW 4
            elif top_card[0][1] == "Wild Draw 4":
                matches = [card for card in player_cards if card[0] == declared_color]
                if matches == []:
                    for i in range(4):
                        take_card(player_cards, deck)
                        print("Took 4 cards")
            return matches
            
            
        
        #USER
        def PLAY_user(top_card,user_cards,deck):
            #WILD CARDS
            if top_card[0][1] in ['Wild', 'Wild Draw 4']:
                cpu_choice = random.choice(colors)
                while True:
                    print(f"CPU: I want the color '{cpu_choice}'")
                    move = int(input("Card Number: ... "))
                    if move == 0:
                        wild_card(top_card, user_cards, cpu_choice)
                        top_card.append([0, top_card[0][1].lower()])
                        top_card.pop(0)
                        print("Card withdrawn!")
                        return
                    try:
                        
                        if cpu_choice == user_cards[move-1][0]:
                            play_card(user_cards[move-1], top_card, user_cards)
                            return
                    except Exception:
                        print('Error, pick a valid card')
                        continue

            #DRAW TWO
            if top_card[0][1] == "Draw Two":
                input("CPU played 'Draw Two' Press any button to draw the cards: ... ")
                for i in range(2):
                    take_card(user_cards, deck)
                top_card.append([top_card[0][0], top_card[0][1].lower()])
                top_card.pop(0)
                return
                                
                    
            #NORMAL play
            while True:
                try:
                    move = int(input("Card Number: ... "))
                except Exception:
                    print("Invalid choice, try again")
                    continue

                if move == 0:
                    take_card(user_cards, deck)
                    print('took')
                    return

                elif top_card[0][0] == user_cards[move-1][0] or top_card[0][1] == user_cards[move-1][1] or user_cards[move-1][0] == 0 or top_card[0][1] in ['wild', 'wild draw 4']:
                    play_card(user_cards[move-1], top_card, user_cards)
                    print('played')
                    if top_card[0][1] in ["Reverse", "Skip"]:
                        print(f"Played a {top_card[0][1]} card, playing again")
                        continue
                    else:
                        return
                
                elif top_card[0][0] != user_cards[move-1][0] and top_card[0][1] != user_cards[move-1][1]:
                    print("Card unplayable, Try a different card or draw if you don't have one")
                    continue
                
                    
                
            
            

        #CPU
        ####
        def PLAY_cpu(top_card,cpu_cards,deck):
            while True:
                #WILD cards
                if top_card[0][1] == "Wild" or top_card[0][1] == "Wild Draw 4":
                    while True:
                        declared_color = input("Pick a color: ... ")
                        if declared_color in colors:
                            break
                        print("Invalid color name")
                    
                    for card in cpu_cards:
                        if card[0] == declared_color:
                            play_card(card, top_card, cpu_cards)
                            print("Played")
                            return
                        elif cpu_cards[-1] == card:
                            wild_card(top_card, cpu_cards, declared_color)
                            top_card.append([0, top_card[0][1].lower()])
                            top_card.pop(0)
                            return

                #DRAW TWO
                elif top_card[0][1] == "Draw Two":
                    for i in range(2):
                        take_card(cpu_cards, deck)
                    top_card.append([top_card[0][0], top_card[0][1].lower()])
                    top_card.pop(0)
                    print("Took")
                    return

                #NORMAL cards
                while True:
                    for card in cpu_cards:
                        if card[0] == top_card[0][0] or card[1] == top_card[0][1] or 0 in cpu_cards[0] or top_card[0][0] == 0:
                            play_card(card, top_card, cpu_cards)
                            break
                        elif cpu_cards[-1] == card:
                            take_card(cpu_cards, deck)
                            return
                    if top_card[0][1] == "Skip" or top_card[0][1] == "Reverse":
                        print(f"I played {top_card[0][1]}, so I will play again")
                        continue
                    else:
                        return


        while True:
            self.top_card_view(top_card)
            self.view(user_cards)
            print(f"The CPU has {len(cpu_cards)} card(s)")
            PLAY_user(top_card,user_cards,deck)
            if len(user_cards) == 0:
                print("Hooray! YOU WIN!!")
                return
            PLAY_cpu(top_card,cpu_cards,deck)
            if len(cpu_cards) == 0:
                print("Ooops! YOU LOSE!")
                return

game = cards()
game.PLAY_Game()










        
