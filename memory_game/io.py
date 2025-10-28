def input_user():
    x = int(input("Enter an even number."))
    y = int(input("Enter an even number."))
    dict1 = {
        "x": x,
        "y": y
    }
    return dict1


def input_coordinates():
    cards = []
    x1 = int(input("Enter coordinate x card 1"))
    y1 = int(input("Enter coordinate y card 1"))
    card1 = {
        "x": x1,
        "y": y1
    }
    x2 = int(input("Enter coordinate x card 2"))
    y2 = int(input("Enter coordinate y card 2"))
    card2 = {
        "x": x2,
        "y": y2
    }
    cards.append(card1)
    cards.append(card2)
    return cards


def print_matrix(matrix):
    for vector in matrix:
        print(vector)
