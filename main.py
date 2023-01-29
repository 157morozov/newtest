while True:
    a = int(input())
    b = int(input())
    c = int(input())
    def max_of_three(a, b, c):
        if a > b:
            if a > c:
                return a
            else:
                return c
        else:
            if b > c:
                return b
            else:
                return c

    print(max_of_three(a, b, c))