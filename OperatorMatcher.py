sym = input("Enter the operator")
match sym:
    case "+" : print("Addition")
    case "-" : print("Subraction")
    case "*" : print("Multiplication")
    case "/" : print("Division")
    case  _  : print("Cannot be determined")
    