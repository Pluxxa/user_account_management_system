class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        super().__init__(user_id, name, access_level)
        self._user_list = []

    def add_user(self, user):
        self._user_list.append(user)

    def remove_user(self, user):
        if user in self._user_list:
            self._user_list.remove(user)
        else:
            print("User not found in the list")

    def get_user_list(self):
        return self._user_list


# Пример использования
if __name__ == "__main__":
    # Создание обычных пользователей
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")

    # Создание администратора
    admin = Admin(3, "Admin")

    # Добавление пользователей администратором
    admin.add_user(user1)
    admin.add_user(user2)

    # Вывод списка пользователей
    print("User List:")
    for user in admin.get_user_list():
        print("ID:", user.get_user_id(), "Name:", user.get_name(), "Access Level:", user.get_access_level())

    # Удаление пользователя
    admin.remove_user(user1)

    # Вывод обновленного списка пользователей
    print("\nUpdated User List:")
    for user in admin.get_user_list():
        print("ID:", user.get_user_id(), "Name:", user.get_name(), "Access Level:", user.get_access_level())
