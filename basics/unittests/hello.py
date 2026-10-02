def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("Hello,", to)


if __name__ == "__main__":
    main()


# return the value instead of printing in hello()
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    return f"Hello, {to}"


if __name__ == "__main__":
    main()
