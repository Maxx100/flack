import pygame

SEQUENCE = "w"


class Menu:
    def __init__(self):
        screen.fill(pygame.Color("grey"))

        f1 = pygame.font.SysFont('candara', 56)
        f2 = pygame.font.SysFont('candara', 36)
        f3 = pygame.font.SysFont('candara', 15)
        text1 = f1.render('Шашки', True,
                          (0, 0, 0))
        text2 = f2.render("Новая игра с компьютером", True,
                          (0, 0, 0))
        text3 = f2.render("Новая игра с другом", True,
                          (0, 0, 0))
        text4 = f3.render("Powered by \"Надежда умирает последней\" community.", True,
                          (0, 0, 0))
        screen.blit(text1, (260, 100))
        screen.blit(text2, (150, 330))
        screen.blit(text3, (190, 450))
        screen.blit(text4, (330, 680))

        pygame.draw.rect(screen, pygame.Color("black"), (140, 320, 445, 50), 1)
        pygame.draw.rect(screen, pygame.Color("black"), (180, 440, 340, 50), 1)
        pygame.display.update()

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.sq_coor(event.pos)
            pygame.display.flip()
            clock.tick(100)
        pygame.quit()

    def sq_coor(self, pos):
        if 140 < pos[0] < 585 and 320 < pos[1] < 360:
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
            exit(0)
        if 180 < pos[0] < 520 and 440 < pos[1] < 490:
            print('second')


