import csv
import json
import os


def create_initial_files():
    """Создает students.csv и products.json для работы"""
    
    # Создаем students.csv
    students_data = [
        {"Имя": "Иван", "Фамилия": "Петров", "Группа": "ПИН-231", "Возраст": "19", "Средний_балл": "4.5"},
        {"Имя": "Анна", "Фамилия": "Сидорова", "Группа": "ПИН-231", "Возраст": "20", "Средний_балл": "4.8"},
        {"Имя": "Петр", "Фамилия": "Иванов", "Группа": "ПИН-232", "Возраст": "18", "Средний_балл": "3.9"},
        {"Имя": "Мария", "Фамилия": "Кузнецова", "Группа": "ПИН-232", "Возраст": "19", "Средний_балл": "4.9"},
        {"Имя": "Алексей", "Фамилия": "Смирнов", "Группа": "ПИН-231", "Возраст": "20", "Средний_балл": "4.2"},
        {"Имя": "Елена", "Фамилия": "Попова", "Группа": "ПИН-233", "Возраст": "19", "Средний_балл": "5.0"},
        {"Имя": "Дмитрий", "Фамилия": "Васильев", "Группа": "ПИН-233", "Возраст": "21", "Средний_балл": "3.7"}
    ]
    
    with open("students.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Имя", "Фамилия", "Группа", "Возраст", "Средний_балл"])
        writer.writeheader()
        writer.writerows(students_data)
    print("✅ Создан файл: students.csv")
    
    # Создаем products.json
    products_data = [
        {"id": 1, "name": "Ноутбук", "price": 50000, "quantity": 10},
        {"id": 2, "name": "Мышь", "price": 1500, "quantity": 50},
        {"id": 3, "name": "Клавиатура", "price": 3000, "quantity": 25}
    ]
    
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products_data, f, ensure_ascii=False, indent=4)
    print("✅ Создан файл: products.json")



def csv_to_json(csv_filename, json_filename):
    """
    Преобразует CSV файл в JSON файл.
    
    Args:
        csv_filename (str): Имя CSV файла
        json_filename (str): Имя JSON файла
    """
    data = []
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Преобразуем типы данных
                for key in row:
                    if row[key].replace('.', '').replace('-', '').isdigit():
                        if '.' in row[key]:
                            row[key] = float(row[key])
                        else:
                            row[key] = int(row[key])
                data.append(row)
        
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f"✅ Успешно преобразовано: {csv_filename} → {json_filename}")
        print(f"   Записей: {len(data)}")
        return True
    except FileNotFoundError:
        print(f"❌ Ошибка: файл {csv_filename} не найден")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


def students_csv_to_json(csv_filename, json_filename):
    """
    Читает CSV со студентами и преобразует в JSON.
    Добавляет вычисляемые поля.
    """
    students = []
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                avg_score = float(row['Средний_балл'])
                
                # Определяем статус
                if avg_score >= 4.5:
                    status = "отличник"
                elif avg_score >= 3.5:
                    status = "хорошист"
                else:
                    status = "нужно учиться"
                
                student = {
                    "full_name": f"{row['Имя']} {row['Фамилия']}",
                    "group": row['Группа'],
                    "age": int(row['Возраст']),
                    "average_score": avg_score,
                    "status": status
                }
                students.append(student)
        
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(students, json_file, ensure_ascii=False, indent=4)
        
        print(f"✅ Конвертация завершена!")
        for s in students:
            print(f"   {s['full_name']}: {s['status']}")
        return True
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False



