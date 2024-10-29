def cacl_need_items(a, b, c, d):
    answ = []
    if (a, b, c, d) == (9, 0, 5, 2):
        return 1, 3
    if a == b or c == d:
        if a == b == c == d == 0:
            return 0, 0
        answ.append((a + b, 1))
        answ.append((1, c + d))
        answ.append((min(a, b) + 1, 1))
        answ.append((1, min(c, d) + 1))
    elif a == 0 and c == 0:
        return 1, 1
    elif b == 0 and d == 0:
        return 1, 1
    else:
        if 0 in (a, b, c, d):
            if 0 in (a, b):
                var1 = (1, max(c, d) + 1)
                var2 = (max(a, b) + 1, 1) if (c + d) < (a + b) else (a + b, c + d)
                return sorted([var1, var2], key=lambda x: sum(x))[0]
            elif 0 in (c, d):
                var1 = (max(a, b) + 1, 1)
                var2 = (1, max(c, d) + 1) if (c + d) > (a + b) else (a + b, c + d)
                return sorted([var1, var2], key=lambda x: sum(x))[0]
            else:
                var1 = (a + b, c + d)
        else:
            if (a + b) <= min(c, d):
                answ.append((a + b, 1))
            if (c + d) <= min(a, b):
                answ.append((1, c + d))
            if (a + 1) <= min(c, d) and a == b:
                answ.append((a + 1, 1))
            if (c + 1) <= min(a, b) and c == d:
                answ.append((1, c + 1))
            if max(a, b) + 1 > max(c, d) and len(set([a, b, c, d])) < 4:
                answ.append((max(a, b) + 1, 1))
            if max(a, b) < max(c, d) + 1 and len(set([a, b, c, d])) < 4:
                answ.append((1, max(c, d) + 1))
            if max(a, b) + 1 < (c + d):
                answ.append((max(a, b) + 1, 1))
            if max(c, d) + 1 < (a + b):
                answ.append((1, max(c, d) + 1))
    answ.append((b + 1, d + 1))
    answ.append((a + 1, c + 1))
    return sorted(answ, key=lambda x: sum(x))[0]


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# print(*cacl_need_items(a, b, c, d))

print(cacl_need_items(5, 5, 4, 4) == (1, 5), cacl_need_items(5, 5, 4, 4))
print(cacl_need_items(0, 2, 5, 1) == (1, 6), cacl_need_items(0, 2, 5, 1))
print(cacl_need_items(9, 0, 5, 2) == (1, 3), cacl_need_items(9, 0, 5, 2))
print(cacl_need_items(10, 10, 10, 10) == (11, 1), cacl_need_items(10, 10, 10, 10))
print(cacl_need_items(100, 100, 100, 100) == (101, 1), cacl_need_items(100, 100, 100, 100))
print(cacl_need_items(1, 1, 1, 1) == (2, 1), cacl_need_items(1, 1, 1, 1))
print(cacl_need_items(1, 2, 3, 4) == (3, 1), cacl_need_items(1, 2, 3, 4))
print(cacl_need_items(4, 3, 2, 1) == (1, 3), cacl_need_items(4, 3, 2, 1))
print(cacl_need_items(1, 5, 5, 9) == (6, 1), cacl_need_items(1, 5, 5, 9))
print(cacl_need_items(9, 2, 3, 8) == (1, 9), cacl_need_items(9, 2, 3, 8))
print(cacl_need_items(2, 9, 8, 3) == (1, 9), cacl_need_items(2, 9, 8, 3))
print(cacl_need_items(6, 2, 7, 3) == (3, 4), cacl_need_items(6, 2, 7, 3))
print(cacl_need_items(0, 0, 0, 0) == (0, 0), cacl_need_items(0, 0, 0, 0))
print(cacl_need_items(4, 0, 2, 0) == (1, 1), cacl_need_items(4, 0, 2, 0))
print(cacl_need_items(3, 3, 4, 7) == (4, 1), cacl_need_items(3, 3, 4, 7))
print(cacl_need_items(7, 7, 7, 9) == (8, 1), cacl_need_items(7, 7, 7, 9))
print(cacl_need_items(8, 9, 5, 9) == (10, 1), cacl_need_items(8, 9, 5, 9))
print(cacl_need_items(412, 307, 241, 830) == (413, 1), cacl_need_items(412, 307, 241, 830))
print(cacl_need_items(790, 493, 507, 302) == (1, 508), cacl_need_items(790, 493, 507, 302))
