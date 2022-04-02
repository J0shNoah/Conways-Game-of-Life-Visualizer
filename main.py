import pygame
from settings import Cell
from GoL_Func import Board

pygame.init()

display_height = 700
tile_size = display_height // 50
display_width = 50 * tile_size

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

n = 50
m = 50

# Add cells to the Cell class
cells = []
for i, row in enumerate(range(n)):
    for j, col in enumerate(range(m)):
        print(i, j)
        cell = Cell(tile_size, col_index=j, row_index=i)
        cells.append(cell)


board = Board(cells, 50, 50)

# simulation loop
count = 0
while True:
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in cells:
                    i.status = 0
                    i.color = "white"
                board.simulate = False
                print("Reset")
            elif event.key == pygame.K_UP:
                board.simulate = True
                print("Simulate")
            elif event.key == pygame.K_DOWN:
                board.simulate = False
                print("Stop")

    screen.fill("black")
    board.draw(screen)

    pygame.display.update()
    clock.tick(15)
