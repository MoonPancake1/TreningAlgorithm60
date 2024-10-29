x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if x > x2 and y > y2:
    print("NE")
elif x > x2 and y2 >= y >= y1:
    print("E")
elif x > x2 and y < y1:
    print("SE")
elif x2 >= x >= x1 and y > y2:
    print("N")
elif x < x1 and y > y2:
    print("NW")
elif x < x1 and y2 >= y >= y1:
    print("W")
elif x < x1 and y < y1:
    print("SW")
elif x2 >= x >= x1 and y < y1:
    print("S")