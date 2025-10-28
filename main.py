from memory_game.game import create_matrix, create_cards, shuffling_cards, matrix_initialization_for_x, matrix_mixing, \
    check_matrix, check_coordinates
from memory_game.io import input_user, input_coordinates,print_matrix


def play():
    print("\033[34mWellcome to the \n\033[35m MEMORY GAME!\033[0m \n  \033[36mgood luck!\033[0m")
    game = True
    while game:
        x_y = input_user()
        matrix = create_matrix(x_y)
        check_mat = check_matrix(matrix)
        if check_mat and check_mat != "win":
            print("\033[34mYou created a memory board.\033[0m")
            print_matrix(matrix)
            cards = shuffling_cards(create_cards(x_y))
            original_matrix = matrix_mixing(matrix, cards)
            play_game = True
            input("\033[34mIf you want to start the game press Enter.\033[0m")
            print("\033[34mGame started\033[0m")
            new_matrix = matrix_initialization_for_x(create_matrix(x_y))
            print_matrix(new_matrix)

            while play_game:

                for y in range(len(new_matrix)):
                    for x in range(len(new_matrix[y])):
                        if original_matrix[y][x] != new_matrix[y][x]:
                            continue
                        else:
                            play_game = False
                            game = False
                            break
                coordinates = input_coordinates()
                checking = check_coordinates(coordinates,x_y)
                if checking:
                    if new_matrix[coordinates["card1"]["x"]][coordinates["card1"]["y"]] and \
                            new_matrix[coordinates["card2"]["x"]][coordinates["card2"]["y"]] == \
                            original_matrix[coordinates["card1"]["x"]][coordinates["card1"]["y"]] and \
                            original_matrix[coordinates["card2"]["x"]][coordinates["card2"]["y"]]:
                        print("You already guessed it.")
                    elif original_matrix[coordinates["card1"]["x"]][coordinates["card1"]["y"]] == \
                            original_matrix[coordinates["card2"]["x"]][coordinates["card2"]["y"]]:
                        new_matrix[coordinates["card1"]["x"]][coordinates["card1"]["y"]] = \
                            original_matrix[coordinates["card1"]["x"]][coordinates["card1"]["y"]]
                        new_matrix[coordinates["card1"]["x"]][coordinates["card1"]["y"]] = \
                            original_matrix[coordinates["card1"]["x"]][coordinates["card1"]["y"]]
                    else:
                        print("Bad guess")

        if check_mat == "win":
            continue_playing = input("Continue playing? prees y/n")
            if continue_playing == "y":
                print("Continue")
            else:
                print("end game")
                break
        elif not check_mat:
            print("\033[34mError mot even num input\033[0m")

    return "you win the game"




if __name__ == "__main__":
    play()
