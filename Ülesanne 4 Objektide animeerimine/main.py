import pygame
import random

pygame.init()

# Mänguakna loomine
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sinine Autode Mäng")

# Pildifailide laadimine
bg_image = pygame.image.load("bg_rally.jpg")
red_car_image = pygame.image.load("f1_red.png")
blue_car_image = pygame.image.load("f1_blue.png")

# Taustapildi kuvamine
screen.blit(bg_image, (0, 0))

# Punase auto kuvamine keskele alla
red_car_rect = red_car_image.get_rect()
red_car_rect.centerx = 640 // 2  # Ekraani laius jagatud 2-ga
red_car_rect.bottom = 480  # Ekraani kõrgus
screen.blit(red_car_image, red_car_rect)

# Siniste autode loomine ja liikumine
blue_cars = []
blue_car_speed = 5  # Liikumiskiirus

def create_blue_car():
    blue_car_rect = blue_car_image.get_rect()
    blue_car_rect.x = random.randint(0, 640 - blue_car_rect.width)  # Juhuslik x-koordinaat
    blue_car_rect.y = random.randint(-100, -50)  # Juhuslik y-koordinaat
    blue_cars.append(blue_car_rect)

def move_blue_cars():
    for car in blue_cars:
        car.y += blue_car_speed
        screen.blit(blue_car_image, car)
        # Kui auto on ekraani alt väljas, loo uus auto
        if car.top > 480:
            blue_cars.remove(car)
            create_blue_car()

# Siniste autode loomine
create_blue_car()

score = 0

def check_collision():
    global score
    for car in blue_cars:
        if car.colliderect(red_car_rect):
            score += 1
            blue_cars.remove(car)
            create_blue_car()

# Skoori kuvamine
def display_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Mängutsükkel
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_image, (0, 0))
    move_blue_cars()
    screen.blit(red_car_image, red_car_rect)
    check_collision()
    display_score()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
