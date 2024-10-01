from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 800, 600
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def hand_move():
    global x,y
    x = random.uniform(0,800)
    y = random.uniform(0, 600)


def move_character():
    global x, y, X, Y, frame
    for i in range(0,100+1,6):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(x, y)
        t=i/100
        a=(1-t)*X + t*x
        b=(1-t)*Y + t*y
        if x-X>0:
            character.clip_draw(frame * 100, 100, 100, 100, a, b)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, a, b)
        update_canvas()
        delay(0.05)

    X, Y = x, y
    frame = (frame + 1) % 8

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
X, Y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_move()
    hand.draw(x,y)
    update_canvas()
    delay(0.1)
    move_character()


    handle_events()

close_canvas()




