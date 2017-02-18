
def inform_indicate(x, y, z):
    str_X = str(x)
    str_Y = str(y)
    str_Z = str(z)

    result = str_X + "時の" + str_Y + "は" + str_Z
    return result


if __name__ == "__main__":
    x = 12
    y = "気温"
    z = 22.4
    print(inform_indicate(x, y, z))