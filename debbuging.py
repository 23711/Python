def divider(num):
    dividers = []
    for i in range(1, num + 1):
        if num % i == 0:
            dividers.append(i)

    return dividers


def run():
    # try:
    #     num = int(input("Give me a number: "))
    #     print(divider(num))
    # except ValueError:
    #     print("you need a number")

    num = input("Give me a number: ")
    assert num.isnumeric() , "It must be a number"


if __name__ == "__main__":
    run()