def run():
    numbers_list = [2, 28, 74, 19, 7, 0, 1007, 21, 32, 67]

    for number in numbers_list:
        if number % 2 == 0 and number != 0:
            print(f"El numero {number} es par")
        elif number % 2 != 0:
            print(f"El numero {number} es impar")
        else:
            print(f"El numero {number} es igual a 0")

if __name__ == "__main__":
    run()