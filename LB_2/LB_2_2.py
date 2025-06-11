import hashlib


def generate_file_hashes(*paths_list):
   hashes_dict = {}


   for single_path in paths_list:
       try:
           with open(single_path, mode='rb') as opened_file:
               file_bytes = opened_file.read()
               hash_hex = hashlib.sha256(file_bytes).hexdigest()
               hashes_dict[single_path] = hash_hex
       except FileNotFoundError:
           print(f"⚠️ Файл не знайдено: {single_path}")
       except IOError as e:
           print(f"❌ Неможливо прочитати файл {single_path}: {e}")


   return hashes_dict


# Приклад використання:
files = [
   "C:\\Users\\Dell\\Downloads\\apache_logs.txt",


]


hashes = generate_file_hashes(*files)
print("🔐 Хеші файлів:")
for filepath, hash_value in hashes.items():
   print(f"{filepath} -> {hash_value}")

