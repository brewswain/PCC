"""
Now let's add the ship to our game. To draw the player's ship on screen, we'll load an image
and then use the Pygame method blit() to draw the image. 

When choosing artwork for your games, be sure to pay attention to licensing. 
The safest and cheapest way to start is to use freely licensed graphics that you can modify
from a website like http://pixabay.com/.

You can use almost any type of image file in your game, but it's easiest ig you use a bitmap
(.bmp) file because Pygame loads bitmaps by default. Although you can configure Pygame to use 
other file types, some file types depend on certain image libraries that must be installed
on your computer. (Most images you'll find are in .jpg, .png, or .gif formats, but you can
convert them to bitmaps using photoshop etc.)

Obviously, try to find a file with a transparent background that you can replace with any bg
colour  using an image editor. Your games will look best if the image's bg colour matches 
your own game's background colour. Alternatively, you can match your game's background to the
image's background.

Make a folder called images inside your main project folder. Save the file ship.bmp in the
images folder.
"""
