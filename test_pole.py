from manimlib import *
import numpy as np



class magnet(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=1)
        circle.set_stroke(WHITE, width=4)
        square = Square()

        self.play(ShowCreation(square))
        # self.play(ShowCreation(circle))
        # self.wait(5)
        #
        # self.embed()


        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEG))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
            In general, using the interactive shell
            is very helpful when developing new scenes
        """)
        self.play(Write(text))


        always(circle.move_to, self.mouse_point)


