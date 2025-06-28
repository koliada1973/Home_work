try:
    # Створюємо виключення з кількома параметрами
    raise Exception("Помилка доступу", 403, "Користувач неавторизований")
except Exception as error:
    # Параметри зберігаються у властивості args (кортеж)
    print("Оброблено виключення:")
    print(f"Тип: {type(error)}")
    print(f"Параметри: {error.args}")
    print(f"Код помилки: {error.args[1]}")
    print(f"Опис: {error.args[0]}, Причина: {error.args[2]}")