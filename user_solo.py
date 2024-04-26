"""Represents a simple user profile."""
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