class Board:
    def __init__(self):
        # Список фигур
        self.board_sq = []
        for i in range(64):
            self.board_sq.append(["e", 0])
        # e - empty | w - white | b - black
        """
        Клетки: 0 - пусто 1 - шашка  2 - шашка взята  3 - подсвет как возможный ход 
                4 - ход должен быть сделан этой шашкой  5 - ход должен быть совершен на эту клетку
                6 - дамка  7 - дамка взята  8 - ход должен быть сделан этой дамкой
        """
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

    def clear_board(self):
        for i in range(len(self.board_sq)):
            if self.board_sq[i][1] in [2, 4]:
                self.board_sq[i][1] = 1
            elif self.board_sq[i][1] in [3, 5]:
                self.board_sq[i][1] = 0
            elif self.board_sq[i][1] in [7, 8]:
                self.board_sq[i][1] = 6

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
            if self.board_sq[i][1] in [2, 7]:
                pygame.draw.rect(screen, pygame.Color("blue"), ((i % 8) * self.cell_size + self.top + 1,
                                                                i // 8 * self.cell_size + self.left + 1,
                                                                self.cell_size - 2,
                                                                self.cell_size - 2))
            elif self.board_sq[i][1] == 3:
                pygame.draw.circle(screen, pygame.Color("blue"), ((i % 8) * self.cell_size +
                                                                  self.top + self.cell_size // 2,
                                                                  i // 8 * self.cell_size +
                                                                  self.left + self.cell_size // 2), self.cell_size // 4)
            elif self.board_sq[i][1] in [4, 8]:
                pygame.draw.rect(screen, pygame.Color("green"), ((i % 8) * self.cell_size + self.top + 1,
                                                                 i // 8 * self.cell_size + self.left + 1,
                                                                 self.cell_size - 2,
                                                                 self.cell_size - 2))
            elif self.board_sq[i][1] == 5:
                pygame.draw.circle(screen, pygame.Color("green"), ((i % 8) * self.cell_size +
                                                                   self.top + self.cell_size // 2,
                                                                   i // 8 * self.cell_size +
                                                                   self.left + self.cell_size // 2),
                                   self.cell_size // 4)

        # Отрисовка фигур
        for i in range(len(self.board_sq)):
            if self.board_sq[i][1] in [1, 2, 4, 6, 7, 8]:
                if self.board_sq[i][0] == "w":
                    r = "white"
                    r2 = (255, 230, 230)
                else:
                    r = "black"
                    r2 = (25, 25, 25)
                pygame.draw.circle(screen, pygame.Color(r), ((i % 8) * self.cell_size +
                                                             self.top + self.cell_size // 2,
                                                             i // 8 * self.cell_size +
                                                             self.left + self.cell_size // 2),
                                   self.cell_size // 2 - 3)
                if self.board_sq[i][1] in [6, 7, 8]:
                    pygame.draw.circle(screen, (0, 255, 240), ((i % 8) * self.cell_size +
                                                               self.top + self.cell_size // 2,
                                                               i // 8 * self.cell_size +
                                                               self.left + self.cell_size // 2),
                                       self.cell_size // 3)
                else:
                    pygame.draw.circle(screen, r2, ((i % 8) * self.cell_size +
                                                    self.top + self.cell_size // 2,
                                                    i // 8 * self.cell_size +
                                                    self.left + self.cell_size // 2),
                                       self.cell_size // 3)

    def check_beat_checker(self, color, mode="all", pos=None):
        if mode == "all":
            for i in range(len(self.board_sq)):
                if color == self.board_sq[i][0]:
                    if self.check_beat_checker_rec_helper(i, color):
                        if self.board_sq[i][1] == 1:
                            self.board_sq[i][1] = 4
                        else:
                            self.board_sq[i][1] = 8
        elif mode == "only_one":
            is_continue_eat = False
            if self.check_beat_checker_rec_helper(pos, color):
                if self.board_sq[pos][1] == 1:
                    self.board_sq[pos][1] = 2
                else:
                    self.board_sq[pos][1] = 7
                is_continue_eat = True
            return is_continue_eat

    def check_beat_checker_rec_helper(self, index=0, color="w"):
        s = False
        reversed_color = "w"
        if color == "w":
            reversed_color = "b"
        if index < 50:
            if index % 8 > 1 and self.board_sq[index + 7] in [[reversed_color, 1], [reversed_color, 6]]:
                if self.board_sq[index + 14][1] == 0:
                    self.board_sq[index + 14] = ["e", 5]
                    self.check_beat_checker_rec_helper(index + 14, color)
                    s = True
            if index % 8 < 6 and self.board_sq[index + 9] in [[reversed_color, 1], [reversed_color, 6]]:
                if index < 46:
                    if self.board_sq[index + 18][1] == 0:
                        self.board_sq[index + 18] = ["e", 5]
                        self.check_beat_checker_rec_helper(index + 18, color)
                        s = True
        if index > 13:
            if index % 8 < 6 and self.board_sq[index - 7] in [[reversed_color, 1], [reversed_color, 6]]:
                if self.board_sq[index - 14][1] == 0:
                    self.board_sq[index - 14] = ["e", 5]
                    self.check_beat_checker_rec_helper(index - 14, color)
                    s = True
            if index % 8 > 1 and self.board_sq[index - 9] in [[reversed_color, 1], [reversed_color, 6]]:
                if index > 17:
                    if self.board_sq[index - 18][1] == 0:
                        self.board_sq[index - 18] = ["e", 5]
                        self.check_beat_checker_rec_helper(index - 18, color)
                        s = True
        return s

    def check_mb_step(self, pos, is_queen=False):
        is_need_eat = False
        is_can_walk = False
        for i in range(len(self.board_sq)):
            if self.board_sq[i][1] in [4, 5, 8]:
                is_need_eat = True
                break
        if not is_queen:
            if self.board_sq[pos[0] + pos[1] * 8][1] in [1, 4]:
                self.board_sq[pos[0] + pos[1] * 8][1] = 2
            if not is_need_eat:
                if self.board_sq[pos[0] + pos[1] * 8][0] == "w":
                    if pos[0] != 7 and self.board_sq[pos[0] + pos[1] * 8 + 9][1] not in [1, 6]:
                        self.board_sq[pos[0] + pos[1] * 8 + 9] = ["e", 3]
                        is_can_walk = True
                    if pos[0] != 0 and self.board_sq[pos[0] + pos[1] * 8 + 7][1] not in [1, 6]:
                        self.board_sq[pos[0] + pos[1] * 8 + 7] = ["e", 3]
                        is_can_walk = True
                else:
                    if pos[0] != 7 and self.board_sq[pos[0] + pos[1] * 8 - 7][1] not in [1, 6]:
                        self.board_sq[pos[0] + pos[1] * 8 - 7] = ["e", 3]
                        is_can_walk = True
                    if pos[0] != 0 and self.board_sq[pos[0] + pos[1] * 8 - 9][1] not in [1, 6]:
                        self.board_sq[pos[0] + pos[1] * 8 - 9] = ["e", 3]
                        is_can_walk = True
        else:
            if self.board_sq[pos[0] + pos[1] * 8][1] in [6, 8]:
                self.board_sq[pos[0] + pos[1] * 8][1] = 7
            if not is_need_eat:
                temp = [7, 9, -7, -9]
                pos_index = pos[0] + pos[1] * 8
                for k in temp:
                    for i in range(1, 8):
                        temp_pi = pos_index + k * i
                        pos = [temp_pi % 8, temp_pi // 8]
                        if self.board_sq[pos[0] + pos[1] * 8][1] not in [1, 6]:
                            self.board_sq[pos[0] + pos[1] * 8] = ["e", 3]
                            is_can_walk = True
                        else:
                            break
                        if pos[0] in [7, 0] or pos[1] in [7, 0]:
                            break
        return is_can_walk

    def check_winner(self, color="w"):
        can_walk = False
        for i in range(64):
            if self.board_sq[i]:
                if self.board_sq[i][0] == color:
                    can_walk = True
                    break
        if not can_walk:
            if color == "w":
                print("Черные победили!")
            else:
                print("Белые победили!")

    # Обработка нажатия на поле
    def sq_coor(self, pos):
        global SEQUENCE
        pos = [(pos[0] - self.top) // self.cell_size, (pos[1] - self.left) // self.cell_size]
        if pos[0] > self.width - 1 or pos[1] > self.height - 1 or 0 > pos[0] or 0 > pos[1]:
            print("None")
        else:
            if self.board_sq[pos[0] + pos[1] * 8][1] != 0 and self.board_sq[pos[0] + pos[1] * 8][0] in [SEQUENCE, "e"]:
                is_moving = [False, 0]
                can_i_walk = True
                for i in range(len(self.board_sq)):
                    if self.board_sq[i][1] in [2, 7]:
                        is_moving = [True, i]
                    elif self.board_sq[i][1] in [4, 5, 8]:
                        can_i_walk = False
                if can_i_walk or self.board_sq[pos[0] + pos[1] * 8][1] in [4, 5, 8]:
                    if is_moving[0]:
                        if self.board_sq[pos[0] + pos[1] * 8][1] == 5:
                            if abs(pos[0] + pos[1] * 8 - is_moving[1]) in [14, 18]:
                                self.board_sq[pos[0] + pos[1] * 8] = self.board_sq[is_moving[1]]
                                self.board_sq[is_moving[1]] = ["e", 0]
                                self.board_sq[abs(pos[0] + pos[1] * 8 + is_moving[1]) // 2] = ["e", 0]
                                self.clear_board()
                                if self.check_beat_checker(SEQUENCE, mode="only_one", pos=pos[0] + pos[1] * 8):
                                    pass
                                else:
                                    self.check_winner(color=SEQUENCE)
                                    if SEQUENCE == "w":
                                        SEQUENCE = "b"
                                    else:
                                        SEQUENCE = "w"
                                    self.clear_board()
                                    self.check_beat_checker(SEQUENCE)
                        else:
                            if self.board_sq[pos[0] + pos[1] * 8] == [SEQUENCE, 1]:
                                self.clear_board()
                                self.check_beat_checker(SEQUENCE)
                                self.check_mb_step(pos)
                            elif self.board_sq[pos[0] + pos[1] * 8] == [SEQUENCE, 6]:
                                self.clear_board()
                                self.check_beat_checker(SEQUENCE)
                                self.check_mb_step(pos, is_queen=True)
                            else:
                                if self.board_sq[pos[0] + pos[1] * 8][1] == 3:
                                    self.board_sq[pos[0] + pos[1] * 8] = self.board_sq[is_moving[1]]
                                    self.board_sq[is_moving[1]] = ["e", 0]
                                    if SEQUENCE == "w":
                                        SEQUENCE = "b"
                                    else:
                                        SEQUENCE = "w"
                                    self.check_winner(color=SEQUENCE)
                                self.clear_board()
                                self.check_beat_checker(SEQUENCE)
                    else:
                        if self.board_sq[pos[0] + pos[1] * 8][1] in [6, 8]:
                            self.check_mb_step(pos, is_queen=True)
                        else:
                            self.check_mb_step(pos)
                else:
                    self.clear_board()
                    self.check_beat_checker(SEQUENCE)
            else:
                self.clear_board()
                self.check_beat_checker(SEQUENCE)
            print("POS:", pos, "| INDEX:", pos[0] + pos[1] * 8, "| STATUS:", self.board_sq[pos[0] + pos[1] * 8])
        for i in range(8):
            if self.board_sq[i][0] == "b" and self.board_sq[i][1] not in [6, 7, 8]:
                self.board_sq[i][1] = 6
            if self.board_sq[i + 56][0] == "w" and self.board_sq[i][1] not in [6, 7, 8]:
                self.board_sq[i + 56][1] = 6


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Checkers")
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    menu = Menu()
    menu.main()
    # board = Board()
    ''' running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                board.sq_coor(event.pos)
        board.render()
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()'''
