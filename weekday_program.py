# Using if-elif statements
# The variable is defined outside the function and passed into it.

def weekday(day):
    if day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")
    elif day == 7:
        print("Sunday")
    else:
        print("Error: Please enter a number between 1 and 7")

day = int(input("Enter the day (1-7): "))
weekday(day)



# Using Dictionary Method
# This approach stores weekdays in a dictionary.

def weekday_dict(day):
    # Dictionary mapping numbers to weekdays
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    print(days.get(day, "Error: Please enter a number between 1 and 7"))

day = int(input("Enter the day (1-7): "))
weekday_dict(day)
