import random


def surrounding_cells(rand_wall, maze):
    s_cells = 0
    if maze[rand_wall[0] - 1][rand_wall[1]] == 'c':
        s_cells += 1
    if maze[rand_wall[0] + 1][rand_wall[1]] == 'c':
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1] - 1] == 'c':
        s_cells += 1
    if maze[rand_wall[0]][rand_wall[1] + 1] == 'c':
        s_cells += 1

    return s_cells


wall = 'w'
cell = 'c'
unvisited = 'u'


def create_maze(width, height, crystal_amount, monster_amount):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)

    # Рандомно вибираем стартовую точку
    starting_height = int(random.random() * height)
    starting_width = int(random.random() * width)
    if starting_height == 0:
        starting_height += 1
    if starting_height == height - 1:
        starting_height -= 1
    if starting_width == 0:
        starting_width += 1
    if starting_width == width - 1:
        starting_width -= 1

    # Обозначаем стартовую клетку и делаем клетки вокруг нее стенами
    maze[starting_height][starting_width] = cell
    walls = [[starting_height - 1, starting_width], [starting_height, starting_width - 1],
             [starting_height, starting_width + 1], [starting_height + 1, starting_width]]

    # Добавляем стены в maze
    maze[starting_height - 1][starting_width] = 'w'
    maze[starting_height][starting_width - 1] = 'w'
    maze[starting_height][starting_width + 1] = 'w'
    maze[starting_height + 1][starting_width] = 'w'
    while walls:
        # Выбираем рандомную стену
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Проверяем левую стену
        if rand_wall[1] != 0:
            if maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == 'c':
                # Находим число соседних клеток
                s_cells = surrounding_cells(rand_wall, maze)

                if s_cells < 3:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Добавляем новые стены
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0] - 1][rand_wall[1]] != 'c':
                            maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    if rand_wall[0] != height - 1:
                        if maze[rand_wall[0] + 1][rand_wall[1]] != 'c':
                            maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1] - 1] != 'c':
                            maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Проверяем верхнюю стену
        if rand_wall[0] != 0:
            if maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == 'c':

                s_cells = surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Добавляем новые стены
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0] - 1][rand_wall[1]] != 'c':
                            maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1] - 1] != 'c':
                            maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    if rand_wall[1] != width - 1:
                        if maze[rand_wall[0]][rand_wall[1] + 1] != 'c':
                            maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Проверяем нижнюю стену
        if rand_wall[0] != height - 1:
            if maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] - 1][rand_wall[1]] == 'c':

                s_cells = surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Добавляем стены
                    if rand_wall[0] != height - 1:
                        if maze[rand_wall[0] + 1][rand_wall[1]] != 'c':
                            maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if rand_wall[1] != 0:
                        if maze[rand_wall[0]][rand_wall[1] - 1] != 'c':
                            maze[rand_wall[0]][rand_wall[1] - 1] = 'w'
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if rand_wall[1] != width - 1:
                        if maze[rand_wall[0]][rand_wall[1] + 1] != 'c':
                            maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Проверяем правую стену
        if rand_wall[1] != width - 1:
            if maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == 'c':

                s_cells = surrounding_cells(rand_wall, maze)
                if s_cells < 2:
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Добавляем новые стены
                    if rand_wall[1] != width - 1:
                        if maze[rand_wall[0]][rand_wall[1] + 1] != 'c':
                            maze[rand_wall[0]][rand_wall[1] + 1] = 'w'
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if rand_wall[0] != height - 1:
                        if maze[rand_wall[0] + 1][rand_wall[1]] != 'c':
                            maze[rand_wall[0] + 1][rand_wall[1]] = 'w'
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if rand_wall[0] != 0:
                        if maze[rand_wall[0] - 1][rand_wall[1]] != 'c':
                            maze[rand_wall[0] - 1][rand_wall[1]] = 'w'
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Удаляем стену
        for wall in walls:
            if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                walls.remove(wall)

    # Обозначаем оставшиеся клетки как стены
    for i in range(0, height):
        for j in range(0, width):
            if maze[i][j] == 'u':
                maze[i][j] = 'w'

    # Добавляем кристаллы и монстров
    # m - монстр
    # k - кристалл
    while monster_amount:
        x, y = int(random.random() * width), int(random.random() * width)
        if 0 < x < width - 1 and 0 < y < width - 1:
            if maze[x][y] == 'c':
                maze[x][y] = 'm'
                monster_amount -= 1
    while crystal_amount:
        x, y = int(random.random() * width), int(random.random() * width)
        if 0 < x < width - 1 and 0 < y < width - 1:
            if maze[x][y] == 'c':
                maze[x][y] = 'k'
                crystal_amount -= 1

    # Добавляем вход и выход
    # t - телепорт
    # e - вход
    t = 1
    e = 1
    while e:
        x = int(random.random() * width)
        if 0 < x < width - 1:
            if maze[-3][x] == 'c':
                maze[-2][x] = 'e'
                e -= 1

    while t:
        x = int(random.random() * width)
        if 0 < x < width - 1:
            if maze[2][x] == 'c':
                maze[1][x] = 't'
                t -= 1

    return maze
