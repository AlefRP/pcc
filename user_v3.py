class User:
    def __init__(self, first_name, last_name, age, gender, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Email: {self.email}")
        
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")
        
first_user = User("John", "Doe", 30, "male", "john.doe@example.com")

first_user.describe_user()
first_user.greet_user()

second_user = User("Jane", "Doe", 25, "female", "jane.doe@example.com")

second_user.describe_user()
second_user.greet_user()