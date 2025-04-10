
import pygame

pygame.init()
big_font = pygame.font.Font(None, 60)
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Two-Player Pygame Chess')
timer = pygame.time.Clock()
fps = 60
# game variables and images
white_pieces  = ['rook', 'knight', 'bishop', 'king', 'queen','bishop','knight','rook','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen','bishop','knight','rook','pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),
                  (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
black_locations = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),
                   (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
captured_white_pieces = []
captured_black_pieces = []
turn_step = 0
selection = 100
valid_moves = [] # save valid moves
# load images
# black
black_rook = pygame.image.load('Images/black rook.png')
black_rook = pygame.transform.scale(black_rook, (80, 80))
black_small_rook = pygame.transform.scale(black_rook, (40, 40))

black_knight = pygame.image.load('Images/black knight.png')
black_knight = pygame.transform.scale(black_knight, (80, 80))
black_small_knight = pygame.transform.scale(black_knight, (40, 40))

black_bishop = pygame.image.load('Images/black bishop.png')
black_bishop = pygame.transform.scale(black_bishop, (80, 80))
black_small_bishop = pygame.transform.scale(black_bishop, (40, 40))

black_queen = pygame.image.load('Images/black queen.png')
black_queen = pygame.transform.scale(black_queen, (80, 80))
black_small_queen = pygame.transform.scale(black_queen, (40, 40))

black_king = pygame.image.load('Images/black king.png')
black_king = pygame.transform.scale(black_king, (80, 80))
black_small_king = pygame.transform.scale(black_king, (40, 40))

black_pawn = pygame.image.load('Images/black pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (80, 80))
black_small_pawn = pygame.transform.scale(black_pawn, (40, 40))

# White
white_rook = pygame.image.load('Images/white rook.png')
white_rook = pygame.transform.scale(white_rook, (80, 80))
white_small_rook = pygame.transform.scale(white_rook, (40, 40))

white_knight = pygame.image.load('Images/white knight.png')
white_knight = pygame.transform.scale(white_knight, (80, 80))
white_small_knight = pygame.transform.scale(white_knight, (40, 40))

white_bishop = pygame.image.load('Images/white bishop.png')
white_bishop = pygame.transform.scale(white_bishop, (80, 80))
white_small_bishop = pygame.transform.scale(white_bishop, (40, 40))

white_queen = pygame.image.load('Images/white queen.png')
white_queen = pygame.transform.scale(white_queen, (80, 80))
white_small_queen = pygame.transform.scale(white_queen, (40, 40))

white_king = pygame.image.load('Images/white king.png')
white_king = pygame.transform.scale(white_king, (80, 80))
white_small_king = pygame.transform.scale(white_king, (40, 40))

white_pawn = pygame.image.load('Images/white pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (80, 80))
white_small_pawn = pygame.transform.scale(white_pawn, (40, 40))

undo = pygame.transform.scale(pygame.image.load('Images/undo.png'), (80, 80))

white_images = [white_rook, white_knight, white_bishop, white_king, white_queen,white_pawn]
white_small_images = [white_small_rook, white_small_knight, white_small_bishop, white_small_king, white_small_queen, white_small_pawn]
black_images = [black_rook, black_knight, black_bishop, black_king, black_queen,black_pawn]
black_small_images = [black_small_rook, black_small_knight, black_small_bishop,black_small_king, black_small_queen, black_small_pawn]

pieces_list = ['rook', 'knight', 'bishop', 'king', 'queen','pawn']
# draw main game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column*200) , row*100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column*200) , row*100, 100, 100])
        pygame.draw.rect(screen,"gray", [0, 800, WIDTH, 100],2)
        pygame.draw.rect(screen,"gray", [800,0, 200, HEIGHT],2)
        status_text = ["White: Select a Piece to Move", "White: Select a Destination",
                       "Black: Select a Piece to Move", "Black: Select a Destination"]
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (50, 830))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100*i), 2)
            pygame.draw.line(screen, 'black', (100*i, 0), (100*i, 800), 2)
        pygame.draw.line(screen, 'black', (800, 800), (WIDTH, 800), 2)
        pygame.draw.line(screen, 'black', (800, 800), (800, HEIGHT), 2)

# draw pieces on board
def draw_pieces():
    for i in range(len(white_pieces)):
        index = pieces_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 12, white_locations[i][1] * 100 + 10))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 12, white_locations[i][1] * 100 + 10))
        if turn_step <= 1:
            if selection == i:
                pygame.draw.rect(screen, "black" , [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100, 100],2)
    for i in range(len(black_pieces)):
        index = pieces_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 12, black_locations[i][1] * 100 + 10))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 12, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen,'black', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100],2)
