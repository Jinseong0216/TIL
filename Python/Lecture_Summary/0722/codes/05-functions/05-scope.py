a = 1
b = 2


def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  #

    local(500)
    print(a, b, c)  #


enclosed()

print(a, b)  #
