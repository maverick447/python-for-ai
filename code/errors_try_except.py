import os

cwd = os.getcwd()
print(f"Current working directory: {cwd}")  

try:
    exception_occured = False
    if os.path.exists('/Volumes/Drive/code/Python/PythonProjects/python-for-ai/code/number.txt'):
        print("The path number.txt exists")
        if cwd != '/Volumes/Drive/code/Python/PythonProjects/python-for-ai/code':
            os.chdir('/Volumes/Drive/code/Python/PythonProjects/python-for-ai/code')
            print(f"Changed working directory to: {os.getcwd()}")
    else :
        print("The path number.txt does not exist")
        #print("We will break from here")
        raise FileNotFoundError
    
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    #number = int(text)
    number = float(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    exception_occured = True
    print("FileNotFoundError: Could not find number.txt")
except ValueError:
    exception_occured = True
    print("ValueError: File doesn't contain a valid number")
except ZeroDivisionError:
    exception_occured
    print("ZeroDivisionError: Cannot divide by zero")
except Exception as e:
    exception_occured
    print(f"An unexpected error occurred: {e}") 

finally:
    print(f"Executing the finally block. Errors occurred: {exception_occured}")
    print("Finally block executed irrespective of Exceptions happened or not.")
    print("Execution completed. Closing file operations if needed.")