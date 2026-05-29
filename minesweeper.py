import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
ROWS = 10
COLS = 10
CELL_SIZE = 50
MINES = 15

WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE + 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Clock
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
DARK_GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 150, 0)

# Font
font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 22)

# Board setup
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]

# Place mines
mine_positions = random.sample(range(ROWS * COLS), MINES)

for pos in mine_positions:
    row = pos // COLS
    col = pos % COLS
    board[row][col] = -1

# Calculate numbers
for row in range(ROWS):
    for col in range(COLS):
        if board[row][col] == -1:
            continue

        count = 0

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if board[nr][nc] == -1:
                        count += 1

        board[row][col] = count



def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if revealed[row][col]:
                pygame.draw.rect(screen, GRAY, rect)

                if board[row][col] == -1:
                    pygame.draw.circle(
                        screen,
                        RED,
                        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
                        12
                    )

                elif board[row][col] > 0:
                    text = font.render(str(board[row][col]), True, BLUE)
                    screen.blit(text, (x + 15, y + 10))

            else:
                pygame.draw.rect(screen, DARK_GRAY, rect)

                if flagged[row][col]:
                    flag_text = font.render("F", True, GREEN)
                    screen.blit(flag_text, (x + 15, y + 10))

            pygame.draw.rect(screen, BLACK, rect, 2)



def reveal_cells(row, col):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        return

    if revealed[row][col] or flagged[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    reveal_cells(row + dr, col + dc)



def check_win():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != -1 and not revealed[row][col]:
                return False

    return True



def game_over(message):
    # Reveal all mines
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == -1:
                revealed[row][col] = True

    draw_board()

    text = font.render(message, True, WHITE)

    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 60, WIDTH, 60))
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT - 45))

    pygame.display.update()
    pygame.time.delay(3000)

    pygame.quit()
    sys.exit()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            col = mouse_x // CELL_SIZE
            row = mouse_y // CELL_SIZE

            if row < ROWS:
                # Left click
                if event.button == 1:
                    if board[row][col] == -1:
                        game_over("GAME OVER")
                    else:
                        reveal_cells(row, col)

                # Right click
                elif event.button == 3:
                    if not revealed[row][col]:
                        flagged[row][col] = not flagged[row][col]

    # Win check
    if check_win():
        game_over("YOU WIN!")

    # Drawing
    screen.fill(BLACK)

    draw_board()

    info_text = small_font.render(
        "Left Click = Reveal | Right Click = Flag",
        True,
        WHITE
    )

    screen.blit(info_text, (10, HEIGHT - 40))

    pygame.display.update()
    clock.tick(60)
