def make_shirt(shirt_size, shirt_text):
    """Summarize the size of the shirt and message printed on it."""
    print("\nThe shirt's size is: " + shirt_size +
          "\nThe shirt's message reads: " + shirt_text)


# Positional arguments
make_shirt('small', 'OwO')
# Keyword arguments
make_shirt(shirt_text='hewwo UwU', shirt_size='medium')
