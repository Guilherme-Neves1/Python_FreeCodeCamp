# Guess_number

import sys
import random
from enum import Enum

def guess_number(name='PlayerOne'):
  game_count = 0
  player_wins = 0
  python_wins = 0
  wins_percent = 0

  def play_guess_number():
    nonlocal name
    nonlocal player_wins
    nonlocal python_wins
    nonlocal wins_percent
    
    class GN(Enum):
      NUMBERONE = 1
      NUMBERTWO = 2
      NUMBERTHREE = 3
      
    playerchoice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3:\n\n")

    if playerchoice not in ["1", "2", "3"]:
      print(f"{name}, please enter 1, 2, or 3.")
      return play_guess_number()

    player = int(playerchoice)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print(f"\n{name}, you chose {str(GN(player)).replace('GN', '').title()}.")
    print(
      f"I was thinking about the number {str(GN(computer)).replace('GN', '').title()}.\n"
    )

    def decide_winner(player, computer):
      nonlocal name
      nonlocal player_wins
      nonlocal python_wins
      nonlocal wins_percent

      if player == 1 and computer == 3:
        player_wins += 1
        wins_percent += 1
        return f"🎉 {name}, you win!"
      elif player == 2 and computer == 1:
        player_wins += 1
        wins_percent += 1
        return f"🎉 {name}, you win!"
      elif player == 3 and computer == 2:
        player_wins += 1
        wins_percent += 1
        return f"🎉 {name}, you win!"
      elif player == computer:
        return "⚔ Tie game!"
      else:
        python_wins += 1
        return f"Sorry, {name}. Better luck next time. 🤖"

    game_result =  (player, computer)

    print(game_result)

    nonlocal game_count
    game_count += 1

    print(f"\nGame count: {game_count}")
    print(f"\n{name}'s wins: {player_wins}")
    print(f"\nYour winning percentage: {wins_percent:.2%}")

    print(f"\nPlay again, {name}?")

    while True:
      playagain = input("\nY for Yes or\nQ to Quit\n")
      if playagain.lower() not in ["y", "q"]:
        continue
      else:
        break

    if playagain.lower() == "y":
      return play_guess_number()
    else:
      print("\n🎉🎉🎉🎉")
      print("Thank you for playing!\n")
      sys.exit(f"Bye, {name}! 👋")

  return play_guess_number()

if __name__ == "__main__":
  import argparse

  parser = argparse.ArgumentParser(
    description="Provides a personalized game experience."
  )

  parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name of the person playing the game."
  )

  args = parser.parse_args()

  start = guess_number(args.name)
  start()

