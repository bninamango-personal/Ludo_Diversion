from Grupo_01 import Dado as dado
from Grupo_01 import Board_ as board
from Grupo_01 import Player as player


def Start():
    board.Create(5, 5)
    board.Render()

    player.Create(0, 0, 'B')
    player.Render()


def Input():
    value = input("Your launch are: ")


def Update():
    player.Move(2)


def Render():
    player.Render()


if __name__ == '__main__':
    Start()
    # Game Loop
    # while True:
    #     Input()
    #     Update()
    #     Render()
