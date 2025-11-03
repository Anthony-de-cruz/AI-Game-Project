"""
Hinger Project
Coursework 001 for: CMP-6058A Artificial Intelligence

@author: A23 (100385770, 100428908, 100357095)
@date:   19/10/2025
"""
import pygame
import sys
import time
from a1_state import State
from a3_agent import Agent

# CONFIG 
CELL_SIZE = 100
MARGIN = 5
FONT_SIZE = 40
BG_COLOR = (30, 30, 30)
ACTIVE_COLOR = (70, 200, 70)
EMPTY_COLOR = (80, 80, 80)
HINGER_COLOR = (255, 80, 80)
TEXT_COLOR = (255, 255, 255)
INFO_COLOR = (200, 200, 200)

def draw_grid(screen, state, font):
    """Draw the board grid and counters."""
    rows, cols = len(state.grid), len(state.grid[0])
    for i in range(rows):
        for j in range(cols):
            x = j * (CELL_SIZE + MARGIN)
            y = i * (CELL_SIZE + MARGIN)
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            val = state.grid[i][j]

            color = EMPTY_COLOR if val == 0 else ACTIVE_COLOR
            pygame.draw.rect(screen, color, rect)
            if val > 0:
                text = font.render(str(val), True, TEXT_COLOR)
                screen.blit(text, text.get_rect(center=rect.center))

def main():
    pygame.init()
    font = pygame.font.Font(None, FONT_SIZE)

    grid = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    state = State(grid)

    # Agents
    agentA = Agent((3, 3), name="Agent1")
    agentB = Agent((3, 3), name="Agent2")


    turnAgentType = "minimax"
    otherAgentType = "alphabeta"

    # Choose mode 
    # Options: "human_vs_human", "human_vs_ai", "ai_vs_ai"
    mode = "ai_vs_ai"

    rows, cols = len(grid), len(grid[0])
    width = cols * (CELL_SIZE + MARGIN)
    height = rows * (CELL_SIZE + MARGIN)
    screen = pygame.display.set_mode((width, height + 80))
    pygame.display.set_caption("Hinger Game")

    clock = pygame.time.Clock()
    running = True
    winner = None

    # Turn management
    human_turn = True          # True = Player 1's turn, False = Player 2 / AI turn
    turn_agent = agentA         # for AI vs AI
    other_agent = agentB

    while running:
        screen.fill(BG_COLOR)
        draw_grid(screen, state, font)

        # Info bar
        info_y = height + 10
        if winner:
            msg = font.render(f"{winner} wins!", True, HINGER_COLOR)
        elif all(c == 0 for row in state.grid for c in row):
            msg = font.render("Draw!", True, INFO_COLOR)
        else:
            if mode == "ai_vs_ai":
                msg = font.render(f"{turn_agent.name}'s turn", True, INFO_COLOR)
            elif mode == "human_vs_ai":
                msg = font.render("Your turn" if human_turn else f"{agentA.name}'s turn", True, INFO_COLOR)
            else:  # human_vs_human
                msg = font.render(f"Player {'1' if human_turn else '2'}'s turn", True, INFO_COLOR)
        screen.blit(msg, (10, info_y))
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #  Human move(s) 
            if mode in ["human_vs_human", "human_vs_ai"] and not winner and event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                if my < height:  # clicked inside board
                    j = mx // (CELL_SIZE + MARGIN)
                    i = my // (CELL_SIZE + MARGIN)
                    if 0 <= i < rows and 0 <= j < cols and state.grid[i][j] > 0:
                        next_state = State(state.clone())
                        next_state.grid[i][j] -= 1
                        
                        # Determine winner if removing a hinger
                        if next_state.numRegions() > state.numRegions():
                            if mode == "human_vs_human":
                                winner = "Player 1" if human_turn else "Player 2"
                            else:  # human_vs_ai
                                winner = "Human"
                        else:
                            if mode == "human_vs_human":
                                human_turn = not human_turn  # switch to next human player
                            else:
                                human_turn = False  # switch to AI
                        state = next_state

        # --- AI vs AI ---
        if mode == "ai_vs_ai" and not winner:
            next_state = turn_agent.move(state, mode = turnAgentType)
            if next_state:
                if next_state.numRegions() > state.numRegions():
                    winner = turn_agent.name
                else:
                    turn_agent, other_agent = other_agent, turn_agent
                    turnAgentType, otherAgentType = otherAgentType, turnAgentType
                state = next_state
            else:
                winner = other_agent.name
            pygame.display.flip()
            time.sleep(1.0)

        # --- AI turn in human_vs_ai ---
        elif mode == "human_vs_ai" and not human_turn and not winner:
            pygame.display.flip()
            time.sleep(0.8)
            next_state = turn_agent.move(state, mode= turnAgentType)
            if next_state:
                if next_state.numRegions() > state.numRegions():
                    winner = turn_agent.name
                else:
                    human_turn = True
                state = next_state
            else:
                winner = "Human"
            pygame.display.flip()
            time.sleep(1.0)

if __name__ == "__main__":
    main()
