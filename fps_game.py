import sys
import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Циклічна анімація руху")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

walk_images = [pygame.image.load(f"images/walk_{i}.png") for i in range(1,10)]
walk_left_images = [pygame.image.load(f"images/walk_left_{i}.png") for i in range(1,10)]
jump_images=[pygame.image.load(f"images/jump_{i}.png") for i in range(1,6)]
walk_index = 0
jump_index = 0
x, y = 100, 300
is_jumping = False
jump_height = 0
max_jump_height = 50
clock = pygame.time.Clock()
player=pygame.Rect(x,y,20,20)
fps = 15

ANIMATION_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMATION_EVENT, 50)
left=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == ANIMATION_EVENT:
        #     walk_index = (walk_index + 1) % len(walk_images)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                jump_height = max_jump_height

    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        left=False
        walk_index = (walk_index + 1) % len(walk_images)
        x+=1
    elif keys[pygame.K_LEFT]:
        walk_index = (walk_index + 1) % len(walk_images)
        left=True
        x-=1

    if is_jumping:
        jump_index+=1
        y -= 10
        jump_height -= 10
        if jump_height <= 0:
            is_jumping = False
            jump_index=0
    else:
        if y < 300:
            y += 5

    screen.fill((255, 255, 255))
    screen.blit(walk_images[walk_index], (x, y))
    if left:
        screen.blit(walk_left_images[walk_index], (x, y))
    if is_jumping:
        screen.blit(jump_images[jump_index], (x, y))
    pygame.display.flip()
    clock.tick(fps)