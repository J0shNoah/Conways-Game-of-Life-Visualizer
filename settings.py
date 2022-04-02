import pygame


class Cell:
    def __init__(self, tile_size, col_index, row_index):
        self.rect = pygame.Rect((col_index * tile_size + 0.5, row_index * tile_size + 0.5),
                                (tile_size - 1, tile_size - 1))
        self.status = 0
        self.color = "white"
        self.col_index = col_index
        self.row_index = row_index
        self.simulate = False

    def drawing_grid(self, array):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
            self.status = 1
            self.color = "black"
        elif self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[2]:
            self.status = 0
            self.color = "white"

        if self.status == 1:
            array[self.row_index][self.col_index] = 1
        elif self.status == 0:
            array[self.row_index][self.col_index] = 0

    def update_self(self, array):
        if array[self.row_index][self.col_index] == 1:
            self.status = 1
            self.color = "black"
        elif array[self.row_index][self.col_index] == 0:
            self.status = 0
            self.color = "white"
