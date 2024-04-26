"""Represents privileges of an admin."""
from user_solo import User

previleges = {
    1: "create",
    2: "read",
    3: "update",
    4: "delete"
}
    
class Privileges:
    """Represents privileges of an admin."""
    def __init__(self, name, privileges):
        """Initializes the privileges."""
        self.name = name
        self.privileges = privileges
        
    def show_privileges(self):
        """Display the privileges of the admin."""
        print(f"The privileges of {self.name} are:")
        for privilege in self.privileges:
            print(f"- {previleges[privilege]}")
    
class Admin(User):
    """Represents an admin user profile."""
    def __init__(self, username, email, address, privileges = []):
        """Initializes the admin."""
        super().__init__(username, email, address)
        self.privileges = Privileges(username, privileges)