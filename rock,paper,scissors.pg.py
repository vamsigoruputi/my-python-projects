import random
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])
def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "player"
    else:
        return "computer"
def play_game():
    print("Welcome to Rock-Paper-Scissors! Type 'quit' to exit.")
    while True:
        player_choice = input("\nEnter rock, paper, or scissors: ").lower().strip()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        winner = get_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
        else:
            print("Computer wins!")
if __name__ == "__main__":
    play_game()
