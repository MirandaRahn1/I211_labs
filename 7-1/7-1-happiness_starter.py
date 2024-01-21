# 3.2 Don't Worry Be Happy
# https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021?select=world-happiness-report-2021.csv

import csv

#Our function to write out data to csv, modified from I210
def write_data(filename, data):
    """Writes out to a csv - takes in a filename and a nested list"""
    try:
        # with open(filename, 'w', newline='') as csvfile:  # if you have a PC
       with open(filename, 'w') as csvfile:    # if you have a Mac
            csv_writer = csv.writer(csvfile)
            for row in data:
                csv_writer.writerow(row)
    except IOError:
        print("No such file or directory")
    except Exception as e:
        print("Error:", e)

    print("\nFile", filename, "saved.\n")

#main

#open the csv file and create a list of the data
with open('world-happiness-report-2021.csv', encoding='utf-8-sig') as csvfile:
    host_reader = csv.DictReader(csvfile)
    data = []
    for row in host_reader:
        data.append(row)

#create the list you want to save to the file
top_ten = [['Country name', 'Regional indicator', 'Ladder score']]

#loop through the data and print the top 10
for i in range(10):
    top_ten.append([i+1, data[i]['Country name'], data[i]['Regional indicator'], data[i]['Ladder score']])
    print(f"{i+1}\t{data[i]['Country name']}\t{data[i]['Regional indicator']}\t{data[i]['Ladder score']}")
    

#write the data out to top_ten.csv
write_data('top_ten.csv', top_ten)