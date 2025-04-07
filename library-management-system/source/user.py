class User:
    """
    Represents a user in the library system.

    Attributes:
        name (str): User's full name.
        user_id (str): Unique identifier for the user.
        user_type (str): Type of user, e.g., 'student' or 'teacher'.
    """

    def __init__(self, name, user_id, user_type="student"):
        """
        Initializes a new User object.
        """
        self.name = name
        self.user_id = user_id
        self.user_type = user_type

    def to_dict(self):
        """
        Converts the User object to a dictionary.

        Returns:
            dict: Dictionary representation of the user.
        """
        return self.__dict__

    @staticmethod
    def from_dict(data):
        """
        Creates a User object from a dictionary.

        Args:
            data (dict): Dictionary with user data.

        Returns:
            User: A new User instance.
        """
        return User(data["name"], data["user_id"], data.get("user_type", "student"))

