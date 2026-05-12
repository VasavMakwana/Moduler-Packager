import datetime
import math
import random
import uuid
from my_utils import file_ops, math_plus

def show_menu():
    print("\n--- Multi-Utility Toolkit ---")
    print("1. Datetime: Show Current Time & Format")
    print("2. Math: Calculate Compound Interest")
    print("3. Random: Generate Password & OTP")
    print("4. UUID: Generate Unique ID")
    print("5. Custom: Celsius to Fahrenheit")
    print("6. Explore: Dynamic Module Exploration (dir)")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            now = datetime.datetime.now()
            print(f"Current: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            
        elif choice == '2':
            p = float(input("Principal: "))
            r = float(input("Rate: "))
            t = float(input("Time: "))
            ci = p * (pow((1 + r / 100), t))
            print(f"Compound Interest: {ci:.2f}")

        elif choice == '3':
            chars = "abcdefghijklmnopqrstuvwxyz1234567890@#$"
            pwd = "".join(random.sample(chars, 10))
            otp = random.randint(1000, 9999)
            print(f"Generated Password: {pwd}")
            print(f"Your OTP: {otp}")

        elif choice == '4':
            u_id = uuid.uuid4()
            print(f"Unique Identifier: {u_id}")
            # Save this to a log using our custom module
            file_ops.save_to_file("logs.txt", f"ID Generated: {u_id}")

        elif choice == '5':
            c = float(input("Enter Celsius: "))
            print(f"Fahrenheit: {math_plus.celsius_to_fahrenheit(c)}")

        elif choice == '6':
            mod_name = input("Enter module to explore (math/random/datetime): ")
            if mod_name == "math": print(dir(math))
            elif mod_name == "random": print(dir(random))
            else: print("Invalid module selection.")

        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()