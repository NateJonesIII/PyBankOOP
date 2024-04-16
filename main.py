from bankuser import BankUser

# Create BankUser instances and perform tests
user1 = BankUser("Bob", 1234, "secret!", 0)
user2 = BankUser("Oinky the pig", 4321, "secret!", 0)

# Deposit money into user2's account
user2.deposit(5000)

# Attempt to withdraw a negative amount from user2's account
print("Testing negative withdrawal request: ")
user2.withdraw(-50)

# Attempt to withdraw a non-numeric amount from user2's account
print("Testing non-numeric withdrawal request: ")
user2.withdraw("500")
print("===================================================")
# Display user balances
user2.show_balance()
user1.show_balance()

# Transfer money from user2 to user1
user2.transfer_money(800, user1)

# Display updated balances after transfer
user2.show_balance()
user1.show_balance()

# Request money from user1 by user2
user2.request_money(user1, 250)

# Display updated balances after request
user2.show_balance()
user1.show_balance()

# Display a message to the user
print("Press Enter to continue...")

# Pause the program and wait for the user to press Enter
input()
