import re

print("=" * 50)
print("ДОМАШНЕЕ ЗАДАНИЕ ПО РЕГУЛЯРНЫМ ВЫРАЖЕНИЯМ")
print("=" * 50)

print("\n🔹 Задание 1: Найди всё")
text = "В группе ПИН-231 учатся 19 студентов. В группе ПИН-232 — 22 студента."
groups = re.findall(r'[А-Я]+-\d{3}', text)
print(f"Текст: {text}")
print(f"Найденные группы: {groups}")

print("\n🔹 Задание 2: Проверь телефон")

def check_phone(phone):
    """Проверяет формат телефона +7-999-123-45-67"""
    pattern = r'^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$'
    return bool(re.match(pattern, phone))

# Тестирование
test_phones = ["+7-999-123-45-67", "+7-123-456-78-90", "89991234567", "не телефон"]
for phone in test_phones:
    if check_phone(phone):
        print(f"✅ {phone} - корректный")
    else:
        print(f"❌ {phone} - неверный формат")

print("\n🔹 Задание 3: Замени мат")
original = "Это плохое слово, и это тоже плохое"
censored = re.sub(r'плохое', '[ЦЕНЗУРА]', original)
print(f"Исходный текст: {original}")
print(f"Цензурированный: {censored}")

print("\n" + "=" * 50)
print("✅ Домашнее задание выполнено!")
print("=" * 50)