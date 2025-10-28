from curses.ascii import isdigit


def input_user():
    x = int(input("Enter an even number."))
    y = int(input("Enter an even number."))
    dict1 = {
        "x": x,
        "y": y
    }
    return dict1


def input_coordinates():
    on = True
    cards = []
    while on:
        checking = True
        while checking:
            x1 = int(input("Enter coordinate x card 1"))
            if not isdigit(x1):
                print("press coordinate between 1 and len of matrix ")
                break
            y1 = int(input("Enter coordinate y card 1"))
            if not isdigit(y1):
                print("press coordinate between 1 and len of matrix ")
                break
            card1 = {
                "x": x1,
                "y": y1
            }
            x2 = int(input("Enter coordinate x card 2"))
            if not isdigit(x2):
                print("press coordinate between 1 and len of matrix ")
                break
            y2 = int(input("Enter coordinate y card 2"))
            if not isdigit(y2):
                print("press coordinate between 1 and len of matrix ")
                break
            card2 = {
                "x": x2,
                "y": y2
            }
            cards.append(card1)
            cards.append(card2)
            on = False
            break
    return cards


def print_matrix(matrix):
    for vector in matrix:
        print(vector)
