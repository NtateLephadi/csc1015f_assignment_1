hours = eval(input("Enter the hours: "))
minutes = eval(input("Enter the minutes: "))
seconds = eval(input("Enter the seconds: "))

if hours < 0 or hours > 23:
    print("Your time is invalid.")
elif minutes < 0 or minutes > 59:
    print("Your time is invalid.")
elif seconds < 0 or seconds > 59:
    print("Your time is invalid.")
else:
    print("Your time is valid.")