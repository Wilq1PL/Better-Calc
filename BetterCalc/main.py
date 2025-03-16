import time
import math

version = "1.0.0"
status = "Full release"

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
    menu = ["Pole prostokąta", "Pole trójkąta", "Pole trapezu", "Pole koła", "Gęstość", "Masę", "Objętość", "Prędkość", "Czas", "Drogę"]

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

    elif selection == 5:
        count_density()

    elif selection == 6:
        count_mass()
    elif selection == 7:
        count_volume()

    elif selection == 8:
        count_velocity()

    elif selection == 9:
        count_time()

    elif selection == 10:
        count_street()

def count_rectangle():
    a = get_number("Podaj wymiary pierwszego boku (w metrach): ")
    b = get_number("Podaj wymiary drugiego boku (w metrach): ")
    print(f"Wynikiem działania jest:\n{a * b}m")
    time.sleep(10)

def count_triangle():
    a = get_number("Podaj długość podstawy (w metrach): ")
    h = get_number("Podaj wysokość (w metrach): ")
    print(f"Wynikiem działania jest:\n{(a * h) / 2}m")
    time.sleep(10)

def count_trapeze():
    a = get_number("Podaj długość podstawy a (w metrach): ")
    b = get_number("Podaj długość podstawy b (w metrach): ")
    h = get_number("Podaj wysokość (w metrach): ")
    print(f"Wynikiem działania jest:\n{((a + b) * h) / 2}m")
    time.sleep(10)

def count_circle():
    r = get_number("Podaj promień koła (w metrach): ")
    print(f"Wynikiem działania jest:\n{math.pi * r ** 2}m")
    time.sleep(10)

def count_density():
    m = get_number("Podaj masę (w kilogramach): ")
    V = get_number("Podaj objętość (w metrach sześciennych): ")
    print(f"Wynikiem działania jest:\n{m / V}kg/m3")
    time.sleep(10)

def count_mass():
    V = get_number("Podaj masę (w kilogramach): ")
    d = get_number("Podaj gęstość (w kilogramach na metr sześcienny: ")
    print(f"Wynikiem działania jest:\n{V * d}kg")
    time.sleep(10)

def count_volume():
    m = get_number("Podaj masę (w kilogramach): ")
    d = get_number("Podaj gęstość (w kilogramach na metr sześcienny): ")
    print(f"Wynikiem działania jest:\n{m / d}m3")
    time.sleep(10)

def count_velocity():
    s = get_number("Podaj drogę (w m): ")
    t = get_number("Podaj czas (w s): ")
    print(f"Wynikiem działania jest:\n{s / t}m/s")
    time.sleep(10)

def count_time():
    s = get_number("Podaj drogę (w m): ")
    v = get_number("Podaj średnią prędkość (w m/s): ")
    print(f"Wynikiem działania jest:\n{s / v}s")
    time.sleep(10)

def count_street():
    v = get_number("Podaj średnią prędkość (w m/s): ")
    t = get_number("Podaj czas (w s): ")
    print(f"Wynikiem działania jest:\n{v * t}m")
    time.sleep(10)

if __name__ == "__main__":
    hello(version)
