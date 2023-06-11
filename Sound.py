import pygame as pg


def Initialize():
    pg.mixer.init()


def Play(file: str, chanel: int, volume: float = 1, loop: bool = False):
    file_path = f"Sounds/{file}"

    pg.mixer.music.load(file_path)

    sound = pg.mixer.Sound(file_path)

    sound.set_volume(volume)

    is_looping: int = -1 if loop else 0

    pg.mixer.Channel(chanel).play(sound, loops=is_looping)


def Stop(chanel: int):
    pg.mixer.Channel(chanel).stop()


def StopAll():
    pg.mixer.stop()
