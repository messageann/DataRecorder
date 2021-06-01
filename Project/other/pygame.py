import pygame
import scripts


FONT_COLOR = (255, 255, 255)
FONT_SIZE = 50

DISPLAY_SIZE = (640, 480)
BACKGROUND_COLOR = (0, 0, 0)

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(DISPLAY_SIZE)

    font = pygame.font.Font(None, FONT_SIZE)
    cases_iter = iter(scripts.CURRENT)
    new_case = next(cases_iter)
    current_text, delay = new_case.get_text(), new_case.get_duration()

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(1000)
        delay -= dt

        text = font.render(current_text, True, FONT_COLOR)
        screen.fill(BACKGROUND_COLOR)
        screen.blit(text, ((DISPLAY_SIZE[0] - text.get_width()) // 2, (DISPLAY_SIZE[1] - text.get_height()) // 2))

        if delay <= 0 or current_text is None:
            try:
                new_case = next(cases_iter)
                current_text, delay = new_case.get_text(), new_case.get_duration()
            except StopIteration:
                running = False

        pygame.display.flip()

pygame.quit()
