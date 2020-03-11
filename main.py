import pygame, pyautogui
pygame.init()

class grid():
    def __init__(self):
        self.field = []
        for x in range(3):
            self.field.append([])
            for y in range(3):
                self.field[x].append(0)
        
        self.player = "x"

        self.check_list = [[[1,0,0],[1,0,0],[1,0,0]], [[0,1,0],[0,1,0],[0,1,0]], [[0,0,1],[0,0,1],[0,0,1]],
        [[1,1,1],[0,0,0],[0,0,0]], [[0,0,0],[1,1,1],[0,0,0]], [[0,0,0],[0,0,0],[1,1,1]],
        [[1,0,0],[0,1,0],[0,0,1]], [[0,0,1],[0,1,0],[1,0,0]]]

    def change_player(self):
        if self.player == "x":
            self.player = "o"
        else:
            self.player = "x"

    def turn(self, x, y):
        self.field[x][y] = self.player

    def check(self):
        for player in (["x", "o"]):
            for check in self.check_list:
                count = 0
                for x in range(len(check)):
                    for y in range(len(check[x])):
                        if check[x][y]:
                            if self.field[x][y] == player:
                                count += 1
                if count == 3:
                    return player, check
        return False, False
    
    def clear_field(self):
        for x in range(3):
            for y in range(3):
                self.field[x][y] = 0


ttt = grid()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (219, 219, 219)
 
# Set the width and height of the screen [width, height]
size = int(pyautogui.size()[1]/2)
cell_size = int(size/3)
screen = pygame.display.set_mode([size, size])
 
pygame.display.set_caption("tic tac toe")

x_img = pygame.transform.scale(pygame.image.load("X.png"), (cell_size, cell_size))
o_img = pygame.transform.scale(pygame.image.load("O.png"), (cell_size, cell_size))
x_won_img = pygame.transform.scale(pygame.image.load("x_won.png"), (size, size))
o_won_img = pygame.transform.scale(pygame.image.load("o_won.png"), (size, size))
images = {"x": x_img, "o": o_img}
won_images = {"x": x_won_img, "o": o_won_img}
 
# Loop until the user clicks the close button.
done = False
pressed = False
winner = ""
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                ttt.clear_field()
                print("reset")
                winner = ""
 
    # --- Game logic should go here
    if winner == "":
        mouse = pygame.mouse.get_pos()
        buttons = pygame.mouse.get_pressed()
        grid_pos = (int(mouse[0]/cell_size), int(mouse[1]/cell_size))

        if buttons[0] and pressed == False:
            pressed = True
            ttt.turn(grid_pos[0], grid_pos[1])
            ttt.change_player()
        if pressed and buttons[0] == 0:
            pressed = False

        player, check = ttt.check()
        if player != False:
            winner = player
            ttt.player = winner

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here

    for x in range(3):
        for y in range(3):
            if ttt.field[x][y] != 0:
                screen.blit(images[f"{ttt.field[x][y]}"], [x*cell_size, y*cell_size])

    # drawing grid
    for x in range(3):
        pygame.draw.line(screen,GREY,[x*cell_size,0],[x*cell_size,size],5)
    for y in range(3):
        pygame.draw.line(screen,GREY,[0,y*cell_size],[size,y*cell_size],5)

    if winner != "":
        x_win = []
        y_win = []
        for x in range(3):
            for y in range(3):
                if check[x][y]:
                    x_win.append(x)
                    y_win.append(y)
        for win in range(len(x_win)-1):
            pygame.draw.line(screen,RED,[(x_win[win]*cell_size)+cell_size/2, (y_win[win]*cell_size)+cell_size/2], [(x_win[win+1]*cell_size)+cell_size/2, (y_win[win+1]*cell_size)+cell_size/2],5)
        #screen.blit(won_images[winner], [0,0])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()