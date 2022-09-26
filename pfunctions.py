from PIL import Image


def to_black_and_white(name):
    image = Image.open("data/color/" + name + ".jpg")
    # open our photo
    grayscale = image.convert('L')
    black_and_white = image.convert('1')
    # convert
    grayscale.save("data/grayscale/" + name + ".jpg")
    black_and_white.save("data/wb/" + name + ".jpg")
    # save
