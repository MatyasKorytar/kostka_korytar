x = randint(1, 6)
y = randint(1, 10)
def on_forever():
    global x
    x = randint(1, 6)
    def on_button_pressed_a():
        pass
    input.on_button_pressed(Button.A, on_button_pressed_a)
    if input.is_gesture(Gesture.SHAKE):
        x = 1
        music.play_melody("C", 120)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
        """)
        x = 2
        basic.show_leds("""
        . . . . .
        . . # . .
        . . . . .
        . . # . .
        . . . . .
        """)
        x = 3
        basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        """)
        x = 4
        basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
        x = 5
        basic.show_leds("""
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        """)
        x = 6
        basic.show_leds("""
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        """)
        pass
        global y
        y = randint(1, 10)
        def on_button_pressed_b():
            pass
        input.on_button_pressed(Button.B, on_button_pressed_b)
        if input.is_gesture(Gesture.SHAKE):
                y = 1
                basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
                y = 2
                basic.show_leds("""
                . . . . .
                . . . . .
                . # . # .
                . . . . .
                . . . . .
                """)
                y = 3
                basic.show_leds("""
                . . . . .
                . . . . .
                . # # # .
                . . . . .
                . . . . .
                """)
                y = 4
                basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                . # . # .
                . . . . .
                """)
                y = 5
                basic.show_leds("""
                . . . . .
                . # . # .
                . . # . .
                . # . # .
                . . . . .
                """)
                y = 6
                basic.show_leds("""
                . . . . .
                . # . # .
                . # . # .
                . # . # .
                . . . . .
                """)
                y = 7
                basic.show_leds("""
                . . . . .
                . # . # .
                . # # # .
                . # . # .
                . . . . .
                """)
                y = 8
                basic.show_leds("""
                . . . . .
                . # . # .
                . # . # .
                . # . # .
                . # . # .
                """)
                y = 9
                basic.show_leds("""
                . . . . .
                . # . # .
                . # # # .
                . # . # .
                . # . # .
                """)
                y = 10
                basic.show_leds("""
                . # . # .
                . # . # .
                . # . # .
                . # . # .
                . # . # .
                """)

        