from proekt320Arsen import funk320Arsen

def main():
    x = int(input("Ввод x: "))
    y = int(input("Ввод y: "))

    result = funk320Arsen(x, y)

    print("Тестирование функции funk320Arsen")
    print(f"x = {x}, y = {y}")
    print(f"Результат = {result}")

if __name__ == "__main__":
    main()