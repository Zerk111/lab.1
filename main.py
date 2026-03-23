from logic import analyze_movement

def main():
    print("аналізатор руху")
    user_input = input("введіть швидкості через пробіл (наприклад: 10 20 30): ")

    try:
        speed_list = [float(x) for x in user_input.split()]
        status, index = analyze_movement(speed_list)
        if status == "VIOLATION":
            print(f"результат: порушення монотонності на індексі {index}")
        else:
            print(f"результат: {status}")
    except ValueError:
        print("помилка: введіть лише числа!")

if __name__ == "__main__":
    main()