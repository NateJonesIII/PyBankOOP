# Regular expression operations import
import re

class User:
    """
    Represents a basic user with name, PIN, and password.
    """

    def __init__(self, name, pin, password):
        """
        Initializes a user with the provided name, PIN, and password.

        Parameters:
        - name (str): The user's name.
        - pin (int): The user's PIN.
        - password (str): The user's password.
        """
        self.name = name
        self.pin = pin
        self.password = password
    
    def change_name(self, newname):
        """
        Changes the user's name to the specified new name, if valid.

        Parameters:
        - newname (str): The new name to set for the user.
        """
        if len(newname) < 2 or len(newname) > 10:
            print("ERROR: Username must be between 2 and 10 characters length.")
        elif str(newname) == self.name:
            print("ERROR: Cannot reuse previous name.")
        elif re.match(r"[\s\w]+$", newname):
            print("ERROR: No white spaces allowed")
        else:
            self.name = newname
    
    def change_pin(self, newpin):
        """
        Changes the user's PIN to the specified new PIN, if valid.

        Parameters:
        - newpin (str): The new PIN to set for the user.
        """
        if len(newpin) != 4:
            print("ERROR: Length of PIN must be 4 digits long.")
        elif int(newpin) == self.pin:
            print("ERROR: Cannot reuse previous PIN.")
        elif re.match(r"[\s\w]+$", newpin):
            print("ERROR: No white spaces allowed")
        else:
            self.pin = newpin
    
    def change_password(self, newpass):
        """
        Changes the user's password to the specified new password, if valid.

        Parameters:
        - newpass (str): The new password to set for the user.
        """
        if len(newpass) < 5:
            print("ERROR: Password must be greater than 5 characters length.")
        elif str(newpass) == self.password:
            print("ERROR: Cannot reuse previous password.")
        else:
            self.password = newpass
    
    def get_pin(self):
        """
        Retrieves the user's PIN.

        Returns:
        - int: The user's PIN.
        """
        return self.pin
    
    def get_name(self):
        """
        Retrieves the user's name.

        Returns:
        - str: The user's name.
        """
        return self.name
    
    def get_balance(self):
        """
        Placeholder method for retrieving user's balance.
        This method will be implemented in the BankUser subclass.

        Returns:
        - float: The user's balance.
        """
        return self.balance
