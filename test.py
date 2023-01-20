import pygame
import random

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Shaq vs Vin")

# Load rock image
rock_image = pygame.image.load("rock.png")

explosion_sound = pygame.mixer.Sound("explosion.wav")


objects = []

class MovingObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("rock.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = [random.randint(1,5),random.randint(1,5)]

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        # Check if the object collides with the edge of the screen
        if self.rect.left < 0 or self.rect.right > 800:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.speed[1] = -self.speed[1]


# Load cursor image
cursor_image = pygame.image.load("ball.png")
cursor_rect = cursor_image.get_rect()

#initialize score/health and add score to top of page
score = 0
health = 100
font = pygame.font.Font("font_file.ttf", 24)
scoredisplay = font.render("Score: " + str(score), True, (255, 255, 255))

spawn_rate = 1000
last_spawn = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    # Update the cursor rect to follow the mouse
    mouse_pos = pygame.mouse.get_pos()
    cursor_rect.center = mouse_pos
    mouse_pos = pygame.mouse.get_pos()
    
    # Update the cursor rect to follow the mouse
    cursor_rect.center = mouse_pos

    health_text = font.render("Health: " + str(int(health)) + "%", True, (255, 0, 0))
    screen.blit(health_text, (10, 10))

    # Check for collision between ball and rock
    for obj in objects:
        if obj.rect.collidepoint(mouse_pos):
            # Remove the object
            objects.remove(obj)
            explosion_sound.play()
            score = score + 1
            scoredisplay = font.render("Score: " + str(score), True, (255, 255, 255))

    # Check if it's time to spawn a new object
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn >= spawn_rate:
        # Create a new object
        obj = MovingObject(random.randint(0,800), random.randint(0,600))
        objects.append(obj)
        # Update the last spawn time
        last_spawn = current_time

    # Update the objects
    for obj in objects:
        obj.update()



    screen.fill((0, 0, 0))

    # Draw the objects
    for obj in objects:
        screen.blit(obj.image, obj.rect)



    # Clear screen and draw sprites
    
    screen.blit(cursor_image, cursor_rect)
    screen.blit(scoredisplay, (500, 10))
    pygame.display.update()

# Quit pygame
pygame.quit()
