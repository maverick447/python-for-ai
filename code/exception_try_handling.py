
while(True):
    try:
        number = int(input("Enter a number: "))
        print(1 / number)
        break
    # having a general exception handler, not recommended as it can catch unexpected exceptions
    #except Exception as e:
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Cannot divide by zero")

    # the logic here is to catch specific exceptions first, then a general exception handler    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # a finally block is used to execute code regardless of whether an exception occurred
    finally:
        print("Execution completed. Do final file cleanup here if needed.")