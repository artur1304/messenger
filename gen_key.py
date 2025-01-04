import hashlib
import os
import json

def generate_key():
    # Генерация случайного ключа
    random_bytes = os.urandom(16)  # Генерируем 16 случайных байт
    key = hashlib.sha256(random_bytes).hexdigest()  # Хешируем для получения ключа
    return key

def save_key(key):
    # Сохраняем ключ в файл
    keys = load_keys()
    keys.append(key)
    with open("keys.json", "w") as file:
        json.dump(keys, file)

def load_keys():
    # Загружаем существующие ключи из файла
    if not os.path.exists("keys.json"):
        return []
    with open("keys.json", "r") as file:
        return json.load(file)

if __name__ == "__main__":
    new_key = generate_key()
    save_key(new_key)
    print(f"Сгенерирован новый ключ: {new_key}")
