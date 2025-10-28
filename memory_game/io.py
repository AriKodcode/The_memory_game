def input_user():
    x = int(input("Enter an even number."))
    y = int(input("Enter an even number."))
    dict1 = {
        "x": x,
        "y": y
    }
    return dict1


def input_coordinates(x_y):
    x = x_y["x"]
    y = x_y["y"]
    while True:
        cards = {}
        x1 = (input("Enter coordinate x card 1"))
        y1 = (input("Enter coordinate y card 1"))
        card1 = {
            "x": x1,
            "y": y1
        }
        x2 = (input("Enter coordinate x card 2"))
        y2 = (input("Enter coordinate y card 2"))
        card2 = {
            "x": x2,
            "y": y2
        }
        cards.update(card1)
        cards.update(card2)
        if 0 < cards[card1]["x"] < len(x) and 0 < cards[card1]["y"] < len(y) and 0 < cards[card2]["x"] < len(x) and 0 < cards[card2]["y"] < len(y):
            if int(cards[card1]["x"]) and int(cards[card1]["y"]) and int(cards[card2]["x"]) and int(cards[card2]["y"]):
                break
    return cards





def print_matrix(matrix):
    for vector in matrix:
        print(vector)
