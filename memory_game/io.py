def input_user():
    while True:
        x, y = "", ""
        x += (input("Enter an even number."))
        y += (input("Enter an even number."))
        if not (x.isdigit()) and (y.isdigit()):
            print("Please enter numbers only")
            continue
        else:
            x, y = int(x), int(y)
            break
    dict1 = {
        "x": x,
        "y": y
    }
    return dict1


def input_coordinates(x_y):
    x = x_y["x"]
    y = x_y["y"]
    while True:
        x1 = input("Enter coordinate X for card 1: ")
        y1 = input("Enter coordinate Y for card 1: ")
        x2 = input("Enter coordinate X for card 2: ")
        y2 = input("Enter coordinate Y for card 2: ")
        if not (x1.isdigit() and y1.isdigit() and x2.isdigit() and y2.isdigit()):
            print("Please enter numbers only.")
            continue
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        x1 -= 1
        x2 -= 1
        y1 -= 1
        y2 -= 1
        if 0 <= x1 < x and 0 <= y1 < y and \
                0 <= x2 < x and 0 <= y2 < y:
            cards = {
                "card1": {"x": x1, "y": y1},
                "card2": {"x": x2, "y": y2}
            }
            return cards
        else:
            print("Coordinates out of range! Please enter values between 0 – ", x_y)


def print_matrix(matrix):
    for vector in matrix:
        print(vector)
