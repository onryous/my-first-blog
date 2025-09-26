import pygame

pygame.init()
dis = pygame.display.set_mode((800,800))

font = pygame.font.SysFont(None,24)

dis_over = False
count = 1

while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()
    count = 1
    x = 10

    while x<800:
        y = 10
        while y<800:
            pygame.draw.rect(dis, (255, 255, 0), (x,y, 40, 40), 1)
            text = font.render(str(count), True, (255,0,0))
            text_rect = text.get_rect(center=(x+20,y+20,))
            dis.blit(text,text_rect)

            count += 1

        y += 50
        x += 50


pygame.display.update()

quit()