
previleges = {
    1: "create",
    2: "read",
    3: "update",
    4: "delete"
}

class User:
    """Represents a simple user profile."""
    def __init__(self, username, email, address):
        """Initializes the user."""
        self.username = username
        self.email = email
        self.address = address
    
    def __str__(self):
        """Return the string representation of the User."""
        return f"{self.username} ({self.email})"
    
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
        
        
administrator = Admin("admin", "admin@example.com", "123 Main St", [1, 2, 3, 4])
administrator.privileges.show_privileges()