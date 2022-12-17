def on_left_pressed():
    global game2, left_car, right_car
    game2 = 1
    left_car = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . 3 1 1 3 . . . . . . 
                    . . . . . 2 1 1 1 1 2 . . . . . 
                    . . . . . 2 1 1 1 1 2 . . . . . 
                    . . . . . . 3 1 1 3 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    right_car = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . 3 1 1 3 . . . . . . 
                    . . . . . 2 1 1 1 1 2 . . . . . 
                    . . . . . 2 1 1 1 1 2 . . . . . 
                    . . . . . . 3 1 1 3 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    left_car.y = 20
    right_car.y = 20
    scene.camera_follow_sprite(left_car)
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
    left_car.vy = 10
    right_car.vy = 10
    left_car.ay = 3
    right_car.ay = 3
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_right_pressed():
    global game2, picture
    game2 = 2
    picture2 = image.create(160, 120)
    picture2.fill(1)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile2(sprite2, location2):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.tile_grass2,
    on_overlap_tile2)

y = 0
x = 0
game2 = 0
right_car: Sprite = None
left_car: Sprite = None
picture = image.create(160, 120)
picture.fill(1)

def on_a_pressed():
    picture.fill(1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_forever():
    global game2, x, y
    if game2 == 1:
        left_car.say_text(pins.P1.analog_read())
        left_car.x = Math.map(pins.P1.analog_read(), 0, 1023, 10, 70)
        right_car.say_text(pins.P2.analog_read())
        right_car.x = Math.map(pins.P2.analog_read(), 0, 1023, 90, 150)
        info.set_score(left_car.y)
    elif game2 == 2:
        x = Math.map(pins.P1.analog_read(), 0, 1023, 1, 160)
        y = Math.map(pins.P2.analog_read(), 0, 1023, 120, 1)
        picture.set_pixel(x, y, 15)
        scene.set_background_image(picture)
forever(on_forever)
