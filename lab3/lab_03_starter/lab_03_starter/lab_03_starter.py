import os


# Part 1: write a short program that prints out the names of all of the contents 
# of the examples/more_examples directory.
home=os.getcwd()
print(os.listdir(os.path.join(home, "examples/more_examples")))


#Part 2: Change the current working directory to the resources/code/ directory.
# Print out the names of all of the files (not directories!) and their sizes
new_directory = os.chdir(os.path.join(os.getcwd(),"resources/code/"))
for file in os.listdir(new_directory):
    if os.path.isfile(file):
        print(file, end=" ")
        print(os.path.getsize(file))


#Part 3: Rename the functions.py file to database_functions.py.
os.rename("functions.py","database_functions.py")