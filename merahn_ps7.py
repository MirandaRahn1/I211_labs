import csv


#7.1 get_trips()
# 
# Write a function get_trips() that reads in the data in 'trips.csv' and returns a 
# list of dictionaries, where each dictionary represents a trip.

def get_trips():
    # reading the data 
    with open('trips.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # create empty list
        trips = []
        for row in reader:
            row_data = {'name': row['name'], 'level': row['level'], 'start_date': row['start_date'], 'location': row['location'], 'length': row['length'], 'leader': row['leader'], 'cost': row['cost'], 'description': row['description']}
            # appending dictionaries to list 
            trips.append(row_data)
    # returning the list of dictionaries
    return trips

# test print
# print(get_trips())


#7.2 get_members()
# 
# Write a function get_members() that reads in the member data contained in 'members.csv' 
# and returns a list of dictionaries, where each dictionary represents a member.

def get_members():
    # reading the data
    with open('members.csv', 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # create empty list
        members = []
        for row in reader:
            row_data = {'name': row['name'], 'address': row['address'], 'email': row['email'], 'date_of_birth': row['date_of_birth'], 'phone': row['phone']}
            # appending dictionaries to list
            members.append(row_data)
    # returning list of dictionaries 
    return members

# test print
# print(get_members())


#7.3 set_trips(list_of_dictionaries)
# 
# Write a function set_trips() that takes a list of dictionaries where each dictionary represents the 
# data for a trip and SAFELY writes the data into'trips.csv'. This function does not return anything.

def set_trips(trips):
    # getting the headers
    fieldnames = list(trips[0].keys())
    # writing data into new csv because it kept deleting my data so I wrote it into a new csv file so it wouldn't get confused
    with open('new_trips.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #I looked up how to use DictWriter because I wasn't sure if I could just use csv.writer, and it told me I needed fieldnames
        for trip in trips:
            writer.writerow(trip)


#7.4 set_members(list_of_dictionaries)
# 
# Write a function set_members() that takes a list of dictionaries where each dictionary represents the 
# data for a member and SAFELY writes the data into 'members.csv'. This function does not return anything.

def set_members(members):
    # getting the headers
    fieldnames = list(members[0].keys())
    # again, writing data into new csv file so it doesn't override and get confusing 
    with open('new_members.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
        # using fieldnames again 
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for member in members:
            writer.writerow(member)


# main
if __name__ == '__main__':
    #Test code!
    print('Trip data:')
    trips = get_trips()
    trips.append({'name':'Pontoon Adventure', 'start_date':'3/4/23', 'length':'1 Day', 'cost':'$50', 'location':'Lake Monroe IN', 'level':'Intermediate', 'leader':'Captain Jack', 'description':'A day on the Lake!'})
    print(trips)
    set_trips(trips)
    
    members = get_members()
    print('Member data:')
    print(members)
    members.append({'name':'Madison Taylor', 'date_of_birth':'7/4/2003', 'email':'madtay@gmail.com', 'address':'505 S Dunn Bloomington', 'phone':'(812)327-3294'})
    set_members(members)
