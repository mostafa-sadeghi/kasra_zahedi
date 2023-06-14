# for i in range(10):
#     print(i, end=' ')
# for i in range(10, 0, -1):
#     print(i, end=' ')

# i = 0
# while i < 10:
#     print(i, end=' ')
#     i = i + 1  # i += 1


# i = 9
# while i >= 0:
#     print(i, end=' ')
#     i -= 1

# for number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(number)

# for s in 'kasra':
#     print(s, end=' ')


# for i in range(3):
#     print("a")
# for j in range(3):
#     print("b")

# for i in range(3):
#     print("a")
#     for j in range(3):
#         print("b")

import random

# for i in range(10):
#     random_number = random.randrange(100,151)
#     print(random_number)
ACTIONS = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0
print('Game started...')

while True:
    print('"0" => "rock", "1" => "paper", "2" => "scissors" ')
    player_selection = input('> ')
    player_hand = ACTIONS[int(player_selection)]
    computer_hand = random.choice(ACTIONS)

    if player_hand == 'paper' and computer_hand == 'rock':
        player_score += 1
        print("player wins")
        print("player's hand:", player_hand)
        print("computer's hand:", computer_hand)
        print(f"{'PLAYER':<10}{'SCORE':>10}")
        print(f"{'ME':<10}{player_score:>10}")
        print(f"{'COMPUTER':<10}{computer_score:>10}")
    elif player_hand == 'rock' and computer_hand == 'scissors':
        player_score += 1
        print("player wins")
        print("player's hand:", player_hand)
        print("computer's hand:", computer_hand)
        print(f"{'PLAYER':<10}{'SCORE':>10}")
        print(f"{'ME':<10}{player_score:>10}")
        print(f"{'COMPUTER':<10}{computer_score:>10}")
    elif player_hand == 'scissors' and computer_hand == 'paper':
        player_score += 1
        print("player wins")
        print("player's hand:", player_hand)
        print("computer's hand:", computer_hand)
        print(f"{'PLAYER':<10}{'SCORE':>10}")
        print(f"{'ME':<10}{player_score:>10}")
        print(f"{'COMPUTER':<10}{computer_score:>10}")

    elif player_hand == 'rock' and computer_hand == 'paper':
        computer_score += 1
        print("computer wins")
        print("player's hand:", player_hand)
        print("computer's hand:", computer_hand)
        print(f"{'PLAYER':<10}{'SCORE':>10}")
        print(f"{'ME':<10}{player_score:>10}")
        print(f"{'COMPUTER':<10}{computer_score:>10}")
    elif player_hand == 'scissors' and computer_hand == 'rock':
        computer_score += 1
        print("computer wins")
        print("player's hand:", player_hand)
        print("computer's hand:", computer_hand)
        print(f"{'PLAYER':<10}{'SCORE':>10}")
        print(f"{'ME':<10}{player_score:>10}")
        print(f"{'COMPUTER':<10}{computer_score:>10}")
    elif player_hand == 'paper' and computer_hand == 'scissors':
        computer_score += 1
        print("computer wins")
        print("player's hand:", player_hand)
        print("computer's hand:", computer_hand)
        print(f"{'PLAYER':<10}{'SCORE':>10}")
        print(f"{'ME':<10}{player_score:>10}")
        print(f"{'COMPUTER':<10}{computer_score:>10}")

    else:
        print("EQUAL")
        print("player's hand:", player_hand)
        print("computer's hand:", computer_hand)
        print(f"{'PLAYER':<10}{'SCORE':>10}")
        print(f"{'ME':<10}{player_score:>10}")
        print(f"{'COMPUTER':<10}{computer_score:>10}")

    print("Do you want to continue?(y or n)")
    if input('> ').lower().startswith('n'):
        print('Thank you for playing...')
        break
