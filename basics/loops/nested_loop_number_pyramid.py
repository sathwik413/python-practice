for i in range(1, 4):
    digits = ""
    for n in range(1, i + 1):
        digits += str(n)
    line = " " * (3 - i) + digits
    print(line)