# check valid moves
def check_valid_moves():
    if turn_step <= 1:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options


# draw valid moves
def draw_valid_moves(moves):
    if turn_step <= 1:
        color = "red"
    else:
        color = "green"
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 10)

# draw captured pieces
def draw_captured_pieces():
    for i in range(len(captured_white_pieces)):
        index = pieces_list.index(captured_white_pieces[i])
        if captured_white_pieces[i] == 'pawn':
            screen.blit(black_small_pawn, (825, 50 * i + 50))
        else:
            screen.blit(black_small_images[index], (825, 50 * i + 50))
    for i in range(len(captured_black_pieces)):
        index = pieces_list.index(captured_black_pieces[i])
        if captured_black_pieces[i] == 'pawn':
            screen.blit(white_small_pawn, (935, 50 * i + 50))
        else:
            screen.blit(white_small_images[index],(935, 50*i + 50))



# draw game over
def draw_game_over():
    text = big_font.render("GAME OVER", True, "red")
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)

# draw history
def draw_history():
    screen.blit(undo, (860, 810))

# check options
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range(len(pieces)):
        piece = pieces[i]
        location = locations[i]
        if piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == "knight":
            moves_list = check_knight(location, turn)
        elif piece == "bishop":
            moves_list = check_bishop(location, turn)
        elif piece == "king":
            moves_list = check_king(location, turn)
        elif piece == "queen":
            moves_list = check_queen(location, turn)
        elif piece == "pawn":
            moves_list = check_pawn(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

# check rook moves
def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list
def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# check bishop moves
def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append(
                    (position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

# check king valid moves
def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

# check queen valid moves
def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

# check valid pawn moves
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')
# main game
win = ''
game_over = False
run = True
history = []
while run:
    timer.tick(fps)
    screen.fill((240, 217, 181))
    draw_board()
    draw_pieces()
    draw_captured_pieces()
    draw_history()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid_moves(valid_moves)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and game_over != True:
            if event.pos[0] > 800 and event.pos[1] > 800 and len(history) >= 1:
                white_pieces, black_pieces,white_locations, black_locations, captured_white_pieces, captured_black_pieces, turn_step = history.pop()
                selection = 100
                valid_moves = []
                win = ''
                game_over = False
            x_coord = event.pos[0]//100
            y_coord = event.pos[1]//100
            click_coord = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coord in white_locations:
                    selection = white_locations.index(click_coord)
                    if turn_step == 0:
                        turn_step = 1
                if click_coord in valid_moves and selection != 100:
                    history.append((white_pieces.copy(),black_pieces.copy(),white_locations.copy(), black_locations.copy(), captured_white_pieces.copy(), captured_black_pieces.copy(), turn_step))
                    if len(history) >= 4:
                        history.pop(0)
                    white_locations[selection] = click_coord
                    if click_coord in black_locations:
                        black_piece = black_locations.index(click_coord)
                        captured_white_pieces.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            win = "white"
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []

            if turn_step >= 2:
                if click_coord in black_locations:
                    selection = black_locations.index(click_coord)
                    if turn_step == 2:
                        turn_step = 3
                if click_coord in valid_moves and selection != 100:
                    history.append((white_pieces.copy(),black_pieces.copy(),white_locations.copy(), black_locations.copy(), captured_white_pieces.copy(), captured_black_pieces.copy(), turn_step))
                    if len(history) >= 4:
                        history.pop(0)
                    black_locations[selection] = click_coord
                    if click_coord in white_locations:
                        white_piece = white_locations.index(click_coord)
                        captured_black_pieces.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            win = "black"
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    white_options = check_options(white_pieces, white_locations, 'white')
                    black_options = check_options(black_pieces, black_locations, 'black')
                    turn_step = 0
                    selection = 100
                    valid_moves = []

        if event.type == pygame.KEYDOWN and game_over:
            win = ''
            game_over = False
            white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn',
                            'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
            black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn',
                            'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
            white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                               (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
            black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                               (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
            captured_white_pieces = []
            captured_black_pieces = []
            history = []
            turn_step = 0
            selection = 100
            valid_moves = []
    if win != "":
        game_over = True
        draw_game_over()

    pygame.display.flip()
pygame.quit()