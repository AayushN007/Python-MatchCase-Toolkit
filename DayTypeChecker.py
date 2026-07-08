day = input("Enter the day")
match day:
    case '1'|'7' : print("Weekend")
    case '2'|'3'|'4'|'5'|'6' : print("Weekday")
    case _ : print("Invalid")