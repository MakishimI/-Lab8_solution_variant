import requests


def main():
    """
    Виконання Варіанту №2 Лабораторної роботи №8.
    Завдання: Вивести назву країни, столицю та регіон за введеною назвою.
    """
    print("--- Пошук інформації про країну ---")

    # 1. Програма повинна приймати з клавіатури назву країни
    country_name = input("Введіть назву країни (англійською, наприклад Ukraine, France): ").strip()

    if not country_name:
        print("Помилка: Назва країни не може бути порожньою.")
        return

    # 2. Змінна має зробити АРІ динамічним
    # Використовуємо публічний API RestCountries
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        # Виконання GET запиту
        response = requests.get(url)

        # Перевірка статусу відповіді
        if response.status_code == 200:
            # 3. Програма повинна парсувати потрібні елементи з JSON файлу в об'єкт
            data = response.json()

            # API повертає список знайдених країн, беремо перший результат
            country_info = data[0]

            # Отримання конкретних полів згідно завдання
            # Використовуємо .get() для безпечного доступу, якщо поля немає
            official_name = country_info.get('name', {}).get('official', 'Невідомо')

            # Столиця повертається як список, беремо перший елемент
            capitals = country_info.get('capital', [])
            capital = capitals[0] if capitals else 'Немає столиці'

            region = country_info.get('region', 'Невідомо')

            # 4. Дані з об'єкта вивести в консоль
            print("\n--- Результати запиту ---")
            print(f"Назва країни: {official_name}")
            print(f"Столиця:      {capital}")
            print(f"Регіон:       {region}")

        elif response.status_code == 404:
            print("\nПомилка: Країну з такою назвою не знайдено. Спробуйте ще раз.")
        else:
            print(f"\nПомилка сервера. Код статусу: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"\nПомилка з'єднання з API: {e}")
    except Exception as e:
        print(f"\nВиникла непередбачувана помилка: {e}")


if __name__ == "__main__":
    main()