# subprocess lets us run each feature as a separate Python script
import subprocess


# Display the main menu
print("===== Moon Restaurant Data =====")

print("1. View User Drop Off")
print("2. View Abandonment rate (Before vs After)")
print("3. View Average Checkout Time")
print("4. View Abandonment Rate by Device")
print("5. Exit")

choice = input("Enter choice: ")

# Run the matching script based on user input
if choice == "1":
    subprocess.run(["python", "scripts/viewDropoff.py"])
elif choice == "2":
    subprocess.run(["python", "scripts/viewAbandonment.py"])
elif choice == "3":
    subprocess.run(["python", "scripts/viewAvgCheckoutTime.py"])
elif choice == "4":
    subprocess.run(["python", "scripts/ViewAbandonmentViaDevice.py"])
elif choice == "5":
    print("Exit!")
else:
    print("Try again.")
