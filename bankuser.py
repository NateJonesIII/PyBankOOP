from user import User

class BankUser(User):
    """
    Represents a bank user with additional banking functionality,
    inheriting from the User class.
    """

    def __init__(self, name, pin, password, balance):
        """
        Initializes a bank user with the provided name, PIN, password, and balance.

        Parameters:
        - name (str): The user's name.
        - pin (int): The user's PIN.
        - password (str): The user's password.
        - balance (float): The user's account balance.
        """
        super().__init__(name, pin, password)
        self.balance = balance
        self.on_hold = False
    
    def show_balance(self):
        """
        Displays the user's account balance.
        """
        print(f"My Balance is: ${self.balance:.2f}")
    
    def withdraw(self, amount):
        """
        Withdraws the specified amount from the user's account, if valid.

        Parameters:
        - amount (float): The amount to withdraw from the account.
        """
        if self.on_hold:
            print("Withdrawal failed: Account(s) involved are on hold.")
            return
        if int(amount) > self.balance: 
            print("ERROR: Withdrawal amount greater than balance.\n")       
        elif int(amount) <= 0:
            print("ERROR: Withdrawal amount must be a positive number.\n")
        elif type(amount) == str:
            print("ERROR: Only numerical values are allowed.\n")
        else:
            self.balance -= amount 
                       
    def deposit(self, amount):
        """
        Deposits the specified amount into the user's account, if valid.

        Parameters:
        - amount (float): The amount to deposit into the account.
        """
        if self.on_hold:
            print("Deposit failed: Account is on hold.")
            return
        self.balance += amount
    
    def transfer_money(self, amount, otheruser):
        """
        Transfers the specified amount from the user's account to another user's account, if valid.

        Parameters:
        - amount (float): The amount to transfer.
        - otheruser (BankUser): The recipient of the transfer.
        """
        if self.on_hold or otheruser.on_hold:
            print("Transfer failed: Account(s) involved are on hold.")
            return
        if float(amount) > self.get_balance():
            print("ERROR: Amount exceeds current balance.")
            return False
        print(f"You are transferring ${amount:.2f} to {otheruser.get_name()}")
        print("Authentication required")
        pin = input(f"Enter your PIN {self.get_name()}: ")   
        # If correct PIN is given for the transferring User. Also return a Boolean value of True.
        if int(pin) == int(self.pin):
            print("Transfer authorized")
            self.withdraw(amount)
            print(f"Transferring ${amount:.2f} to {otheruser.name}")
            otheruser.deposit(amount)
            return True
        # If an incorrect PIN is given, return a Boolean value of False.
        else:     
            print("Invalid Pin. Transaction canceled.")
            return False
    
    def request_money(self, otheruser, amount):
        """
        Requests the specified amount from another user's account, if valid.

        Parameters:
        - otheruser (BankUser): The user from whom money is being requested.
        - amount (float): The amount to request from the other user.
        """
        if self.on_hold or otheruser.on_hold:
            print("Requests failed: Account(s) involved are on hold.")
        if float(amount) > otheruser.get_balance():
            print("ERROR: Amount exceeds withdrawal threshold.")
            return False
        print(f"You are requesting ${amount:.2f} from {otheruser.get_name()}")
        print("Authentication is required...")
        otherpin = input(f"Enter {otheruser.get_name()}'s PIN: ")
        if int(otherpin) == int(otheruser.get_pin()):
            # Will ask for and validate the password of the User requesting money as well
            password = input(f"Enter your password{self.get_name()}: ")
            if password == self.password:
                print("Request Authorized")
                otheruser.withdraw(amount)
                self.deposit(amount)
                print(f"{otheruser.get_name()} sent ${amount:.2f}")
            else:
                print("Invalid Password. Transaction canceled")
                return True
        else:
            print("Invalid Pin. Transaction canceled.")
            return False
    
    def toggle_on_hold(self):
        """
        Toggles the account hold status.
        """
        self.on_hold = not self.on_hold
            
    def get_on_hold_status(self):
        """
        Retrieves the account hold status.

        Returns:
        - bool: True if account is on hold, False otherwise.
        """
        return self.on_hold
