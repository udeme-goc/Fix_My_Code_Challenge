#!/usr/bin/python3
"""
User class
"""


class User():
    """
    Represents a user with an email address.

    Attributes:
        __email (str): The email address of the user.
    """

    def __init__(self):
        """
        Initialize a new User object with no email address.
        """
        self.__email = None

    @property
    def email(self):
        """
        Get the email address of the user.

        Returns:
            str: The email address of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Set the email address of the user.

        Args:
            value (str): The new email address to set.

        Raises:
            TypeError: If the provided value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    # Example usage
    u = User()
    u.email = "john@snow.com"
    print(u.email)
