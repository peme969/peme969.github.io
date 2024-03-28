# Swervin' Mervin
# (c) Andrew Buntine
# https://github.com/buntine/SwervinMervin
import pygbag.aio as asyncio
import pygame
import sys

sys.path.insert(0, "./swervin_mervin")
import game
import settings

pygame.init()

pygame.display.set_caption("Swervin' Mervin")


async def main():
    if settings.FULLSCREEN:
        w_flag = pygame.FULLSCREEN
        pygame.mouse.set_visible(False)
    else:
        w_flag = 0

    fps_clock = pygame.time.Clock()
    window = pygame.display.set_mode(settings.DIMENSIONS, w_flag)
    instance = game.Game(window, fps_clock)

    while True:
        if instance.waiting:
            await instance.wait()
        else:
            await instance.play()


asyncio.run(main())
