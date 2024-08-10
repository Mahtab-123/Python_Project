import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Prompt the user to insert their card and provide voice feedback
print("Please insert your Card")
engine.say("Please insert your Card")
engine.runAndWait()
print("Card is inserted..")
engine.say("Card is inserted")
engine.runAndWait()
time.sleep(3)

# Set the predefined ATM password
password = 1234

# Prompt the user to enter their ATM pin and provide voice feedback
pin = int(input("Enter your ATM pin: "))
engine.say("Enter your ATM pin:")
engine.runAndWait()

# Initialize the user's account balance
balance = 5000

# Check if the entered pin matches the stored password
if pin == password:
    engine.say("Correct pin entered.")
    engine.runAndWait()

    # Provide options for the user to choose a transaction type
    engine.say("Please choose an option:")
    engine.runAndWait()
    
    print('''
          1. Balance Inquiry
          2. Withdraw Balance
          3. Deposit Balance
          4. Exit
          ''')

    # Loop to continuously accept user input for transaction type
    while True:
        try:
            # Attempt to get the user's choice and handle invalid input
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            engine.say("Please enter a valid option.")
            engine.runAndWait()
            continue

        # Balance inquiry: Show and speak the current balance
        if option == 1:
            print(f"Your Current balance is {balance}")
            engine.say(f"Your Current balance is {balance}")
            engine.runAndWait()
        
        # Withdrawal process: Check if the amount can be withdrawn and update the balance
        elif option == 2:
            engine.say("Please enter the withdrawal amount:")
            engine.runAndWait()
            withdraw_amount = int(input("Please enter the withdrawal amount: "))
            if withdraw_amount > balance:
                print("Insufficient balance!")
                engine.say("Insufficient balance!")
                engine.runAndWait()
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account.")
                engine.say(f"{withdraw_amount} is debited from your account.")
                print(f"Your current balance is {balance}")
                engine.say(f"Your current balance is {balance}")
                engine.runAndWait()
        
        # Deposit process: Add the deposit amount to the balance and confirm the update
        elif option == 3:
            engine.say("Please enter the deposit amount:")
            engine.runAndWait()
            deposit_amount = int(input("Please enter the deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account.")
            engine.say(f"{deposit_amount} is credited to your account.")
            print(f"Your updated balance is {balance}")
            engine.say(f"Your updated balance is {balance}")
            engine.runAndWait()
        
        # Exit: Thank the user and break the loop to end the program
        elif option == 4:
            print("Thank you for using our service!")
            engine.say("Thank you for using our service!")
            engine.runAndWait()
            break
        
        # Handle invalid menu options
        else:
            print("Invalid option, please try again.")
            engine.say("Invalid option, please try again.")
            engine.runAndWait()
else:
    # Handle incorrect pin entry
    print("Incorrect pin!")
    engine.say("Incorrect pin!")
    engine.runAndWait()
