import random
import string
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Toddler Learning Game"

class ToddlerGame(arcade.Window):
    """Simple letter matching game."""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.current_letter = None
        self.score = 0
        self.attempts = 0
        self.max_rounds = 10
        self._next_letter()

    def _next_letter(self):
        self.current_letter = random.choice(string.ascii_uppercase)
        self.attempts += 1

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            f"Type the letter: {self.current_letter}",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            arcade.color.BLACK,
            60,
            anchor_x="center",
        )
        arcade.draw_text(
            f"Score: {self.score}",
            10,
            SCREEN_HEIGHT - 40,
            arcade.color.DARK_BLUE,
            24,
        )

    def on_key_press(self, key, modifiers):
        if key == getattr(arcade.key, self.current_letter):
            self.score += 1
        if self.attempts < self.max_rounds:
            self._next_letter()
        else:
            print(f"Final Score: {self.score}/{self.max_rounds}")
            arcade.close_window()


def main():
    ToddlerGame()
    arcade.run()


if __name__ == "__main__":
    main()
