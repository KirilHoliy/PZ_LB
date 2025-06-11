Аутентифікація — тема: Вхід у систему хакерської школи «Червоний Капюшон»
import hashlib


# Словник користувачів
uchni = {
   "volk": {
       "parol": hashlib.md5("krasnyj123".encode()).hexdigest(),
       "pib": "Сірий Вовк Володимирович"
   },
   "alisa": {
       "parol": hashlib.md5("h4ckm3".encode()).hexdigest(),
       "pib": "Лисиця Аліса Іванівна"
   }
}


def dostup_do_hackshkoly(login):
   if login in uchni:
       vvedenyy = input("🔑 Введіть пароль для входу: ")
       khesh = hashlib.md5(vvedenyy.encode()).hexdigest()
       if khesh == uchni[login]["parol"]:
           print(f"✅ Доступ дозволено! Вітаємо, агент {uchni[login]['pib']}.")
       else:
           print("⛔ Невірний пароль.")
   else:
       print("⛔ Користувача не знайдено.")


# Ось саме тут має бути виклик
korystuvach = input("👤 Введіть логін: ")
dostup_do_hackshkoly(korystuvach)
