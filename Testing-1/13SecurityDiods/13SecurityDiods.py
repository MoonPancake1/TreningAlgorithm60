def analyze_matrix(n: int, m: int, n_matrix: list) -> tuple:
    coords_normal = []
    cnt_active_diods_normal = 0
    need_find_symb = "#"
    background_symb = "."
    for y in range(n):
        for x in range(m):
            if n_matrix[y][x] == need_find_symb:
                cnt_active_diods_normal += 1
            elif n_matrix[y][x] == background_symb:
                if x == 0 or n_matrix[y][x - 1] == need_find_symb:
                    coords_normal.append([x + 1, n - y])
                elif x == (m - 1) or n_matrix[y][x + 1] == need_find_symb:
                    coords_normal.append([x + 1, n - y])
    return coords_normal, cnt_active_diods_normal


def calculate_rectangle_diods(coords: list) -> list:
    rectangle_diods = []
    now_rectangle_diods = [(-1, -1), (-1, -1)]
    for i in range(len(coords) - 1):
        if coords[i][1] == coords[i + 1][1]:
            if now_rectangle_diods == [(-1, -1), (-1, -1)]:
                now_rectangle_diods = [(coords[i]), (coords[i + 1])]
            else:
                now_rectangle_diods = [(now_rectangle_diods[0]), (coords[i + 1])]
        elif (coords[i][0] == coords[i + 1][0]) and (abs(coords[i][1] - coords[i + 1][1]) == 1):
            if now_rectangle_diods == [(-1, -1), (-1, -1)]:
                now_rectangle_diods = [(coords[i]), (coords[i + 1])]
            else:
                now_rectangle_diods = [(now_rectangle_diods[0]), (coords[i + 1])]
        elif abs(coords[i][1] - coords[i + 1][1]) == 1:
            try:
                if coords[i + 1][1] == coords[i + 2][1] and i > 0:
                    if coords[i][1] != coords[i - 1][1]:
                        rectangle_diods.append((coords[i], coords[i]))
                elif coords[i + 1][1] == coords[i + 2][1] and i == 0:
                    rectangle_diods.append((coords[i], coords[i]))
            except IndexError as e:
                if coords[i - 1][1] == coords[i][1]:
                    rectangle_diods.append((coords[i], coords[i]))
        else:
            if len(coords) > 1 and now_rectangle_diods == [(-1, -1), (-1, -1)]:
                rectangle_diods.append((coords[i], coords[i]))
            else:
                rectangle_diods.append(now_rectangle_diods)
            now_rectangle_diods = [(-1, -1), (-1, -1)]
    if len(rectangle_diods) >= 1:
        if rectangle_diods[-1] != now_rectangle_diods and now_rectangle_diods != [(-1, -1), (-1, -1)]:
            rectangle_diods.append(now_rectangle_diods)
        elif len(coords) == 2 and len(rectangle_diods) == 1:
            if rectangle_diods[0][0] == rectangle_diods[0][1]:
                rectangle_diods.append((coords[1], coords[1]))
    else:
        if now_rectangle_diods != [(-1, -1), (-1, -1)]:
            if len(now_rectangle_diods) == 1:
                rectangle_diods.append((now_rectangle_diods, now_rectangle_diods))
            else:
                rectangle_diods.append(now_rectangle_diods)
        elif len(coords) == 1:
            rectangle_diods.append((coords[0], coords[0]))
    return rectangle_diods


def rot90(matrix):
    return list(zip(*matrix[::-1]))


def crop_martix_func(n: int, n_matrix: list) -> list:

    new_matrix = []
    active_diods = []

    for i in range(len(n_matrix)):
        cnt_deact_diods = 0
        for j in range(len(n_matrix[i])):
            if n_matrix[i][j] == ".":
                cnt_deact_diods += 1
            elif n_matrix[i][j] == "#":
                active_diods.append([j + 1, i + 1])
        if cnt_deact_diods < n:
            new_matrix.append(n_matrix[i])

    return new_matrix, active_diods


def this_I(n: int, m: int, cnt_active_diods_normal: int, active_diods: list) -> bool:
    if len(active_diods) == 2:
        if abs(active_diods[0][0] - active_diods[1][0]) > 1 or abs(active_diods[0][1] - active_diods[1][1]) > 1:
            return False
    if n * m == cnt_active_diods_normal:
        return True
    return False


def this_O(n: int, m: int, rectangles: list, cnt_active_diods_normal: int) -> bool:
    if len(rectangles) == 1 and rectangles != [[[1, n], [m, 1]]]:
        x3, y3 = rectangles[0][0]
        x4, y4 = rectangles[0][1]
        if x3 != 1 and y3 != n:
            if x4 != n and y4 != n:
                return True
    return False


def this_C(n: int, m: int, rectangles: list) -> bool:
    if len(rectangles) == 1:
        x3, y3 = rectangles[0][0]
        x4, y4 = rectangles[0][1]
        if x3 != 1 and 1 < y3 < n:
            if x4 != 1 and 1 < y4 < n:
                return True
    return False


