from PIL import Image
import argparse


def make_art():
    img_choice = _get_input()
    img_file = _what_file(img_choice)
    pixels, size = _open_image(img_file)

    ascii_chars = "@%#&%*+=>:-.` "
    len_ac = len(ascii_chars)
    i = 0
    d = 2

    for y in range(0, size[1], d*2):
        for x in range(0, size[0], d):
            i += 1
            pixel = pixels[x, y]
            print(ascii_chars[int(len_ac * (pixel / 256))], end="")
        print()


def _open_image(img_arg):
    image = Image.open(img_arg).convert("L")
    pixels = image.load()
    size = image.size
    return (pixels, size)


def _get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_image', nargs=1)
    args = parser.parse_args()
    choice = args.input_image[0]
    options = ["cat", "dog", "mouse"]
    if choice not in options:
        choice = options[1]
    return choice


def _what_file(choice):
    if choice == "cat":
        img_file = "data/cat.png"
    elif choice == "dog":
        img_file = "data/dog.jpeg"
    elif choice == "mouse":
        img_file = "data/mouse.png"
    return(img_file)


if __name__ == "__main__":
    make_art()
