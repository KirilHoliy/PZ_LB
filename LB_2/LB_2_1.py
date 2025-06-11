def analyze_log_file(log_file_path):
   try:
       result_dict = {}
       with open(log_file_path) as file:
           for line in file:
               split_list = line.split()


               # Перевірка: чи є в рядку статус-код
               if len(split_list) > 8:
                   status_code = split_list[8]
                   if status_code.isdigit():  # перевірка, що це число
                       if status_code in result_dict:
                           result_dict[status_code] += 1
                       else:
                           result_dict[status_code] = 1
               else:
                   print("⚠️ Рядок надто короткий або має неочікувану структуру:", line.strip())


   except FileNotFoundError:
       print("❌ Файл не знайдено.")
       result_dict = {}
   except IOError:
       print("❌ Помилка читання файлу.")
       result_dict = {}


   return result_dict




# ✅ Виклик функції
path_to_log_file = "C:\\Users\\Dell\\Downloads\\apache_logs.txt"  # (додано .txt і виправлено слеші)
res = analyze_log_file(path_to_log_file)
print("📊 Статистика HTTP-кодів:", res)
