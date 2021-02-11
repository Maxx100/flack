def check_beat_checker_rec_helper_for_fucking_queen(self, index, color="w", is_eat=False, direction=0):
    reversed_color = "w"
    if color == "w":
        reversed_color = "b"
    temp = self.moving([index % 8, index // 8])
    if direction in temp:
        temp.remove(direction)
    for k in temp:
        for i in range(1, 8):
            temp_pi = index + k * i
            pos = [temp_pi % 8, temp_pi // 8]
            if self.board_sq[pos[0] + pos[1] * 8][1] in [1, 6]\
                    and self.board_sq[pos[0] + pos[1] * 8][0] == reversed_color\
                    and pos[0] not in [7, 0] and pos[1] not in [7, 0]:
                is_eat = True
            elif is_eat:
                self.board_sq[pos[0] + pos[1] * 8] = ["e", 5]
                self.check_beat_checker_rec_helper_for_fucking_queen(index=temp_pi, color=color,
                                                                     is_eat=True, direction=-k)
            if pos[0] in [7, 0] or pos[1] in [7, 0]:
                break
    return is_eat