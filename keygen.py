import json
import random								# библиотеки
import os


KEYS_FILE = "keys.json"						# файлы
USERS_FILE = "users.json"


def load_keys():
    if not os.path.exists(KEYS_FILE) or not os.path.getsize(KEYS_FILE) > 0:
        return {}
    with open(KEYS_FILE, "r") as file:		# функции для работы с ключами
        return json.load(file)

def save_keys(keys):
    with open(KEYS_FILE, "w") as file:
        json.dump(keys, file)


def load_users():
    if (not os.path.exists(USERS_FILE) or not os.path.getsize(USERS_FILE)) > 0:
        return {}
    with open(USERS_FILE, "r") as file:		# функции для работы с пользователями
        return json.load(file)

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file)


name = input()
users = load_users()
keys = load_keys()
if name in users:
	print(keys[name])
else:										# кейген и проверка на существование ключа
	key = random.randint(0, 
		9999999999999999)
	key = str(key).zfill(16)
	print(key)
	keys[name] = key
	save_keys(keys)
