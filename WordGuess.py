import random
from enum import Enum

class GameStatus(Enum):
    VICTORY = "Victory"
    KEEP_GUESSING = "Defeat"
    INVALID_INPUT = "Invalid Input"

class WordGuess:
    def __init__(self, valid_words, target_word):
        self.valid_words = valid_words
        self.target_word = target_word
        
    def create_hint(self, guess):
        remaining_letters = list(self.target_word)
        
        hint = []
        
        for i, letter in enumerate(guess):
            if letter == self.target_word[i]:
                hint.append('1')
            elif letter in self.target_word:
                hint.append('0')
            else:
                hint.append('-')
        return hint
                
        
    
    def evulate_guess(self, guess):
        if len(guess) != len(self.target_word):
            print(f"Words must have {len(self.target_word)} characters")
            return GameStatus.INVALID_INPUT
        elif guess not in self.valid_words:
            print("Word must exist in the list")
            return GameStatus.INVALID_INPUT
        elif guess == self.target_word:
            print("CONGRATS YOU GUESSED IT RIGHT")
            return GameStatus.VICTORY
        else:
            print(self.create_hint(guess))
            return GameStatus.KEEP_GUESSING
    
        
    
def play_word_game():
    word_list = ["able", "bell", "boss", "cast", "cash", "knot", "note", "near", "over", "salt", "wood"]
    
    chosen_word = random.choice(list(word_list))
    max_attempt = 5
    
    # game start
    game = WordGuess(word_list, chosen_word)
    
    def take_turn(round_number):
        if round_number > max_attempt:
            print("Out of attempts, do better next time!")
            return
        else:
            user_guess = input(f"Attempt {round_number}. Take your guess:\n")
            outcome = game.evulate_guess(user_guess)
            
            if outcome == GameStatus.VICTORY:
                print("YOU WIN")
            elif outcome == GameStatus.KEEP_GUESSING:
                take_turn(round_number + 1)
            elif outcome == GameStatus.INVALID_INPUT:
                take_turn(round_number)  
            
    
    # first turn
    
    # Take in user guess
    
    # create hint
    
    # round incremnt
    
    # win or lose (5 rounds)
    
    take_turn(1)
    
    
if __name__ == "__main__":
    play_word_game()