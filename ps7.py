import csv


#7.1 get_trips()
# 
# Write a function get_trips() that reads in the data in 'trips.csv' and returns a 
# list of dictionaries, where each dictionary represents a trip.

def get_trips():
    with open('trips.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        trips = []
        for row in reader:
            row_data = {'name':row['name'], 'level':row['level'], 'start_date':row['start_date'], 'location':row['location'], 'length':row['length'], 'leader':row['leader'], 'cost':row['cost'], 'description':row['description']}
            trips.append(row_data)
    return trips


#7.2 get_members()
# 
# Write a function get_members() that reads in the member data contained in 'members.csv' 
# and returns a list of dictionaries, where each dictionary represents a member.

def get_members():
    with open('members.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        members = []
        for row in reader:
            row_data = {'name':row['name'], 'address':row['address'], 'email':row['email'], 'date_of_birth':row['date_of_birth'], 'phone':row['phone']}
            members.append(row_data)
    return members


#7.3 set_trips(list_of_dictionaries)
# 
# Write a function set_trips() that takes a list of dictionaries where each dictionary represents the 
# data for a trip and SAFELY writes the data into'trips.csv'. This function does not return anything.

def set_trips(trips):
    headers = ['name', 'level', 'start_date', 'location', 'length', 'leader', 'cost', 'description']
    with open('trips.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, headers=headers)
        writer.writeheader()
        for trip in trips:
            writer.writerow({'name':trip['name'], 'level':trip['level'], 'start_date':trip['start_date'], 'location':trip['location'], 'length':trip['length'], 'leader':trip['leader'], 'cost':trip['cost'], 'description':trip['description']})


#7.4 set_members(list_of_dictionaries)
# 
# Write a function set_members() that takes a list of dictionaries where each dictionary represents the 
# data for a member and SAFELY writes the data into 'members.csv'. This function does not return anything.

def set_members():
    feildnames = ['name', 'address', 'email', 'date_of_birth', 'phone']
    with open('members.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, feildnames=feildnames)
        writer.writeheader()
        for member in members:
            writer.writerow({'name':member['name'], 'address':member['address'], 'email':member['email'], 'date_of_birth':member['date_of_birth'], 'phone':member['phone']})


if __name__ == '__main__':
    #Test code!
    print('Trip data:')
    trips = get_trips()
    print(trips)
    trips.append({'name':'Pontoon Adventure', 'start_date':'3/4/23', 'length':'1 Day', 'cost':'$50', 'location':'Lake Monroe IN', 'level':'Intermediate', 'leader':'Captain Jack', 'description':'A day on the Lake!'})
    set_trips(trips)
    
    print('Member data:')
    members=get_members()
    print('Member data:')
    print(members)
    members.append({'name':'Madison Taylor', 'date_of_birth':'7/4/2003', 'email':'madtay@gmail.com', 'address':'505 S Dunn Bloomington', 'phone':'(812)327-3294'})
    set_members(members)