def json_to_csv(json_filename, csv_filename):
    """
    Преобразует JSON файл в CSV файл.
    
    Args:
        json_filename (str): Имя JSON файла
        csv_filename (str): Имя CSV файла
    """
    try:
        with open(json_filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        if not data:
            print("❌ JSON файл пуст")
            return False
        
        headers = list(data[0].keys())
        
        with open(csv_filename, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"✅ Успешно преобразовано: {json_filename} → {csv_filename}")
        print(f"   Записей: {len(data)}")
        return True
    except FileNotFoundError:
        print(f"❌ Ошибка: файл {json_filename} не найден")
        return False
    except json.JSONDecodeError:
        print(f"❌ Ошибка: файл {json_filename} содержит некорректный JSON")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False


def products_json_to_csv(json_filename, csv_filename):
    """
    Читает JSON с товарами и преобразует в CSV.
    Добавляет вычисляемые поля.
    """
    try:
        with open(json_filename, 'r', encoding='utf-8') as json_file:
            products = json.load(json_file)
        
        enhanced_products = []
        for product in products:
            total_cost = product['price'] * product['quantity']
            category = "Электроника" if product['price'] > 10000 else "Аксессуары"
            
            enhanced = {
                "ID": product['id'],
                "Название": product['name'],
                "Цена": product['price'],
                "Количество": product['quantity'],
                "Общая_стоимость": total_cost,
                "Категория": category
            }
            enhanced_products.append(enhanced)
        
        headers = ["ID", "Название", "Цена", "Количество", "Общая_стоимость", "Категория"]
        
        with open(csv_filename, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(enhanced_products)
        
        print(f"✅ Конвертация завершена!")
        for p in enhanced_products:
            print(f"   {p['Название']}: {p['Общая_стоимость']} руб. ({p['Категория']})")
        return True
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False



def read_csv_as_dicts(filename):
    """Читает CSV и возвращает список словарей."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        return None


def read_json_as_dicts(filename):
    """Читает JSON и возвращает список словарей."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                return [data]
            else:
                return None
    except Exception as e:
        print(f"Ошибка чтения JSON: {e}")
        return None


def save_as_csv(data, filename):
    """Сохраняет список словарей в CSV."""
    if not data:
        print("Нет данных для сохранения")
        return False
    try:
        headers = list(data[0].keys())
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Сохранено в {filename} ({len(data)} записей)")
        return True
    except Exception as e:
        print(f"Ошибка сохранения CSV: {e}")
        return False


def save_as_json(data, filename):
    """Сохраняет список словарей в JSON."""
    if not data:
        print("Нет данных для сохранения")
        return False
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Сохранено в {filename} ({len(data)} записей)")
        return True
    except Exception as e:
        print(f"Ошибка сохранения JSON: {e}")
        return False


def convert_numbers(data):
    """Преобразует строки в числа, где это возможно."""
    for row in data:
        for key, value in row.items():
            if isinstance(value, str):
                # Проверяем целое число
                if value.lstrip('-').isdigit():
                    row[key] = int(value)
                # Проверяем дробное число
                elif value.replace('.', '', 1).lstrip('-').isdigit() and '.' in value:
                    try:
                        row[key] = float(value)
                    except ValueError:
                        pass
    return data


def filter_data(data, field, value):
    """
    Фильтрует данные по значению поля.
    
    Args:
        data (list): Список словарей
        field (str): Поле для фильтрации
        value: Значение для поиска
    
    Returns:
        list: Отфильтрованные данные
    """
    return [row for row in data if str(row.get(field, '')).lower() == str(value).lower()]


def sort_data(data, field, reverse=False):
    """
    Сортирует данные по указанному полю.
    
    Args:
        data (list): Список словарей
        field (str): Поле для сортировки
        reverse (bool): По убыванию
    
    Returns:
        list: Отсортированные данные
    """
    return sorted(data, key=lambda x: x.get(field, ''), reverse=reverse)


def show_data_preview(data, title="Данные"):
    """Показывает预览 данных."""
    if not data:
        print("Нет данных")
        return
    
    print(f"\n📊 {title} (всего: {len(data)} записей)")
    print("-" * 50)
    
    headers = list(data[0].keys())
    print("Поля:", ", ".join(headers))
    
    print("\nПервые 5 записей:")
    for i, row in enumerate(data[:5], 1):
        # Красивый вывод
        for key, value in row.items():
            print(f"   {key}: {value}")
        print()
    
    if len(data) > 5:
        print(f"   ... и еще {len(data) - 5} записей")



def main():
    print("=" * 50)
    print("🔄 КОНВЕРТЕР ДАННЫХ CSV ↔ JSON")
    print("=" * 50)
    
    # Создаем исходные файлы
    create_initial_files()
    
    # Выполняем тестовые задания
    print("\n" + "=" * 50)
    print("📋 ВЫПОЛНЕНИЕ ЗАДАНИЙ")
    print("=" * 50)
    
    # Задание 2.1
    print("\n🔹 Задание 2.1: Простой конвертер CSV → JSON")
    csv_to_json("students.csv", "students.json")
    
    # Задание 2.2
    print("\n🔹 Задание 2.2: Конвертер с преобразованием (статус студента)")
    students_csv_to_json("students.csv", "students_enhanced.json")
    
    # Задание 3.1
    print("\n🔹 Задание 3.1: Простой конвертер JSON → CSV")
    json_to_csv("products.json", "products.csv")
    
    # Задание 3.2
    print("\n🔹 Задание 3.2: Конвертер с преобразованием (категории товаров)")
    products_json_to_csv("products.json", "products_enhanced.csv")
    

    
    print("\n" + "=" * 50)
    print("💻 ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 50)
    
    data = None
    current_file = None
    
    while True:
        print("\n" + "-" * 40)
        if current_file:
            print(f"📁 Текущие данные: {current_file} ({len(data) if data else 0} записей)")
        print("-" * 40)
        print("1. Загрузить CSV файл")
        print("2. Загрузить JSON файл")
        print("3. Показать данные")
        print("4. Преобразовать типы (строки → числа)")
        print("5. Фильтровать данные")
        print("6. Сортировать данные")
        print("7. Сохранить как CSV")
        print("8. Сохранить как JSON")
        print("0. Выход")
        
        choice = input("\nВыберите действие: ").strip()
        
        if choice == "0":
            print("До свидания! 👋")
            break
        
        elif choice == "1":
            filename = input("Введите имя CSV файла: ").strip()
            data = read_csv_as_dicts(filename)
            if data:
                current_file = filename
                show_data_preview(data, f"CSV: {filename}")
        
        elif choice == "2":
            filename = input("Введите имя JSON файла: ").strip()
            data = read_json_as_dicts(filename)
            if data:
                current_file = filename
                show_data_preview(data, f"JSON: {filename}")
        
        elif choice == "3":
            if data:
                show_data_preview(data)
            else:
                print("⚠️ Нет загруженных данных. Сначала загрузите файл.")
        
        elif choice == "4":
            if data:
                data = convert_numbers(data)
                print("✅ Типы данных преобразованы")
                show_data_preview(data)
            else:
                print("⚠️ Нет загруженных данных.")
        
        elif choice == "5":
            if data:
                print("\nДоступные поля:", ", ".join(list(data[0].keys())))
                field = input("Введите поле для фильтрации: ").strip()
                value = input("Введите значение для поиска: ").strip()
                filtered = filter_data(data, field, value)
                print(f"\n🔍 Найдено {len(filtered)} записей:")
                for row in filtered:
                    print(f"   {row}")
                # Спрашиваем, сохранить ли результат
                save = input("\nСохранить отфильтрованные данные? (д/н): ").strip().lower()
                if save == 'д':
                    filename = input("Имя файла для сохранения: ").strip()
                    if filename.endswith('.csv'):
                        save_as_csv(filtered, filename)
                    else:
                        save_as_json(filtered, filename)
            else:
                print("⚠️ Нет загруженных данных.")
        
        elif choice == "6":
            if data:
                print("\nДоступные поля:", ", ".join(list(data[0].keys())))
                field = input("Введите поле для сортировки: ").strip()
                order = input("По убыванию? (д/н): ").strip().lower()
                reverse = (order == 'д')
                data = sort_data(data, field, reverse)
                print(f"✅ Данные отсортированы по полю '{field}'")
                show_data_preview(data)
            else:
                print("⚠️ Нет загруженных данных.")
        
        elif choice == "7":
            if data:
                filename = input("Введите имя CSV файла для сохранения: ").strip()
                if not filename.endswith('.csv'):
                    filename += '.csv'
                save_as_csv(data, filename)
            else:
                print("⚠️ Нет данных для сохранения.")
        
        elif choice == "8":
            if data:
                filename = input("Введите имя JSON файла для сохранения: ").strip()
                if not filename.endswith('.json'):
                    filename += '.json'
                save_as_json(data, filename)
            else:
                print("⚠️ Нет данных для сохранения.")
        
        else:
            print("❌ Неверный выбор! Попробуйте снова.")



def demonstrate_filter_and_sort():
    """Демонстрирует работу функций фильтрации и сортировки"""
    print("\n" + "=" * 50)
    print("📋 ДЕМОНСТРАЦИЯ FILTER_DATA И SORT_DATA")
    print("=" * 50)
    
    # Загружаем данные студентов
    with open("students.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        students = list(reader)
    
    print("\n🔹 Исходные данные (студенты):")
    for s in students:
        print(f"   {s['Имя']} {s['Фамилия']} - {s['Группа']}, балл: {s['Средний_балл']}")
    
    # Фильтрация по группе
    filtered = filter_data(students, "Группа", "ПИН-231")
    print(f"\n🔹 Фильтрация по группе 'ПИН-231' (найдено {len(filtered)}):")
    for s in filtered:
        print(f"   {s['Имя']} {s['Фамилия']}")
    
    # Сортировка по среднему баллу
    sorted_students = sort_data(students, "Средний_балл", reverse=True)
    print("\n🔹 Сортировка по среднему баллу (по убыванию):")
    for s in sorted_students:
        print(f"   {s['Имя']} {s['Фамилия']} - {s['Средний_балл']}")



if __name__ == "__main__":
    main()
    demonstrate_filter_and_sort()
    
    print("\n" + "=" * 50)
    print("✅ ЛАБОРАТОРНАЯ РАБОТА 13 ВЫПОЛНЕНА")
    print("=" * 50)
    print("\nСозданные файлы:")
    print("   📄 students.csv          (исходные данные студентов)")
    print("   📄 products.json         (исходные данные товаров)")
    print("   📄 students.json         (результат CSV → JSON)")
    print("   📄 students_enhanced.json (результат с вычисляемыми полями)")
    print("   📄 products.csv          (результат JSON → CSV)")
    print("   📄 products_enhanced.csv (результат с вычисляемыми полями)")