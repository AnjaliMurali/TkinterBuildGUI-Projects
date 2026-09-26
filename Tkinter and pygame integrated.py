import tkinter as tk
import pygame
import sys

# ---------------- TKINTER INPUT ----------------

player_name = ""

def start_game():
    global player_name
    player_name = entry.get()
    root.destroy()   # Close tkinter window

root = tk.Tk()
root.title("Enter Player Name")

tk.Label(root, text="Player Name:").pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Start Game", command=start_game).pack(pady=10)

root.mainloop()

# ---------------- PYGAME GAME ----------------

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame with Tkinter Input")

font = pygame.font.SysFont(None, 48)

running = True

while running:
    screen.fill((30, 30, 30))

    # Display player name
    text = font.render(f"Player: {player_name}", True, (255, 255, 255))
    screen.blit(text, (200, 250))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()