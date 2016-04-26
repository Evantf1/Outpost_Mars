__author__ = 'Justin'

import pygame, sys, random, math
import database_worker, database_defaults
from pygame.locals import *
pygame.init()
window_x = 800
window_y = 640
DISPLAYSURF = pygame.display.set_mode((window_x, window_y))
terrain = database_defaults.Terrain.getTerrainAll()

images = ["Fuel", "Launch Pad", "Starter", "Horiculture Habitat"]
gifs = ["Fuel", "Launch Pad", "Starter", "Corn Growing", "Recycling"]
print gifs
print images
img_32 = [pygame.image.load("pygameAssets\\" + image + " 32.png") for image in images]
img_64 = [pygame.image.load("pygameAssets\\" + image + " 32.png") for image in images]
gif_32 = [pygame.image.load("pygameAssets\\" + gif + " 32.gif").convert_alpha() for gif in gifs]
gif_64 = [pygame.image.load("pygameAssets\\" + gif + " 64.gif").convert_alpha() for gif in gifs]

gridDict_rect = {}
gridDict_surf = {}
side_size = 32
x_len = int(math.floor(window_x / side_size))
y_len = int(math.ceil(window_y / side_size))

z = 0
for x in range(0, x_len):
    for y in range(0, y_len):
        gridDict_rect[(x, y, z)] = pygame.Rect((x * side_size, y * side_size), (side_size, side_size))
        #database_defaults.Tile.createTile(x, y, z)

database_defaults.Tile.createTiles(gridDict_rect.keys())


print gridDict_rect


count = 0
for key in gridDict_rect.keys():
        rand = random.randint(0, 3)
        grassPic = pygame.image.load(terrain[rand][2])
        DISPLAYSURF.blit(grassPic, gridDict_rect[key])
        count += 1

DISPLAYSURF.blit(gif_64[1], gridDict_rect[(10, 10, 0)])
DISPLAYSURF.blit(gif_64[0], gridDict_rect[(10, 12, 0)])
DISPLAYSURF.blit(gif_64[2], gridDict_rect[(12, 10, 0)])
DISPLAYSURF.blit(gif_64[3], gridDict_rect[(8, 10, 0)])
DISPLAYSURF.blit(gif_64[4], gridDict_rect[(10, 8, 0)])


while True: # main game loop



    for event in pygame.event.get():

        rand_x = random.randint(0, 10)
        rand_y = random.randint(0, 10)

        #pygame.transform.rotate(gridDict_surf[(rand_x, rand_y, 0)], 90)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()