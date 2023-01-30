# importing os here
import os

# Practice Set 3
# ! Use this file as your starter file
# ! Do not move this file outside of the provided directory and files
# ! Reference the slides for Practice Set 3 for details on using the os module
# os module documentation:
# https://docs.python.org/3/library/os.html?highlight=os#module-os

# PS 3.1
# Write a function directory_choice() that prints the names of all the 
# directories in the current working directory (but not the files), 
# then ask the user to choose one of the directories. 

# fuction definition
def directory_choice():
    my_list = (os.listdir(os.path.join(home, '')))
    return my_list

# ask user to chose directory and display the directories
home=os.getcwd()
print('Current Directories:')
my_list = directory_choice()
print(directory_choice())
user_input = input('Please select a directory: ')

# If the user gives you something that isn’t valid (isn’t a directory name), 
# ask again until it’s a valid directory name.

# checking if user inputs a valid directory
for my_list in (os.listdir(home)):
    if (os.path.isdir(user_input)):
        print('Selected directory: ', user_input)
        break
    else:
        print('That is not a valid directory, try again')
        user_input = input('Please select a directory: ')

# Example output:
# Current Directories:
# ['more_files', 'other_files'] 
# Please select a directory: files
# That is not a valid directory, try again
# Please select a directory: more_files
# Selected directory: more_files


# PS 3.2
# Using the os module and your file skills,
# create three new files in our current directory:
# file-4.txt, file-5.txt and file-6.txt




# PS 3.3
# Expand your code from PS 3.1 by writing a new function print_files()
# In your main, once you have selected a valid directory (PS 3.1):
# add functionality to move into the selected directory, 
# and then print out all valid file names
# (each file name should print on its own line, do not print any directories)

# def print_files():
    # print the files

# move into selected directory
# new_directory = os.chdir(os.path.join(os.getcwd(), user_input))
# for file in os.listdir(new_directory):
#     if os.path.isfile(file):
#         print(file, end=" ")

# Example output:
# Current Directories:
# ['more_files', 'other_files'] 
# Please select a directory: files
# That is not a valid directory, try again
# Please select a directory: more_files
# Selected directory: more_files
# Available files:
# more-1.txt
# more-2.txt




