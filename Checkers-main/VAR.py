if self.board_sq[index + k * i][1] != 0:
    if eating:
        self.board_sq[index + k * i] = ["e", 5]
        print(index + k * i)
        self.check_beat_checker_rec_helper(index + k * i, color)
        s = True
        break
    elif self.board_sq[index + k * i][0] == reversed_color:
        eating = True