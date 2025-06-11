import sqlite3
import hashlib
import os

# Підключення до БД (створить файл, якщо не існує)
DB_FILE = "users.db"
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Створення таблиці, якщо вона не існує
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        login TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        full_name TEXT NOT NULL
    )
''')
conn.commit()

# Хешування пароля (SHA-256)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Додавання нового користувача
def add_user():
    print("\n=== ДОДАВАННЯ КОРИСТУВАЧА ===")
    login = input("Логін: ").strip()
    full_name = input("ПІБ: ").strip()
    password = input("Пароль: ").strip()

    if not login or not full_name or not password:
        print("❌ Всі поля обов’язкові!")
        return

    hashed = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)",
                       (login, hashed, full_name))
        conn.commit()
        print("✅ Користувача додано успішно.")
    except sqlite3.IntegrityError:
        print("❌ Користувач з таким логіном вже існує.")

# Оновлення пароля
def update_password():
    print("\n=== ОНОВЛЕННЯ ПАРОЛЯ ===")
    login = input("Логін: ").strip()
    new_password = input("Новий пароль: ").strip()

    if not login or not new_password:
        print("❌ Усі поля обов’язкові!")
        return

    new_hash = hash_password(new_password)
    cursor.execute("UPDATE users SET password = ? WHERE login = ?", (new_hash, login))
    if cursor.rowcount == 0:
        print("❌ Користувача не знайдено.")
    else:
        conn.commit()
        print("✅ Пароль оновлено успішно.")

# Перевірка автентифікації
def authenticate():
    print("\n=== ВХІД ДО СИСТЕМИ ===")
    login = input("Логін: ").strip()
    password = input("Пароль: ").strip()
    password_hash = hash_password(password)

    cursor.execute("SELECT full_name FROM users WHERE login = ? AND password = ?", (login, password_hash))
    result = cursor.fetchone()

    if result:
        print(f"✅ Успішна автентифікація. Вітаємо, {result[0]}!")
    else:
        print("❌ Невірний логін або пароль.")

# Основне меню
def main_menu():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати користувача")
        print("2. Оновити пароль")
        print("3. Увійти")
        print("4. Вихід")
        choice = input("Ваш вибір (1-4): ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            update_password()
        elif choice == "3":
            authenticate()
        elif choice == "4":
            print("👋 Вихід із програми. До побачення!")
            break
        else:
            print("❌ Невірний вибір! Введіть цифру 1-4.")

if __name__ == "__main__":
    main_menu()
    conn.close()
