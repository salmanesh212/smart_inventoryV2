from core.exceptions import InvalidEmailException


class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def validate_email(self):
        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            raise InvalidEmailException(f"Invalid email: {self.email}")
        print("Valid email")
