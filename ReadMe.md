# User Bank System

This Python project implements a simple user management system using object-oriented programming principles and regular expressions for input validation.

## Table of Contents:

- [Class_Description](#class-description)
- [Preview](#preview)
- [Installation](#installation)
- [Usage](#usage)
- [Code Snippets](#code-snippets)
- [Testing](#testing)
- [Technologies](#technologies)
- [Methodologies and Principles](#methodologies-and-principles)
- [Ouput](#ouput)
- [Creator](#creator)

## Class Description:

The User Bank System consists of two classes: `User` and `BankUser`. These classes are designed to manage user information, including their name, PIN, password, and balance. The `BankUser` class extends the `User` class with additional functionalities specific to banking operations, such as withdrawing, depositing, transferring money, and requesting money from other users.

The project demonstrates the use of regular expressions (RE) for input validation, ensuring that usernames, PINs, and passwords meet specific criteria. Additionally, it showcases object-oriented programming (OOP) principles such as encapsulation, inheritance, and polymorphism.

## Preview

<img width="500"  alt="GUI" src="https://github.com/NateJonesIII/PyBankOOP/blob/main/assets/img/preview.PNG">

## Installation:

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the Python script `user_management_system.py` in your preferred Python environment.

## Usage:

1. Import the `User` and `BankUser` classes from the `user_management_system.py` file.
2. Create instances of `User` or `BankUser` objects.
3. Utilize the methods provided by each class to manage user information and perform banking operations.

## Code Snippets:

### `User` Class Constructor

```python
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
```

### `BankUser` Class Method: `withdraw`

```def withdraw(self, amount):
    if self.on_hold:
        print("Withdrawal failed: Account(s) involved are on hold.")
        return
    if int(amount) > self.balance:
        print("ERROR: Withdrawal amount greater than balance.")
    elif int(amount) <= 0:
        print("ERROR: Withdrawal amount must be a positive number.")
    else:
        self.balance -= amount
```

## Testing:

- The project includes various test cases to ensure the functionality and correctness of each method within the User and BankUser classes. Automated testing frameworks such as unittest or pytest can be utilized to execute these test cases.

## Technologies:

- Python: Programming language used for implementation
- Regular Expressions (RE): Used for input validation
- Object-Oriented Programming (OOP): Principles applied for modularity and reusability

## Methodologies and Principles:

I Learned these several methodologies and principles:

- Object-Oriented Programming (OOP): Classes and objects are used to encapsulate data and behavior, promoting modularity and reusability.
- Regular Expressions (RE): Regular expressions are employed for input validation, ensuring data integrity and security.
- Encapsulation: Data is encapsulated within class instances, and access is controlled through methods, enhancing data security and abstraction.
- Inheritance: The BankUser class inherits from the User class, facilitating code reuse and promoting a hierarchical structure.
- Polymorphism: Methods like withdraw, deposit, and transfer_money exhibit polymorphic behavior, allowing for flexible and interchangeable implementations.

## Ouput:

<img width="500"  alt="GUI" src="https://github.com/NateJonesIII/PyBankOOP/blob/main/assets/img/OutPut.PNG">

## Creator:

- [Profile](https://github.com/NateJonesIII/ "Nathaniel Jones") - [LinkedIn](https://www.linkedin.com/in/nathaniel-jones/) - [Email](mailto:15nate.jones@gmail.com?subject=Hello "Hello Nate!")
