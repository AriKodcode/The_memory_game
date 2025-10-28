def create_matrix(x_y_size : dict):
    x = x_y_size['x']
    y = x_y_size['y']
    matrix = []

    if x % 2 == 0 and y % 2 == 0:
        if x_y_size['x'] and x_y_size['y'] == 2:
            return True
        else:
           for i in range(x):
               vector = []
               for j in range(y):
                   vector.append('x')
               matrix.append(vector)
        return matrix
    else:
        return False