def this_L(n: int, m: int, rectangles: list) -> bool:
    if len(rectangles) == 1:
        x3, y3 = rectangles[0][0]
        x4, y4 = rectangles[0][1]
        if x3 != 1 and y3 == n:
            if x4 == m and y4 > 1:
                return True
    return False


def this_H(n: int, m: int, rectangles: list, cnt_active_diods_normal: int) -> bool:
    if len(rectangles) == 2:
        s = n * m
        need_diactive_diods_normal = n * m - cnt_active_diods_normal
        x3, y3 = rectangles[0][0]
        x4, y4 = rectangles[0][1]
        x5, y5 = rectangles[1][0]
        x6, y6 = rectangles[1][1]
        need_diactive_diods_practic = ((x4 - x3 + 1) * (y3 - y4 + 1) + (x6 - x5 + 1) * (y5 - y6 + 1))
        if need_diactive_diods_practic == need_diactive_diods_normal:
            if (1 < x3 <= x4) and (y3 == n):
                if x4 < m:
                    if 1 < x5 == x3 <= x6 and y5 >= y6:
                        if x6 < m and y6 == 1:
                            return True
    return False


def this_P(n: int, m: int, rectangles: list) -> bool:
    if len(rectangles) == 2:
        x3, y3 = rectangles[0][0]
        x4, y4 = rectangles[0][1]
        x5, y5 = rectangles[1][0]
        x6, y6 = rectangles[1][1]
        if 1 < x3 <= x4 and n > y3 >= y4:
            if x4 < n and y4 > y5:
                if 1 < x5 == x3 <= x6 and y5 >= y6:
                    if x6 == m and y6 == 1:
                        return True
    return False


def diods_func(n: int, n_matrix: list) -> str:
    crop_matrix, active_diods = crop_martix_func(n, n_matrix)
    if len(crop_matrix) > 0:
        rotate_matrix = rot90(crop_matrix)
        crop_matrix, active_diods_new = crop_martix_func(len(rotate_matrix[0]), rotate_matrix)
        rotate_matrix = rot90(rot90(rot90(crop_matrix)))
        n, m = len(rotate_matrix), len(rotate_matrix[0])
        coords_normal, cnt_active_diods_normal = analyze_matrix(n, m, rotate_matrix)
        rectangles_normal = calculate_rectangle_diods(coords_normal)
        if this_I(n, m, cnt_active_diods_normal, active_diods):
            return "I"
        elif this_O(n, m, rectangles_normal, cnt_active_diods_normal):
            return "O"
        elif this_C(n, m, rectangles_normal):
            return "C"
        elif this_L(n, m, rectangles_normal):
            return "L"
        elif this_H(n, m, rectangles_normal, cnt_active_diods_normal):
            return "H"
        elif this_P(n, m, rectangles_normal):
            return "P"
        else:
            return "X"
    return "X"


if __name__ == '__main__':
    DEBUG = False
    if DEBUG:
        n = int(input())
        n_matrix = [input() for _ in range(n)]
        crop_matrix, active_diods = crop_martix_func(n, n_matrix)
        if len(crop_matrix) > 0:
            rotate_matrix = rot90(crop_matrix)
            crop_matrix, active_diods_new = crop_martix_func(len(rotate_matrix[0]), rotate_matrix)
            rotate_matrix = rot90(rot90(rot90(crop_matrix)))
            [print(*line) for line in rotate_matrix]
            n_test, m_test = len(rotate_matrix), len(rotate_matrix[0])
            # print(n_test, m_test) # Ширина и длина соответственно
            coords_normal, cnt_active_diods_normal = analyze_matrix(n_test, m_test, rotate_matrix)
            rectangles_normal = calculate_rectangle_diods(coords_normal)
            print(coords_normal)
            print(calculate_rectangle_diods(coords_normal))
            print(diods_func(n, n_matrix))
        else:
            print("X")
    else:
        with open('./input.txt', 'r') as f:
            lines = [line[:-1] for line in f.readlines()]

        ns = [str(j) for j in range(1, 11)]
        i = 0
        n_test = 1
        suc_test = 1

        while i <= len(lines):
            try:
                if lines[i] in ns:
                    n = int(lines[i])
                    n_matrix = lines[i + 1: i + n + 1]
                    # try:
                    result = diods_func(n, n_matrix)
                    answ = lines[i + n + 1]
                    if answ == result:
                        print(f"Test №{n_test} ({i + 1}-{i + n + 2}) - [OK]: Return: {result}, Answer: {answ}")
                        suc_test += 1
                    else:
                        print(f"Test №{n_test} ({i + 1}-{i + n + 2}) - [FAIL]: Return: {result}, Answer: {answ}")
                    # i += 1 + n + 1
                    # except Exception as e:
                    #     print(f"Test №{n_test} ({i + 1}-{i + n + 2}) - [FAIL]: Return: {e}, Answer: {answ}")
                    i += 1 + n + 1
                elif lines[i] == '':
                    n_test += 1
                    i += 1
            except IndexError:
                break

        print(f"Прошло тестов: {suc_test}/{n_test}")
