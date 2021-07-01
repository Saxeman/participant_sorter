# This is the Participant_Sorter code, for Documentation look at the README file

import csv
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: Add in command line input and user choice for multiple files.
    # reads in csv file to program
    # change total_entries to account for multiple file as well as to dynamically read how many people there are
    total_entries = 0
    for i in range(len(sys.argv) - 1):
        with open(str(sys.argv[i + 1])) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                total_entries += 1
    print(total_entries)
    all_data = [[0] * 8 for _ in range(total_entries)]
    with open('S1 and S1S2 Participants  - ADDL S1 JUN 15 2021.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                for i in range(8):
                    all_data[line_count][i] = row[i]
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                for i in range(8):
                    all_data[line_count][i] = row[i]
                print(f'Session:{row[0]}, uniqname:{row[1]}, UMID:{row[2]}, Role:{row[3]}, GivenName:{row[4]}, '
                      f'MiddleName:{row[5]}, Surname:{row[6]}, PersonalEmail:{row[7]}')
                line_count += 1
        print(f'Processed {line_count} lines.')
        # creates matrix for combination of all data
        print(all_data)
