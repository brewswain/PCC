def make_shirt(shirt_size='large', shirt_text='i love python'):
    """Summarize the size of the shirt and message printed on it."""
    print("\nThe shirt's size is: " + shirt_size +
          "\nThe shirt's message reads: " + shirt_text.title())


make_shirt()
make_shirt(shirt_size='medium')

make_shirt(shirt_text='hewwo UwU', shirt_size='small')
