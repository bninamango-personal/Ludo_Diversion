import Board_ as board

position_x = position_y = 0
character = ''


def Create(x: int, y: int, c: str):
    global position_x, position_y, character
    position_x = x
    position_y = y
    character = c


def Move(y: int):
    global position_y
    position_y += y


def Render():
    global position_x, position_y, character
    board.Update(position_x, position_y, character)
    board.Render()