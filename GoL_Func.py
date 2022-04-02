import pygame


class Board:
    def __init__(self, cells, n, m):
        self.cells = cells
        self.simulate = False
        self.n = n
        self.m = m
        self.array = self.generate_array()

    def update_array(self):
        new_array = self.generate_array()
        # makes the new array and assigns the 1's based on GoL rules.
        for cell in self.cells:
            count = self.neighbours(cell)
            # if 1 < count <= 3 and cell.status == 1:
            if 3 >= count > 1 == cell.status:
                new_array[cell.row_index][cell.col_index] = 1
                cell.color = "black"
            elif count == 3 and cell.status == 0:
                cell.status = 1
                new_array[cell.row_index][cell.col_index] = 1
                cell.color = "black"
        # New array created so this updates the status of the cells that are now 0 in the new array.

        for cell in self.cells:
            if new_array[cell.row_index][cell.col_index] == 0:
                cell.status = 0
                cell.color = "white"
        self.array = new_array

    # Finds all the neighbours for each cell.
    def neighbours(self, cell):
        x = cell.col_index
        y = cell.row_index
        if cell.status == 1:
            count_nbs = -1
        else:
            count_nbs = 0
        for i in range(-1, 2):
            if y + i > self.n - 1:
                y = -1
            for j in range(-1, 2):
                if x + j > self.m - 1:
                    x = -1
                if self.array[y + i][x + j] == 1:
                    count_nbs += 1
        return count_nbs

    # This creates a new array of zeros with the same dimensions as the last array.
    def generate_array(self):
        new_array = []
        for i in range(self.n):
            array_row = []
            for j in range(self.m):
                array_row.append(0)
            new_array.append(array_row)
        return new_array

    def draw(self, surface):
        for cell in self.cells:
            pygame.draw.rect(surface, cell.color, cell.rect)
            cell.drawing_grid(self.array)

        if self.simulate:
            self.update_array()
