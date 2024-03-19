# import random
# import pygame

# class Card:
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
#         self.image = pygame.image.load(f'cards/{self.rank.lower()}_of_{self.suit.lower()}.png')
        
#     def draw(self, surface, pos):
#         surface.blit(self.image, pos)
        
#     def __repr__(self):
#         return f"{self.rank} of {self.suit}"

# class Deck:
#     suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
#     ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    
#     def __init__(self,num_decks=1):
#         self.num_decks = num_decks
#         self.cards = []
#         self.shuffle()
        
#     def shuffle(self):
#         for suit in self.suits:
#             for rank in self.ranks:
#                 self.cards = [Card(suit, rank)]
#         random.shuffle(self.cards)

#     def deal(self):
#         if len(self.cards) < 20 * self.num_decks:  # Arbitrary threshold to reshuffle
#             self.shuffle()
#         return self.cards.pop()
    
# class BlackjackGame:
#     def __init__(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode((800, 600))
#         pygame.display.set_caption('Blackjack')
#         self.setup()
    
#     def setup(self):
#         self.deck = Deck()
#         self.player_hand = []
#         self.dealer_hand = []
#         self.game_over = False
#         self.deal_initial_cards()
        
#     def run(self):
#         while not self.game_over:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.game_over = True
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_h:  # Hit
#                         self.player_action()
#                     elif event.key == pygame.K_s:  # Stand
#                         self.dealer_action()
#                         self.game_over = True  # End game after dealer's turn

#             self.screen.fill((0, 122, 0))  # Table green
#             self.show_hands_pygame()
#             pygame.display.flip()
#             self.clock.tick(60)

#         pygame.quit()

#     def deal_initial_cards(self):
#         self.player_hand.append(self.deck.deal())
#         self.dealer_hand.append(self.deck.deal())
#         self.player_hand.append(self.deck.deal())
#         self.dealer_hand.append(self.deck.deal())
    
#     def show_hands(self, reveal_dealer=False):
#         def format_card_display(card):
#             rank_display_map = {
#                 'Jack': 'J', 'Queen': 'Q', 'King': 'K', 'Ace': 'A',
#                 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5', 
#                 'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9', 'Ten': '10'
#             }
#             return rank_display_map[card.rank]
        
#         player_hand_ranks = [format_card_display(card) for card in self.player_hand]
#         dealer_hand_ranks = [format_card_display(card) for card in self.dealer_hand]

#         print("Your Hand:", ', '.join(player_hand_ranks))
#         if reveal_dealer:
#             print("Dealer's Hand:", ', '.join(dealer_hand_ranks))
#         else:
#             print("Dealer's Hand: ", dealer_hand_ranks[0], ", ? ")
            
#     def get_hand_value(self, hand):
#         value = 0
#         aces = 0
#         rank_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        
#         for card in hand:
#             if card.rank in ['Jack', 'Queen', 'King']:
#                 value += 10
#             elif card.rank == 'Ace':
#                 aces += 1
#                 value += 11
#             else:
#                 value += rank_values[card.rank]
                
#         while value > 21 and aces:
#             value -= 10
#             aces -= 1
#         return value
                
#     def player_action(self):
#         while True:
#             action = input("(H)it or (S)tand? ").lower()
#             if action == 'h':
#                 new_card = self.deck.deal()
#                 self.player_hand.append(new_card)

#                 if self.get_hand_value(self.player_hand) > 21:
#                     print("Bust! You lose.")
#                     self.game_over = True
#                     return
#             elif action == 's':
#                 break
#             else:
#                 print("Invalid input, please choose '(H)it' or '(S)tand'.")
                
#     def dealer_action(self):
#         while self.get_hand_value(self.dealer_hand) < 17:
#             self.dealer_hand.append(self.deck.deal())
#         self.show_hands(reveal_dealer=True)
    
#         if self.get_hand_value(self.dealer_hand) > 21:
#             print("Dealer busts! You win!")
#         elif self.get_hand_value(self.dealer_hand) < self.get_hand_value(self.player_hand):
#             print("You win!")
#         elif self.get_hand_value(self.dealer_hand) > self.get_hand_value(self.player_hand):
#             print("Dealer wins!")
#         else:
#             print("It's a tie!")
        
#     def play(self):
#         self.setup
        
#         self.deal_initial_cards()
#         self.show_hands()
#         if not self.game_over:
#             self.player_action()
#         if not self.game_over:
#             self.dealer_action()

# def main():
#     num_decks = 6
#     decks = Deck(num_decks)
#     while True:
#         game = BlackjackGame()
#         game.play()

#         replay = input("Do you want to play again? (y/n): ").lower()
#         if replay != 'y':
#             print("Thanks for playing!")
#             break

# if __name__ == "__main__":
#     main()

lass Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self,num_decks=1):
        self.num_decks = num_decks
        self.cards = []
        self.shuffle()
        
    def shuffle(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards = [Card(suit, rank)]
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) < 20 * self.num_decks:  # Arbitrary threshold to reshuffle
            self.shuffle()
        return self.cards.pop()
    
class BlackjackGame:
    def __init__(self):
        self.setup()
    
    def setup(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False

    def deal_initial_cards(self):
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())
    
    def show_hands(self, reveal_dealer=False):
        def format_card_display(card):
            rank_display_map = {
                'Jack': 'J', 'Queen': 'Q', 'King': 'K', 'Ace': 'A',
                'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5', 
                'Six': '6', 'Seven': '7', 'Eight': '8', 'Nine': '9', 'Ten': '10'
            }
            return rank_display_map[card.rank]
        
        player_hand_ranks = [format_card_display(card) for card in self.player_hand]
        dealer_hand_ranks = [format_card_display(card) for card in self.dealer_hand]

        print("Your Hand:", ', '.join(player_hand_ranks))
        if reveal_dealer:
            print("Dealer's Hand:", ', '.join(dealer_hand_ranks))
        else:
            print("Dealer's Hand: ", dealer_hand_ranks[0], ", ? ")
            
    def get_hand_value(self, hand):
        value = 0
        aces = 0
        rank_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        
        for card in hand:
            if card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                aces += 1
                value += 11
            else:
                value += rank_values[card.rank]
                
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
                
    def player_action(self):
        while True:
            action = input("(H)it or (S)tand? ").lower()
            if action == 'h':
                new_card = self.deck.deal()
                self.player_hand.append(new_card)

                if self.get_hand_value(self.player_hand) > 21:
                    print("Bust! You lose.")
                    self.game_over = True
                    return
            elif action == 's':
                break
            else:
                print("Invalid input, please choose '(H)it' or '(S)tand'.")
                
    def dealer_action(self):
        while self.get_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.deal())
        self.show_hands(reveal_dealer=True)
    
        if self.get_hand_value(self.dealer_hand) > 21:
            print("Dealer busts! You win!")
        elif self.get_hand_value(self.dealer_hand) < self.get_hand_value(self.player_hand):
            print("You win!")
        elif self.get_hand_value(self.dealer_hand) > self.get_hand_value(self.player_hand):
            print("Dealer wins!")
        else:
            print("It's a tie!")
        
    def play(self):
        self.setup
        
        self.deal_initial_cards()
        self.show_hands()
        if not self.game_over:
            self.player_action()
        if not self.game_over:
            self.dealer_action()

def main():
    num_decks = 6
    decks = Deck(num_decks)
    while True:
        game = BlackjackGame()
        game.play()

        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()