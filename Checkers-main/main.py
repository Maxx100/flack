import pygame

SEQUENCE = "w"


class Menu:
    def __init__(self):
        pass

    def main(self):
        pass


class Board:
    def __init__(self):
        # Список фигур
        self.board_sq = []
        for i in range(64):
            self.board_sq.append(["e", 0])
        # e - empty | w - white | b - black
        # Клетки: 0 - пусто  1 - шашка  2 - шашка взята  3 - подсвет как возможный ход
        # Заполнение
        for k in range(0, 7, 2):
            self.board_sq[k] = ["w", 1]
            self.board_sq[k + 9] = ["w", 1]
            self.board_sq[k + 16] = ["w", 1]
            self.board_sq[k + 41] = ["b", 1]
            self.board_sq[k + 48] = ["b", 1]
            self.board_sq[k + 57] = ["b", 1]
        # Стандартные значения графики
        self.width = 8
        self.height = 8
        self.left = 10
        self.top = 10
        self.cell_size = 85

    # Рендер поля
    def render(self):
        # Фон
        screen.fill(pygame.Color("grey"))
        # Проход по всем клеткам и их отрисовка
        for j in range(self.height):
            for i in range(self.width):
                pygame.draw.rect(screen, pygame.Color("white"), (i * self.cell_size + self.top,
                                                                 j * self.cell_size + self.left,
                                                                 self.cell_size,
                                                                 self.cell_size), 1)

        for i in range(len(self.board_sq)):
            if self.board_sq[i][1] == 2:
                pygame.draw.rect(screen, pygame.Color("blue"), ((i % 8) * self.cell_size + self.top - 1,
                                                                i // 8 * self.cell_size + self.left - 1,
                                                                self.cell_size - 2,
                                                                self.cell_size - 2))
            elif self.board_sq[i][1] == 3:
                pygame.draw.circle(screen, pygame.Color("blue"), ((i % 8) * self.cell_size +
                                                                  self.top + self.cell_size // 2,
                                                                  i // 8 * self.cell_size +
                                                                  self.left + self.cell_size // 2), self.cell_size // 4)

        # Отрисовка фигур
        for i in range(len(self.board_sq)):
            if self.board_sq[i][1] in [1, 2]:
                if self.board_sq[i][0] == "w":
                    r = "white"
                else:
                    r = "black"
                pygame.draw.circle(screen, pygame.Color(r), ((i % 8) * self.cell_size +
                                                             self.top + self.cell_size // 2,
                                                             i // 8 * self.cell_size +
                                                             self.left + self.cell_size // 2),
                                   self.cell_size // 2 - 3)

    # Обработка нажатия на поле
    def sq_coor(self, pos):
        global SEQUENCE
        pos = [(pos[0] - self.top) // self.cell_size, (pos[1] - self.left) // self.cell_size]
        if pos[0] > self.width - 1 or pos[1] > self.height - 1 or 0 > pos[0] or 0 > pos[1]:
            print("None")
        else:
            if self.board_sq[pos[0] + pos[1] * 8][1] != 0 and self.board_sq[pos[0] + pos[1] * 8][0] == SEQUENCE:
                is_moving = [False, 0]
                for i in range(len(self.board_sq)):
                    if self.board_sq[i][1] == 2:
                        is_moving = [True, i]
                        break
                if is_moving[0]:
                    if self.board_sq[pos[0] + pos[1] * 8][1] == 3:
                        self.board_sq[pos[0] + pos[1] * 8] = self.board_sq[is_moving[1]]
                        self.board_sq[is_moving[1]] = ["e", 0]
                    for i in range(len(self.board_sq)):
                        if self.board_sq[i][1] == 2:
                            self.board_sq[i][1] = 1
                        elif self.board_sq[i][1] == 3:
                            self.board_sq[i][1] = 0
                else:
                    if self.board_sq[pos[0] + pos[1] * 8][0] == "w":
                        if pos[0] != 7 and self.board_sq[pos[0] + pos[1] * 8 + 9][1] != 1:
                            self.board_sq[pos[0] + pos[1] * 8 + 9] = ["e", 3]
                        if pos[0] != 0 and self.board_sq[pos[0] + pos[1] * 8 + 7][1] != 1:
                            self.board_sq[pos[0] + pos[1] * 8 + 7] = ["e", 3]
                    else:
                        if pos[0] != 7 and self.board_sq[pos[0] + pos[1] * 8 - 9][1] != 1:
                            self.board_sq[pos[0] + pos[1] * 8 - 9] = ["e", 3]
                        if pos[0] != 0 and self.board_sq[pos[0] + pos[1] * 8 - 7][1] != 1:
                            self.board_sq[pos[0] + pos[1] * 8 - 7] = ["e", 3]
            else:
                for i in range(len(self.board_sq)):
                    if self.board_sq[i][1] == 2:
                        self.board_sq[i][1] = 1
                    elif self.board_sq[i][1] == 3:
                        self.board_sq[i][1] = 0
            print(pos)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Checkers")
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                board.sq_coor(event.pos)

        board.render()
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
