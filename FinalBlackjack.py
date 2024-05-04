
from pickle import NONE
import random
import pygame

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image = pygame.image.load(f'C:/Users/luke/OneDrive/Documents/Visual Studio 2022/Projects/Blackjack/Cards/{self.rank.lower()}_of_{self.suit.lower()}.png')
        self.image = pygame.transform.scale(self.image, (100, 140))

    def draw(self, surface, pos):
        surface.blit(self.image, pos)
        
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = []
        self.shuffle()
        
    def shuffle(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks] * self.num_decks
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) < 20 * self.num_decks:  # Arbitrary threshold to reshuffle
            self.shuffle()
        return self.cards.pop()

class BlackjackGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1260, 720))
        pygame.display.set_caption('Blackjack')
        self.clock = pygame.time.Clock()
        
        self.setup()
    
    def setup(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        self.deal_initial_cards()
    
    def main_loop(self):
        while True:  # Keep the game running indefinitely
            self.setup()  # Reset the game state for a new hand
            self.deal_initial_cards()  # Deal initial cards for the new hand
            self.show_hands_pygame()

            while not self.game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return  # Exit the game loop and stop the program
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_h:  # Hit
                            self.player_action()
                        elif event.key == pygame.K_s:  # Stand
                            self.dealer_action()
                            if not self.game_over:
                                self.game_over = True  # End game after dealer's turn
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            return
                                
                    
                if not self.game_over:
                    self.show_hands_pygame()
                    pygame.display.flip()
                self.clock.tick(60)


    def display_outcome(self, win_text=None):
        # Display the outcome message for a few seconds before resetting the game
        font = pygame.font.Font(None, 36)
        text_surface = font.render(win_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()

        waiting_for_space = True
        while waiting_for_space:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # Exit the game completely
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting_for_space = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return  # Provide an option to quit the game


    def deal_initial_cards(self):
        self.player_hand = []
        self.dealer_hand = []
        
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())
        self.player_hand.append(self.deck.deal())
        self.dealer_hand.append(self.deck.deal())
        
        self.dealer_face_down = True
        
        if self.get_hand_value(self.player_hand) == 21:
           self.display_outcome("Blackjack! You win!")
           self.game_over = True
    
    def show_hands_pygame(self):
        self.screen.fill((0, 122, 0))
        player_card_pos = (100, 400)
        dealer_card_pos = (100, 100)
        
        for card in self.player_hand:
            card.draw(self.screen, player_card_pos)
            player_card_pos = (player_card_pos[0] + card.image.get_width() + 10, player_card_pos[1])
            
        for idx, card in enumerate(self.dealer_hand):
            if idx == 0 and self.dealer_face_down and not self.game_over:
                back_of_card_image = pygame.image.load('../cards/back_of_card.png')
                back_of_card_image = pygame.transform.scale(back_of_card_image, (100, 140))
                self.screen.blit(back_of_card_image, dealer_card_pos)
            else:
                card.draw(self.screen, dealer_card_pos)
            dealer_card_pos = (dealer_card_pos[0] + card.image.get_width() + 10, dealer_card_pos[1])

        pygame.display.flip()

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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_h]:  # Hit
            new_card = self.deck.deal()
            self.player_hand.append(new_card)

            if self.get_hand_value(self.player_hand) > 21:
                win_text = "Bust! You lose."
                self.display_outcome(win_text)
                self.game_over = True
        elif keys[pygame.K_s]:  # Stand
            self.dealer_action()
                
    def dealer_action(self):
        while self.get_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.deal())
        
        self.show_hands_pygame()
    
        player_value = self.get_hand_value(self.player_hand)
        dealer_value = self.get_hand_value(self.dealer_hand)
    
        if dealer_value > 21:
            win_text = "Dealer busts! You win!"
            
        elif dealer_value < player_value:
            win_text = "You win!"
            
        elif dealer_value > player_value:
            win_text = "Dealer wins! You lose."
            
        else:
            win_text = "It's a tie!"
        
        self.dealer_face_down = False  # Make sure dealer's cards are revealed
        self.show_hands_pygame()  # Update display to show all dealer's cards
        self.display_outcome(win_text)
        self.game_over = True

        pygame.display.flip()
        
    def play(self):
        self.setup()
        
        self.deal_initial_cards()
        self.show_hands_pygame()
        if not self.game_over:
            self.player_action()
        if not self.game_over:
            self.dealer_action()

def main():
    game = BlackjackGame()
    game.main_loop()

if __name__ == "__main__":
    main()
