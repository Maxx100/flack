import pygame


class Menu:
    def __init__(self):
        pass

    def main(self):
        pass


class Board:
    def __init__(self, figures):
        self.figures = figures
        self.width = 8
        self.height = 8
        self.left = 10
        self.top = 10
        self.cell_size = 85

    def render(self):
        screen.fill(pygame.Color("yellow"))
        for j in range(self.height):
            for i in range(self.width):
                pygame.draw.rect(screen, pygame.Color("white"), (i * self.cell_size + self.top,
                                                                 j * self.cell_size + self.left,
                                                                 self.cell_size,
                                                                 self.cell_size), 1)
        for i in self.figures:
            temp = i.return_data()
            if temp[0] == "w":
                r = "white"
            else:
                r = "black"
            pygame.draw.circle(screen, pygame.Color(r), ((temp[1] % 8) * self.cell_size +
                                                             self.top + self.cell_size // 2,
                                                             (temp[1] - 1) // 8 * self.cell_size +
                                                             self.left + self.cell_size // 2),
                               self.cell_size // 2)


class Checker:
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord

    def return_data(self):
        return self.color, self.coord


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Checkers")
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    arr = []
    for k in range(1, 8, 2):
        arr.append(Checker("w", k))
        arr.append(Checker("w", k + 9))
        arr.append(Checker("w", k + 16))

        arr.append(Checker("b", k + 41))
        arr.append(Checker("b", k + 48))
        arr.append(Checker("b", k + 57))
    board = Board(arr)
    board.render()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
