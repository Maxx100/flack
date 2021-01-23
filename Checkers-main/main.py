import pygame


class Menu:
    def __init__(self):
        pass

    def main(self):
        pass


class Board:
    def __init__(self):
        # Список экземпляров фигур
        self.arr = []
        self.board_sq = [0] * 64  # Клетки: 0 - пусто  1 - шашка  2 - шашка взята  3 - подсвет как возможный ход
        # Заполнение списков
        for k in range(1, 8, 2):
            self.board_sq[k - 1] = 1
            self.arr.append(Checker("w", k))
            self.board_sq[k + 8] = 1
            self.arr.append(Checker("w", k + 9))
            self.board_sq[k + 15] = 1
            self.arr.append(Checker("w", k + 16))

            self.arr.append(Checker("b", k + 41))
            self.board_sq[k + 40] = 1
            self.arr.append(Checker("b", k + 48))
            self.board_sq[k + 47] = 1
            self.arr.append(Checker("b", k + 57))
            self.board_sq[k + 56] = 1
        # Стандартные значения графики
        self.width = 8
        self.height = 8
        self.left = 10
        self.top = 10
        self.cell_size = 85

    # Проверка, возможен ли данный ход
    def can_it_move(self, coord, fig):
        # Временное хранилище данных о фигуре
        temp = fig.return_data()
        # Если ход возможен...
        if abs(coord - temp[1]) in [7, 9]:
            if coord not in self.board_sq:
                return True
        return False

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
        # Отрисовка фигур
        for i in self.arr:
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

    # Обработка нажатия на поле
    def sq_coor(self, pos):
        pos = [(pos[0] - self.top) // self.cell_size, (pos[1] - self.left) // self.cell_size]
        if pos[0] > self.width - 1 or pos[1] > self.height - 1 or 0 > pos[0] or 0 > pos[1]:
            print("None")
        else:
            if 2 in self.board_sq:
                if self.board_sq[pos[0] + pos[1] * 8] == 1:
                    pass
                else:
                    self.board_sq[self.board_sq.index(2)] = 1
            else:
                if self.board_sq[pos[0] + pos[1] * 8] == 1:
                    self.board_sq[pos[0] + pos[1] * 8] = 2
            print(pos)


# Класс шашки
class Checker:
    def __init__(self, color, coord, is_move=False):
        self.color = color
        self.coord = coord
        self.is_move = is_move

    # Запрос данных о фигуре
    def return_data(self):
        return self.color, self.coord, self.is_move


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Checkers")
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board()
    board.render()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                board.sq_coor(event.pos)
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
