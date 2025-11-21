using System;
using System.Globalization;

/* To jest wersja C# programu Better-Calc stworzona jedynie w celach treningowych
 * Dla najlepszych lepiej działającej wersji, proszę korzystać z wersji pythonowej
 * Jestem oryginalnym autorem obu wersji
 * I am very sorry for using AI, but I am horible C# programmer*/

namespace BetterCalc    
{
    class Program
    {
        static void Main(string[] args)
        {
            const string version = "0.1.0 C# - Beta";
            const string author = "Wilq1PL";

            string[] modes = {
                "Dodawanie",
                "Odejmowanie",
                "Mnożenie",
                "Dzielenie",
                "Pole kwadratu",
                "Pole prostokąta",
                "Pole trójkąta",
                "Pole trapezu",
                "Pole koła"
            };
            Console.WriteLine("Better-Calc v" + version + " by " + author);
            for (int i = 0; i < modes.Length; i++)
            {
                Console.WriteLine((i + 1) + ". " + modes[i]);
            }

            Console.WriteLine("Wybierz tryb (1-" + modes.Length + "):");
            string choice = Console.ReadLine()?.Trim() ?? "";

            if (!int.TryParse(choice, out int choiceNum) || choiceNum < 1 || choiceNum > modes.Length)
            {
                Console.WriteLine("Nieprawidłowy wybór.");
                return;
            }

            double result = 0;

            if (choiceNum >= 1 && choiceNum <= 4)
            {
                // Arytmetyka
                double num1 = ReadNumber("Podaj pierwszą liczbę (np. 3.5 lub 7/8):");
                double num2 = ReadNumber("Podaj drugą liczbę (np. 2 lub 1/3):");

                switch (choiceNum)
                {
                    case 1:
                        result = num1 + num2;
                        break;
                    case 2:
                        result = num1 - num2;
                        break;
                    case 3:
                        result = num1 * num2;
                        break;
                    case 4:
                        if (num2 != 0)
                        {
                            result = num1 / num2;
                        }
                        else
                        {
                            Console.WriteLine("Błąd: Nie można dzielić przez zero.");
                            return;
                        }
                        break;
                }

                Console.WriteLine("Wynik: " + result);
                return;
            }

            // Pole figur
            switch (choiceNum)
            {
                case 5: // Kwadrat
                    {
                        double side = ReadPositiveNumber("Podaj długość boku kwadratu:");
                        result = side * side;
                        Console.WriteLine("Pole kwadratu: " + result);
                        break;
                    }
                case 6: // Prostokąt
                    {
                        double width = ReadPositiveNumber("Podaj szerokość prostokąta:");
                        double height = ReadPositiveNumber("Podaj wysokość prostokąta:");
                        result = width * height;
                        Console.WriteLine("Pole prostokąta: " + result);
                        break;
                    }
                case 7: // Trójkąt
                    {
                        double bas = ReadPositiveNumber("Podaj długość podstawy trójkąta:");
                        double height = ReadPositiveNumber("Podaj wysokość trójkąta:");
                        result = 0.5 * bas * height;
                        Console.WriteLine("Pole trójkąta: " + result);
                        break;
                    }
                case 8: // Trapez
                    {
                        double a = ReadPositiveNumber("Podaj długość pierwszej podstawy trapezu:");
                        double b = ReadPositiveNumber("Podaj długość drugiej podstawy trapezu:");
                        double height = ReadPositiveNumber("Podaj wysokość trapezu:");
                        result = 0.5 * (a + b) * height;
                        Console.WriteLine("Pole trapezu: " + result);
                        break;
                    }
                case 9: // Koło
                    {
                        double r = ReadPositiveNumber("Podaj promień koła:");
                        result = Math.PI * r * r;
                        Console.WriteLine("Pole koła: " + result);
                        break;
                    }
                default:
                    Console.WriteLine("Nieobsługiwany tryb.");
                    break;
            }
        }

        // Wczytuje liczbę; akceptuje:
        // - liczby całkowite/zmiennoprzecinkowe (separator '.' lub ',')
        // - ułamki w postaci "a/b" (a i b mogą być liczbami zmiennoprzecinkowymi)
        // Pętla powtarza się aż do poprawnego wprowadzenia.
        static double ReadNumber(string prompt)
        {
            while (true)
            {
                Console.WriteLine(prompt);
                string? input = Console.ReadLine()?.Trim();

                if (string.IsNullOrEmpty(input))
                {
                    Console.WriteLine("Wejście nie może być puste. Spróbuj ponownie.");
                    continue;
                }

                // Obsługa ułamków w formacie a/b
                if (input.Contains("/"))
                {
                    var parts = input.Split('/');
                    if (parts.Length != 2)
                    {
                        Console.WriteLine("Nieprawidłowy format ułamka. Użyj a/b.");
                        continue;
                    }

                    string numS = parts[0].Trim().Replace(',', '.');
                    string denS = parts[1].Trim().Replace(',', '.');

                    if (double.TryParse(numS, NumberStyles.Float, CultureInfo.InvariantCulture, out double num) &&
                        double.TryParse(denS, NumberStyles.Float, CultureInfo.InvariantCulture, out double den))
                    {
                        if (den == 0)
                        {
                            Console.WriteLine("Błąd: mianownik nie może być zero.");
                            continue;
                        }
                        return num / den;
                    }
                    else
                    {
                        Console.WriteLine("Nieprawidłowe wartości w ułamku. Wprowadź liczby.");
                        continue;
                    }
                }

                // Obsługa zwykłych liczb (akceptujemy '.' i ',' jako separator dziesiętny)
                string normalized = input.Replace(',', '.');
                if (double.TryParse(normalized, NumberStyles.Float, CultureInfo.InvariantCulture, out double value))
                {
                    return value;
                }

                // Jeśli doszliśmy tu, to wejście nie jest liczbą
                Console.WriteLine("Nieprawidłowe dane: oczekiwana liczba lub ułamek. Spróbuj ponownie.");
            }
        }

        // Wczytuje liczbę większą od zera (używa ReadNumber)
        static double ReadPositiveNumber(string prompt)
        {
            while (true)
            {
                double v = ReadNumber(prompt);
                if (v <= 0)
                {
                    Console.WriteLine("Wartość musi być większa od zera. Spróbuj ponownie.");
                    continue;
                }
                return v;
            }
        }
    }
}