# Создание родительского класса
class User():
    def __init__(self, ID, name, access_level):
        self._protected_ID = ID
        self.public_name = name
        self._protected_access_level = access_level

# Создание функции вывода списка пользователей
    def list_users(self):
        return self.public_name
        print("Вот список имён пользователей: ", self.public_name)

# Создание дочернего класса
class Admin(User):
    def __init__(self, ID, name, access_level, manager_access):
        super().__init__(ID, name, access_level)
        self.__private_manager_access = manager_access

# Создание функции добавления пользователя в родительский список

# Создание функции удаления пользователя из родительского списка