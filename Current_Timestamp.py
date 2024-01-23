'''
Name: Ramya
Date: 22/01/2024
Task: 1
'''

# Created a Python program using function that will create a text file with current timestamp

# Importing datetime module which has the class datatime
import datetime

# Defining a function to create a file with current timestamp
def create_file(file_name, content, current_time):
    # Open a new file with write option and stored it in a variable called file
    file = open(file_name, "w")
    # Write function to the content of file
    file.write(content)
    return file

# Main function execution
if __name__ == "__main__":
    # Passing values or arguments to the parameters of the method create_file
    file_name = "Diwali.txt"
    content = "Let's celebrate the Diwali Utsav with Diyas, flowers, crackers, sweets and more...!\n\n\n\nTimestamp: {time}"
    current_time = datetime.datetime.now()
    
    # Print the file name and current timestamp on the console
    print(create_file(file_name, content.format(time = current_time), current_time))
    print(current_time)