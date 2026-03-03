print("Welcome to the seconds to date converter!")
total_seconds = int(input("Enter the number of seconds (0–8640000): "))
if 0 <= total_seconds and total_seconds <= 8640000:
    # calculate the number of days, hours, minutes and seconds
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # determine the correct form of the word "днів"
    last_two = days % 100
    last_one = days % 10
    if 11 <= last_two <= 14:
        day_word = "днів"
    elif last_one == 1:
        day_word = "день"
    elif 2 <= last_one <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    # print the result
    print(f"{total_seconds} => {days} {day_word}, {hours:02d}:{minutes:02d}:{seconds:02d}")
else:
    # print an error message if the input is invalid
    print("Invalid input. Please enter a number between 0 and 8640000.")
