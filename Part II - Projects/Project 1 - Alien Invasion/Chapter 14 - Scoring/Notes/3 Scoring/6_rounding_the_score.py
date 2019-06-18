"""
Most arcade-style shooting games report scores as multiples of 10, so let's follow that lead
with our scoring. Let's also format the score to include comma separators in large numbers.
We'll make this change in Scoreboard:
"""

# scoreboard.py


def prep_score(self):
    """Turn the score into a rendered image."""
    rounded_score = int(round(self.stats.score, -1))
    score_str = "{:,}".format(rounded_score)
    self.score_image = self.font.render(
        score_str, True, self.text_color, self.ai_settings.bg_color)


"""
The round() function normally rounds a decimal number to a set number of decimal places given as 
the second argument. However, if you pass a negative number as the second argument, round() 
will round the value to the nearest 10, 100, 1000, and so on. The code at line 12 tells Python
to round the value of stats.score to the nearest 10 and store it in rounded_score.

At line 13, a string formatting directive tells Python to insert commas into numbers when 
converting a numerical value to a string- for example, to output 1,000,000 instead of 1000000.
Now when you run the game, you should see a neatly formatted, rounded score even when you rack 
up lots of points.
"""
