# Создание списка для хранения данных всех пользователей
all_users = []

# Создание родительского класса
class User():
    def __init__(self, ID, name, access_level):
        self._protected_ID = ID
        self.public_name = name
        self._protected_access_level = access_level
        # Добавление пользователя в список
        all_users.append(self)

# Создание функции получения имени
    def get_name(self):
        return self.public_name

# Создание дочернего класса
class Admin(User):
    def __init__(self, ID, name, access_level, manager_access):
        super().__init__(ID, name, access_level)
        self.__private_manager_access = manager_access

# Создание функции вывода списка пользователей
    def list_users(self):
        return [user.get_name() for user in all_users]
print(Admin.list_users(all_users)) # Почему данная функция выдаёт пустой список?
# Как сделать, чтобы функция выдавала список всех пользователей?

# Создание функции добавления пользователя в список
def add_user(ID, name, access_level):
    new_user = User(ID, name, access_level)
    all_users.append(new_user)
    return new_user
    print(f"{new_user.get_name()} добавлен в список") # Почему данная функция не работает?

# Создание функции удаления пользователя из списка
def remove_user(user):
    if user in all_users:
        del user # Почему данная функция не работает?
        print(f"{user.get_name()} удалён из списка")
    else:
        print("Такого пользователя нет в списке")


# Тестирование

user1 = User(1, "Поля", 2)
user2 = User(2, "Вася", 1)
user3 = User(3, "Коля", 3)

admin1 = Admin(1, "Саша", 2, True)
admin2 = Admin(2, "Маша", 1, False)
admin3 = Admin(3, "Лена", 3, True)

all_users = [user1, user2, user3, admin1, admin2, admin3]
print(Admin.list_users(all_users))

user3.get_name()
print(f"{user3.get_name()} - {user3._protected_access_level}")

admin1.get_name()
print(f"{admin1.get_name()} - {admin1._protected_access_level}")

add_user(4, "Женя", 2)
print(Admin.list_users(all_users)) # Почему данная функция выдаёт имя нового user 2 раза?

add_user(5, "Даша", 3)
print(Admin.list_users(all_users)) # Почему данная функция выдаёт имя нового user 2 раза?
