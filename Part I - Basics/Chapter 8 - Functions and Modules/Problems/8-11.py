magicians = ['harry', 'leanansidhe', 'dresden', 'harkle']
named_magicians = []


def show_magicians(magicians, named_magicians):
    """Introduce Magicians. Move magicians to named_magicians list."""

    print("May I present, the world's greatest magicians!")

    while magicians:
        current_magician = magicians.pop()
        named_magicians.append(current_magician)


def make_great(named_magicians):
    for magician in named_magicians:
        print(magician.title() + " The Great" + "!")


show_magicians(magicians[:], named_magicians)
make_great(named_magicians)
print(magicians)
