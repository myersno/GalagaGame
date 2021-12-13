import os
import pygame as pg

# Complete me! - TODO

class Enemy(pg.sprite.Sprite):
    # Load the sprite with an image
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("enemy.png").convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randrange(0, 200)
        self.speedx = random.randrange(1,2)
    # Make the enemies a random distance from the player (speed is a bit weird)
    def update(self):
        self.rect.x += self.speedx
        if self.rect.right > screenWidth:
            self.rect.x = 50
            self.rect.y = random.randrange(0, 250)
            self.speedx = random.randrange(1,3)
        if self.rect.x > screenWidth:
            self.kill()
    # Enemies go pew pew
    def shootEnemy(self):
         bulletEnemy = BulletEnemy(self.rect.centerx, self.rect.bottom)
         allSprites.add(bulletEnemy)
         bulletsEnemy.add(bulletEnemy)
