import hashlib
from datetime import datetime

# Базовий клас User
class User:
    def __init__(self, username, password, is_active=True):
        self.username = username
        self.password_hash = User.hash_password(password)
        self.is_active = is_active

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        return self.password_hash == User.hash_password(password)

# Підклас Administrator
class Administrator(User):
    def __init__(self, username, password, is_active=True):
        super().__init__(username, password, is_active)
        self.permissions = []

    def add_permission(self, permission):
        self.permissions.append(permission)

# Підклас RegularUser
class RegularUser(User):
    def __init__(self, username, password, is_active=True):
        super().__init__(username, password, is_active)
        self.last_login = None

    def update_last_login(self):
        self.last_login = datetime.now()

# Підклас GuestUser
class GuestUser(User):
    def __init__(self, username):
        super().__init__(username, password="", is_active=False)

# Клас AccessControl
class AccessControl:
    def __init__(self):
        self.users = {}

    def add_user(self, user_obj):
        self.users[user_obj.username] = user_obj

    def authenticate_user(self, username, password):
        found_user = self.users.get(username)
        if found_user and found_user.verify_password(password) and found_user.is_active:
            if isinstance(found_user, RegularUser):
                found_user.update_last_login()
            return found_user
        return None

# === Приклад використання ===
if __name__ == "__main__":
    access_control = AccessControl()

    admin_user = Administrator("admin", "adminyarik")
    admin_user.add_permission("manage_users")

    regular_user = RegularUser("Yaroslav", "Yaroslav911")
    guest_user = GuestUser("visitor")

    access_control.add_user(admin_user)
    access_control.add_user(regular_user)
    access_control.add_user(guest_user)

    # Перевірка входу
    authenticated_user = access_control.authenticate_user("Yaroslav", "Yaroslav911")
    if authenticated_user:
        print(f"Вхід успішний: {authenticated_user.username}")
    else:
        print("Невірне ім'я користувача або пароль")
