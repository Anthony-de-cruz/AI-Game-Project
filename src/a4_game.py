#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

@author: A23 (100385770, 100428908, 100357095)
@date:   24/10/2025
"""

# a4_game.py

from a1_state import State
from a3_agent import Agent

def play(state: State, agentA: Agent | None, agentB: Agent | None) -> str | None:
    """
    Simulates a full Hinger game between two players (Agent or human)
    
    Parameters
    ----------
    state : State
        Initial game board
    agentA : Agent | None
        First player (None = human)
    agentB : Agent | None
        Second player (
    Returns
    -------
    str | None
        Name of the winner, or None if the game ends in a draw.
    """

    # Start game
    print("=== HINGER GAME START ===")
    print("Initial board:\n")
    print(state)

    current = state
    current_agent = agentA
    other_agent = agentB
    turn = 1

    while True:
        print(f"\n--- Turn {turn} ---")
        print(f"Current player: {current_agent.name if current_agent else 'Human A' if current_agent is agentA else 'Human B'}")
        print(current)

        if current_agent is None:
            # if human
            try:
                row = int(input("Enter row index: "))
                col = int(input("Enter column index: "))
                # Validate move
                if not (0 <= row < len(current.grid) and 0 <= col < len(current.grid[0])):
                    print("Invalid cell coordinates! Out of bounds.")
                    print(f"{other_agent.name if other_agent else 'Human'} wins by default.")
                    return other_agent.name if other_agent else "Human"
                if current.grid[row][col] <= 0:
                    print("Invalid move! Cell is empty.")
                    print(f"{other_agent.name if other_agent else 'Human'} wins by default.")
                    return other_agent.name if other_agent else "Human"

                new_grid = current.clone()
                new_grid[row][col] -= 1
                next_state = State(new_grid)

            except ValueError:
                print("Invalid input! Must be integers.")
                print(f"{other_agent.name if other_agent else 'Human'} wins by default.")
                return other_agent.name if other_agent else "Human"

        else:
            # Agent’s turn
            next_state = current_agent.move(current, mode="minimax")
            if next_state is None:
                print("Agent failed to produce a valid move.")
                print(f"{other_agent.name if other_agent else 'Human'} wins by default.")
                return other_agent.name if other_agent else "Human"

        # Check if game over or hinger made
        if next_state.numHingers() > 0:
            print("\nHinger Created!")
            print(next_state)
            print(f"Winner: {other_agent.name if other_agent else 'Human'}")
            return other_agent.name if other_agent else "Human"

        if not any(next_state.moves()):
            print("\nNo more moves available — Draw!")
            print(next_state)
            return None

        # Go to next turn
        current = next_state
        current_agent, other_agent = other_agent, current_agent
        turn += 1



def tester():
    grid = [
        [0, 0, 0],
        [2, 0, 1],
        [0, 0, 0]
    ]

    state = State(grid)
    agentA = Agent((3, 3), name="Alpha")
    agentB = Agent((3, 3), name="Beta")

    winner = play(state, agentA, agentB)
    if winner:
        print(f"\n=== Game Over! Winner: {winner} ===")
    else:
        print("\n=== Game Over! It's a Draw ===")


if __name__ == "__main__":
    tester()
