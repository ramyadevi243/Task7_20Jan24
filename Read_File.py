'''
Name: Ramya
Date: 22/01/2024
Task: 2
'''

# Python program using function that will read a text file

# Defining a function to read a file
def read_file(file_name):
    # Opening a file with Read option
    file = open(file_name, "r")
    return file.read()

# Main method execution
if __name__ == "__main__":
    
    # Passing value or argument to the parameter for method read_file and storing it in
    # variable file_name
    file_name = "Diwali.txt"

    # Print the content of the file in the console
    print("Content of the file",read_file(file_name))

