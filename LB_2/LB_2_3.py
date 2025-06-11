from collections import Counter


def filter_ips(input_file_path, output_file_path, allowed_ips):
   ip_count = Counter()


   try:
       with open(input_file_path, 'r') as file:
           for line in file:
               parts = line.split()
               if not parts:
                   continue  # пропускаємо порожні рядки
               ip = parts[0]  # IP - перша частина рядка


               if ip in allowed_ips:
                   ip_count[ip] += 1


       if ip_count:
           with open(output_file_path, 'w') as output_file:
               for ip, count in ip_count.items():
                   output_file.write(f"{ip} - {count}\n")
           print(f"Результат записано у файл: {output_file_path}")
       else:
           print("Не знайдено жодної дозволеної IP-адреси в лог-файлі.")


   except FileNotFoundError:
       print(f"❌ Файл не знайдено: {input_file_path}")
   except IOError:
       print(f"❌ Помилка запису до файлу: {output_file_path}")


   return ip_count




# Виклик функції з вашим шляхом
allowed_ips = ["83.149.9.216", "93.114.45.13", "50.16.19.13"]
input_log_path = r"C:\Users\Dell\Downloads\apache_logs.txt"
output_filtered_path = r"C:\Users\Dell\Downloads\filtered_ips.txt"


ip_counts = filter_ips(input_log_path, output_filtered_path, allowed_ips)
print("Підсумкові IP-адреси:", ip_counts)
