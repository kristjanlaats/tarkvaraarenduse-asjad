#kristjan.laats
import pygame
import math

pygame.init()
# Ekraani seaded
screen = pygame.display.set_mode([640,480])

class CustomRect(pygame.Rect):
    def __init__(self, x, y, width, height, custom_attribute):
        super().__init__(x, y, width, height)
        self.custom_attribute = custom_attribute

pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

running = True

# Lisame pildid
bg_shop = pygame.image.load("bg_shop.png")
bg_shop = pygame.transform.scale(bg_shop, [640,480])
screen.blit(bg_shop,[0,0])
bg_shop_rect = bg_shop.get_rect()

seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [300,300])
screen.blit(seller,[100,100])
seller_rect = seller.get_rect()

chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [400,200])
screen.blit(chat,[250,50])
chat_rect = chat.get_rect()

VIKK_logo = pygame.image.load("VIKK_logo.png")
VIKK_logo = pygame.transform.scale(VIKK_logo, [200,100])
screen.blit(VIKK_logo,[0,350])
VIKK_logo_rect = VIKK_logo.get_rect()

mõõk = pygame.image.load("mõõk.png")
mõõk = pygame.transform.scale(mõõk, [200,50])
screen.blit(mõõk,[500,200])
mõõk_rect = mõõk.get_rect()

tort = pygame.image.load("tort.png")
tort = pygame.transform.scale(tort, [200,100])
screen.blit(tort,[300,200])
tort_rect = tort.get_rect()

font = pygame.font.Font(None, 30)
text = font.render("Tere, mina olen Kristjan Lääts", True, [255,255,255])
screen.blit(text, [260,150])

def draw_text_arc(surface, text, font, color, center, radius, angle):
    characters = [char for char in text]
    total_characters = len(characters)
    angle_per_char = angle / (total_characters - 1)

    for i, char in enumerate(characters):
        char_angle = angle_per_char * i - angle / 2
        rotated_text = pygame.transform.rotate(font.render(char, True, color), char_angle)
        char_pos = (center[0] + radius * math.cos(math.radians(char_angle)) + 40,  # Nihutame 10 pikslit paremale
                    center[1] + radius * math.sin(math.radians(char_angle)))
        surface.blit(rotated_text, rotated_text.get_rect(center=char_pos))

# Teksti kaare seaded
center = (100, 400)  # Uued koordinaadid
radius = 70
angle = 180

# Ekraani uuendamine
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Taustapildi joonistamine
    draw_text_arc(screen, "TULEVIK 2050", font, [255, 255, 255], center, radius, angle)  # Valge kaarega teksti joonistamine
    pygame.display.flip()  # Ekraani uuendamine

pygame.quit()
