import pygame, sys, random, json
from pygame.math import Vector2

class SNAKE:
    """Class representing the snake in the game."""
    def __init__(self):
        """Initialize the snake."""
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.start_moving = False
        
        # Load and scale snake head images
        self.head_up = pygame.image.load("images/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("images/head_down.png").convert_alpha()
        self.head_right = pygame.image.load("images/head_right.png").convert_alpha()
        self.head_left = pygame.image.load("images/head_left.png").convert_alpha()

        self.head_up = pygame.transform.scale(self.head_up, (cell_size, cell_size))
        self.head_down = pygame.transform.scale(self.head_down, (cell_size, cell_size))
        self.head_right = pygame.transform.scale(self.head_right, (cell_size, cell_size))
        self.head_left = pygame.transform.scale(self.head_left, (cell_size, cell_size))

        # Load and scale snake tail images
        self.tail_up = pygame.image.load("images/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("images/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("images/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load("images/tail_left.png").convert_alpha()

        self.tail_up = pygame.transform.scale(self.tail_up, (cell_size, cell_size))
        self.tail_down = pygame.transform.scale(self.tail_down, (cell_size, cell_size))
        self.tail_right = pygame.transform.scale(self.tail_right, (cell_size, cell_size))
        self.tail_left = pygame.transform.scale(self.tail_left, (cell_size, cell_size))

        # Load and scale snake body images
        self.body_horizental = pygame.image.load("images/body_horizental.png").convert_alpha()
        self.body_vertical = pygame.image.load("images/body_vertical.png").convert_alpha()

        self.body_horizental = pygame.transform.scale(self.body_horizental, (cell_size, cell_size))
        self.body_vertical = pygame.transform.scale(self.body_vertical, (cell_size, cell_size))

        # Load and scale snake body corner images
        self.body_tl = pygame.image.load("images/top_left.png").convert_alpha()
        self.body_bl = pygame.image.load("images/down_left.png").convert_alpha()
        self.body_tr = pygame.image.load("images/top_right.png").convert_alpha()
        self.body_br = pygame.image.load("images/down_right.png").convert_alpha()

       
        self.body_tl = pygame.transform.scale(self.body_tl, (cell_size, cell_size))
        self.body_bl = pygame.transform.scale(self.body_bl, (cell_size, cell_size))
        self.body_tr = pygame.transform.scale(self.body_tr, (cell_size, cell_size))
        self.body_br = pygame.transform.scale(self.body_br, (cell_size, cell_size))

        # Load sound effects
        self.crunch_sound = pygame.mixer.Sound('sounds/crunch_2.mp3')
        self.explosion = pygame.mixer.Sound('sounds/bomb2.mp3')
        self.head = self.head_right
        self.tail = self.tail_left
    

    def draw_snake(self):
        """Draw the snake on the screen."""
        self.update_head_graphics()
        self.update_tail_graphics()
       

        for index, block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizental, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)
                    
    def move_snake(self):
        """Move the snake based on its direction."""
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        """Add a new block to the snake's body."""
        
        self.new_block = True

    def update_head_graphics(self):
        """Update the graphics of the snake's
        head based on its movement direction.
        """
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0): self.head = self.head_left
        elif head_relation == Vector2(-1, 0): self.head = self.head_right
        elif head_relation == Vector2(0, 1): self.head = self.head_up
        elif head_relation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
        """Update the graphics of the snake's tail
        based on its movement direction.
        """
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

    def reset(self):
        """Reset the snake to its initial state."""
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        

    def play_crunch_sound(self):
        """Play the sound effect when the snake eats an apple."""
        self.crunch_sound.play()

    def play_explosion(self):
        """Play the sound effect when the snake hits a bomb."""
        self.explosion.play()

class FRUIT:
    """Class representing the fruit (apple) in the game."""
    def __init__(self):
        """Initialize the fruit."""
        self.randomize()

    def draw_fruit(self):
        """Draw the fruit on the screen."""
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        """Randomize the position of the fruit."""
        self.x = random.randint(0 , cell_number - 1)
        self.y = random.randint(0 , cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class BOMB:
    """Class representing the bomb in the game."""
    def __init__(self):
        """Initialize the bomb."""
        self.randomize()

    def draw_bomb(self):
        """Draw the bomb on the screen."""
        bomb_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(bomb, bomb_rect)

    def randomize(self):
        """Randomize the position of the bomb."""
        self.x = random.randint(0 , cell_number - 1)
        self.y = random.randint(0 , cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    """Class managing the main game loop."""
    def __init__(self):
        """Initialize the main game."""
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.game_state = "start_menu"
        self.high_score = self.load_high_score()
        self.bomb = BOMB()
        self.game_over_sound_played = False
        pygame.mixer.init()
        self.background_music = pygame.mixer.Sound('sounds/gamesound.mp3')
        self.background_music.play(-1)
        

    def update(self):
        """Update the game state."""
        if self.game_state != "playing":
            return
        if self.snake.start_moving == False:
            return
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        """Draw all game elements on the screen."""
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.bomb.draw_bomb()

    def check_collision(self):
        """Check for collisions between the snake, fruit, and bomb."""
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            
        if self.bomb is not None and self.bomb.pos == self.snake.body[0]:
            
            if len(self.snake.body) > 3:
                self.snake.body.pop()
                self.snake.play_explosion()
                self.bomb = BOMB()
            else:
                self.game_over()
                return

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            if self.bomb is not None and block == self.bomb.pos:
                self.bomb.randomize()

        

    def check_fail(self):
        """Check if the game should end due to the snake
        colliding with walls or itself.
        """
        if self.game_state == "game_over":
            return
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                if self.game_state == "playing":
                    self.game_over()

        current_score = len(self.snake.body) - 3
        if current_score > self.high_score:
            self.high_score = current_score
            self.save_high_score()

    def game_over(self):
        """Display the game over screen and handle high score updates."""
        self.snake.reset()
        self.game_state = "game_over"
        self.game_over_sound_played = False
        
        
        

    def draw_grass(self):
        """Draw the grass pattern on the screen."""
        grass_color =   (167, 209, 61)
        for row in range (cell_number):
            if row % 2 == 0:
                for col in range (cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size , row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

            else:
                for col in range (cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size , row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        """Draw the current score on the screen."""
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (65, 74, 12))
        score_label = game_font.render("Score:", True, (65, 74, 12))

        score_rect = score_surface.get_rect(center = (cell_number * cell_size - 70, 30))
        
        apple_x = score_rect.right + 10
        apple_y = score_rect.bottom - 17
        
        score_label_rect = score_label.get_rect(midright=(score_rect.left - 10, score_rect.centery))
        label_rect = score_label.get_rect(midright=(score_rect.left - 10, score_rect.centery))
        apple_rect = apple.get_rect(midleft=(apple_x, apple_y))
        
        bg_rect = score_rect.union(label_rect).union(apple_rect)
        pygame.draw.rect(screen, (140, 180, 50), bg_rect)

        frame_rect = bg_rect.inflate(5, 5)
        pygame.draw.rect(screen,(65, 74, 12), frame_rect, width=2)

        screen.blit(score_label, score_label_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)


    def load_high_score(self):
        """Load the high score from a file."""
        try:
            with open("high_score.json", "r") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    return data.get("high_score", 0)
                else:
                    return 0
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Save the high score to a file."""
        data = {"high_score": self.high_score}
        with open("high_score.json", "w") as file:
            json.dump(data, file)


def draw_game_over_screen(screen, high_score):
    """Draw the game over screen.

    Args:
        screen (pygame.Surface): The Pygame surface representing the game window.
        high_score (int): The highest score achieved in the game.
    """
    
    if not main_game.game_over_sound_played:
        game_over_sound = pygame.mixer.Sound('sounds/gameover4.wav')
        
        game_over_sound.play()
        main_game.game_over_sound_played = True
    
    screen.fill((10, 10, 10))
    font = pygame.font.SysFont('OCR A Extended', 40)

    title = pygame.font.SysFont('Snap ITC', 90).render('Game Over', True, (255, 0, 0))
    restart_button = font.render('R - Restart', True, (255, 255, 255))
    quit_button = font.render('Q - Quit', True, (255, 255, 255))
    high_score_text = font.render(f'High Score: {high_score}', True, (255, 255, 255))
    
    screen.blit(title, (screen.get_width() / 2 - title.get_width() / 2, screen.get_height() / 2.9 - title.get_height() / 3))
    screen.blit(restart_button, (screen.get_width() / 2 - restart_button.get_width() / 2, screen.get_height() / 1.9 + restart_button.get_height()))
    screen.blit(quit_button, (screen.get_width() / 2 - quit_button.get_width() / 2, screen.get_height() / 2 + quit_button.get_height() / 2))
    screen.blit(high_score_text, (screen.get_width() / 2 - high_score_text.get_width() / 2, screen.get_height() - high_score_text.get_height() - 20))
    
    pygame.display.update()
    

def draw_start_menu(screen):
    """Draw the start menu screen.

    Args:
        screen (pygame.Surface): The Pygame surface representing the game window.
    """
    screen.fill((10, 10, 10))
    font = pygame.font.SysFont('Snap ITC', 90)
    title = font.render('Snake Game', True, (50, 255, 50))
    start_button = pygame.font.SysFont('OCR A Extended', 50).render('Press SPACE to Start', True, (255, 255, 255))
    screen.blit(title, (screen.get_width() / 2 - title.get_width() / 2, screen.get_height() / 2.3 - title.get_height() / 2))
    screen.blit(start_button, (screen.get_width() / 2 - start_button.get_width() / 2, screen.get_height() / 2 + start_button.get_height() / 2))
    pygame.display.update()

# Initialize Pygame
pygame.init()
pygame.mixer.init()

cell_size = 34
cell_number = 20
screen_size = (cell_size * cell_number, cell_size * cell_number)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
apple = pygame.image.load('images/apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (cell_size, cell_size))

bomb = pygame.image.load('images/bomb.png').convert_alpha()
bomb = pygame.transform.scale(bomb, (cell_size, cell_size))

game_font = pygame.font.Font(None, 40)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 170)
main_game = MAIN()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

        if main_game.snake.direction.x != 0 or main_game.snake.direction.y != 0:
            main_game.snake.start_moving = True

    if main_game.game_state == "start_menu":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            main_game.game_state = "playing"
            main_game.snake.start_moving = False
            main_game.is_game_over = False

        draw_start_menu(screen)


    elif main_game.game_state == "playing":
        screen.fill((175, 215, 70))
        main_game.draw_elements()
            

    elif main_game.game_state == "game_over":
        draw_game_over_screen(screen, main_game.high_score)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            main_game.game_state = "start_menu"
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
        

    
    pygame.display.flip()
    clock.tick(60)
