# Kevin Rodriguez
# Game Engine

import pygame, random
from pygame.math import Vector2 # For player movement


# Initialize PyGame & Set Window Dimensions
pygame.init()
screen_x = 1200
screen_y = 800
screen = pygame.display.set_mode((screen_x, screen_y))

# Background and Sprites
background = pygame.image.load("vertical_road.jpg")
background = pygame.transform.scale(background, (screen_x, screen_y)) # Rescales grass background texture to fit the screen resolution
spritePNG = pygame.image.load("car.png").convert()
mobPNG = pygame.image.load("bomb.png")
spriteAttack = pygame.image.load("missile.png")

# Rescales sprites (x and y can be adjusted accordingly)
spritePNG = pygame.transform.scale(spritePNG, (100, 65))
mobPNG = pygame.transform.scale(mobPNG, (50, 50))
spriteAttack = pygame.transform.scale(spriteAttack, (40, 40))

# PyGame Window Name & Icon
pygame.display.set_caption("2D Game")
pygame.display.set_icon(spritePNG)

# Screen Text

font = pygame.font.SysFont(None, 50)
def text_on_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [screen_x / 2, screen_y / 2])

def background_scene(background):
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))

# # Sprite Collision
# def touching(sprite_a, sprite_b):
#     collided = pygame.sprite.collide_mask(sprite_a, sprite_b)
#     return collided

# Player Sprite Attributes
class Player(pygame.sprite.Sprite):
    def __init__(self, pos=(screen_x / 2, screen_y / 2)):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritePNG
        self.original_image = self.image
        self.image.set_colorkey((0, 0, 0)) # Makes black hitbox invisible - Change values to change hitbox color
        self.rect = self.image.get_rect(center=pos) # Creates Sprite Hitbox using AABB
        self.radius = int(self.rect.width * .9 / 2)  # Sprite Collision using CBB
        # self.rect.center = (screen_x / 2, screen_y / 2) # Spawn sprite in the center of the screen
        self.position = Vector2(pos)
        self.direction = Vector2(1, 0)
        self.speed = 0
        self.angle_speed = 0
        self.angle = 0

    # Player Sprite Direction using Vectors
    def update(self):
        if self.angle_speed != 0:
            # Rotate the direction vector and then the image.
            self.direction.rotate_ip(self.angle_speed)
            self.angle += self.angle_speed
            self.image = pygame.transform.rotate(self.original_image, -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        # Update the position vector and the rect.
        self.position += self.direction * self.speed
        self.rect.center = self.position

        # Boundary Detection - Sprite does not go past the edges
        self.rect.clamp_ip(screen.get_rect())

    def attack(self):
        attack = playerAttack(self.rect.centerx, self.rect.top)
        all_sprites.add(attack)
        attacks.add(attack)

# Player Attack Attributes
class playerAttack(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteAttack
        self.rect = self.image.get_rect() # Creates Sprite Hitbox using AABB
        self.radius = int(self.rect.width * .9 / 2)  # Sprite using CBB
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy

        # Delete Attack Sprite if it moves off the screen
        if self.rect.bottom < 0:
            self.kill()

# Mob Sprite Attributes
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mobPNG
        self.rect = self.image.get_rect() # Creates Sprite Hitbox using AABB
        self.radius = int(self.rect.width * .9 / 2) # Sprite Collision using CBB
        # Spawn Coordinates Randomized
        self.rect.x = random.randrange(screen_x - self.rect.width)
        self.rect.y = random.randrange(-100, -40)

        # Mob Speed is randomized when created
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-4, 4)

    def update(self):
        # Mob Movement - When mob moves off screen without being hit then it will respawn at the top
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > screen_y + 10 or self.rect.left < -25 or self.rect.right > screen_x + 20:
            self.rect.x = random.randrange(screen_x - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

# Get Mouse Position for future incorporation - Returns a Tuple
mouse_movement = pygame.mouse.get_pos()

# FPS
clock = pygame.time.Clock()

# Create Sprite Groups and add Sprites to it
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
attacks = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Mob Count
for i in range(6):
    bomb = Mob()
    all_sprites.add(bomb)
    mobs.add(bomb)

def main():
    # Event Loop
    loop = True
    while loop:

        # Time / FPS
        pygame.time.delay(20)
        clock.tick(60)

        # Create Background using Sprite
        background_scene(background)

        # Event Loop
        for event in pygame.event.get():
            # Close game with Exit Button
            if event.type == pygame.QUIT:
                loop = False
            # Main Sprite movement
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.speed += 1
                elif event.key == pygame.K_DOWN:
                    player.speed -= 1
                elif event.key == pygame.K_LEFT:
                    player.angle_speed = -4
                elif event.key == pygame.K_RIGHT:
                    player.angle_speed = 4
                # Sprite Attack
                elif event.key == pygame.K_SPACE:
                    player.attack()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.angle_speed = 0
                elif event.key == pygame.K_RIGHT:
                    player.angle_speed = 0



        # Attack + Mob Collision - Built into PyGame - AABB
        collisions = pygame.sprite.groupcollide(mobs, attacks, True, True)
        for hit in collisions:
            bomb = Mob()
            all_sprites.add(bomb)
            mobs.add(bomb)

        # Player + Mob Collision - Built into PyGame - Sprite Collision using CBB
        collisions = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        if collisions:
            loop = False



        all_sprites.update()
        pygame.display.update()
        all_sprites.draw(screen)
        pygame.display.update()

main()






