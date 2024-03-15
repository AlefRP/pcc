class User:
    def __init__(self, first_name, last_name, age, gender, email, loggin_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.login_attempts = loggin_attempts
        
    def describe_user(self):
        """
        A method to describe the user's first name, last name, age, gender, and email.
        """
        """"""
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Email: {self.email}")
        
    def greet_user(self):
        """_summary_
        """
        print(f"Hello {self.first_name} {self.last_name}!")
        
    def increment_loggin_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempts: {self.login_attempts}")
        
first_user = User("John", "Doe", 30, "male", "john.doe@example.com")

first_user.describe_user()
first_user.greet_user()

second_user = User("Jane", "Doe", 25, "female", "jane.doe@example.com")

second_user.describe_user()
second_user.greet_user()

for _ in range(3):
    second_user.increment_loggin_attempts()

second_user.reset_login_attempts()