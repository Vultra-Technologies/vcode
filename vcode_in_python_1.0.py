# Our Simple Language Interpreter

# Initialize an empty dictionary to store variables
variables = {}

def evaluate_expression(expr):
    try:
        return eval(expr, variables)
    except:
        return None

while True:
    command = input("vcode-1.0> ").strip().lower()

    if command == "exit":
        print("Goodbye!")
        break


    elif command == "print":
        expr = input("Enter an expression to print: ")
        result = evaluate_expression(expr)
        if result is not None:
            print("Result:", result)
        else:
            print("ERROR: Invalid expression.")

    elif command == "asvar":
        var_name = input("Enter variable name: ")
        expr = input(f"Enter an expression to assign to {var_name}: ")
        result = evaluate_expression(expr)
        if result is not None:
            variables[var_name] = result
            print(f"{var_name} assigned with value {result}")
        else:
            print("ERROR: Invalid expression.")
    
    elif command == "help":
        print("Type 'lscom' to list commands, 'lercom' to list all commands and write what they do, or 'exit', to exit back to the interpreter.")
        while True:
            que = input("vhelp>")
            if que == 'lscom':
               print("print, asvar, help, exit.")
            if que == 'lercom':
                print("print, to print an expression, asvar, to assign a variable to an expression, help, to get help, and exit, to exit the interpreter.")
            if que == 'exit':
                break

    else:
        print(f"ERROR: Unkown command: {command}")

  
