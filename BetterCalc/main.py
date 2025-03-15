import time
import math

version = "1.0.1"
status = "beta"

def hello(ver):
    print(f"Better Calc by Wilq1PL\nv{ver}-{status}")
    time.sleep(1)
    choose_counting(selecting_menu())

def is_number(value):
    try:
        float(value)  # Sprawdzamy, czy da się przekonwertować na liczbę rzeczywistą
        return True
    except ValueError:
        return False

def get_number(prompt):
    while True:
        value = input(prompt).strip()
        if is_number(value):
            return float(value)  # Zwrot wartości jako liczby rzeczywistej
        print("❌ Podano niepoprawną wartość. Proszę wpisać liczbę.\n")

def selecting_menu():
    menu = ["Pole prostokąta", "Pole trójkąta", "Pole trapezu", "Pole koła"]

    def print_menu():
        print("\nWybierz opcję:")
        for idx, item in enumerate(menu, start=1):
            print(f"{idx}. {item}")

    while True:
        print_menu()
        selection = input("Wybieram: ").strip()

        if is_number(selection):
            selection = int(selection)
            if 1 <= selection <= len(menu):
                print(f"✅ Wybrano: {menu[selection - 1]}\n")
                time.sleep(0.25)
                return selection

        print("❌ Podano niepoprawną wartość. Proszę wpisać numer opcji.\n")

def choose_counting(selection):
    if selection == 1:
        count_rectangle()
    elif selection == 2:
        count_triangle()
    elif selection == 3:
        count_trapeze()
    elif selection == 4:
        count_circle()

def count_rectangle():
    a = get_number("Podaj wymiary pierwszego boku: ")
    b = get_number("Podaj wymiary drugiego boku: ")
    print(f"Wynikiem działania jest:\n{a * b}")

def count_triangle():
    a = get_number("Podaj długość podstawy: ")
    h = get_number("Podaj wysokość: ")
    print(f"Wynikiem działania jest:\n{(a * h) / 2}")

def count_trapeze():
    a = get_number("Podaj długość podstawy a: ")
    b = get_number("Podaj długość podstawy b: ")
    h = get_number("Podaj wysokość: ")
    print(f"Wynikiem działania jest:\n{((a + b) * h) / 2}")

def count_circle():
    r = get_number("Podaj promień koła: ")
    print(f"Wynikiem działania jest:\n{math.pi * r ** 2}")

if __name__ == "__main__":
    hello(version)
