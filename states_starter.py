import csv
from operator import itemgetter

#4.1: Write a function to open states.csv and read in the data as a list of dictionaries
def read_states():
    with open ('states.csv','r', encoding='utf-8-sig') as csvfile:
        host_reader = csv.DictReader(csvfile)
        data = []
        for row in host_reader:
            data.append(row)
        return data


# for part 4.5. Modify the write_data() function in the slides to work with a list of dictionaries
def write_data(name, data):
    try:
        # with open(filename, 'w', newline='') as csvfile:  # if you have a PC
       with open('states.csv', 'w') as csvfile:    # if you have a Mac
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['State','Capital','Largest City','Bird,Flower'])
            for state in states:
                csv_writer.writerow(state.values())
    except IOError:
        print("No such file or directory")
    except Exception as e:
        print("Error:", e)
    print("\nFile", 'states.csv' , "saved.\n")


#main
#read in and print out the state data
states = read_states()
print(states)


#4.2: Add new data to the dictionary for some states. Add the key 'population' to the states variable 
# with the following values for these states:
# Indiana: 6845000
# Illinois: 12809000
# Ohio: 11852000
# Kentucky: 4539000
# Michigan: 10116000

for state in states:
    if state['State'] == 'Indiana':
        state['population'] = '6845000'
    if state['State'] == 'Illinois':
        state['population'] = '12809000'
    if state['State'] == 'Ohio':
        state['population'] = '11852000'
    if state['State'] == 'Kentucky':
        state['population'] = '4539000'
    if state['State'] == 'Michigan':
        state['population'] = '10116000'

print(states)


#4.3 Print out a table of the names and populations for states that now have a population 
# List in order of population, high to low
#HINT: you might need to create another data structure

state_pop = []
for state in states:
    if int(state.get('population', 0)) > 0:
        state_pop.append([state['State'], state['population']])

state_pop = sorted(state_pop, key=itemgetter(1), reverse = True)

for state in state_pop:
    if len(state[0]) < 8:
        seperator = '\t\t'
    else:
        seperator = '\t'

    print(state[0], state[1], end=seperator)


#4.4 Ask the user for the name of a state. Make sure the name is a valid state name. 
#Print out the  state flower and bird for that state



#4.5 Now write the modified CSV data back out to states.csv 
# You can't use the write_data() function from the slides as it takes a list of lists, not a list of dictionaries.
# You will need to modify write_data() to work with a list of dictionaries instead.
# Edit the function above. Don't forget to write the keys as your first line!