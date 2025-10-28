from random import randrange


def create_matrix(x_y_size: dict):
    x = x_y_size['x']
    y = x_y_size['y']
    matrix = []

    if x % 2 == 0 and y % 2 == 0:
        if x_y_size['x'] and x_y_size['y'] == 2:
            return "win"
        else:
            for i in range(x):
                vector = []
                for j in range(y):
                    vector.append("")
                matrix.append(vector)
        return matrix
    else:
        return False


def create_cards(x_y_size: dict):
    card_list = []
    x = x_y_size["x"]
    y = x_y_size["y"]
    num_card = (x * y) // 2
    for num in range(num_card):
        card_list.append(num)
        card_list.append(num)

    return card_list


def shuffling_cards(deck: list):
    result = deck
    for i in range(1000):
        index1 = randrange(len(deck))
        index2 = randrange(len(deck))
        if index1 == index2:
            continue
        else:
            result[index1], result[index2] = result[index2], result[index1]
    return result


def matrix_initialization_for_x(matrix: list):
    for vector in matrix:
        for char in range(len(vector)):
            vector[char] = "x"
    return matrix


def matrix_mixing(matrix: list, shuffling_cards2: list):
    counter = 0
    for vector in matrix:
        for char in range(len(vector)):
            vector[char] = str(shuffling_cards2[counter])
            counter += 1
    return matrix

def check_matrix(check):
    if check:
        return check
    elif check == "win":
        return "win"
    elif not check:
        return False
    else:
        return False


def check_coordinates(coordinates: dict, x_y: dict):
    x = x_y["x"]
    y = x_y["y"]
    card1 = coordinates["card1"]
    card2 = coordinates["card1"]
    if 0 < card1["x"] < x and 0 < card1["y"] < y and 0 < card2["x"] < x and 0 < card2["y"] < y:
        return True
    else:
        return False