# This is the Participant_Sorter code, for Documentation look at the README file

import csv
import sys
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # reads in csv file to program
    # change total_entries to account for multiple file as well as to dynamically read how many people there are
    total_entries = 0
    for i in range(len(sys.argv) - 2):
        with open(str(sys.argv[i + 2])) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                total_entries += 1
    # creates our emtpy matrix for holding data
    unscrubbed_data = [[0] * 9 for _ in range(total_entries)]
    line_count = 0
    for file_num in range(len(sys.argv) - 2):
        with open(str(sys.argv[file_num + 2])) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # populates matrix with values
            for row in csv_reader:
                for i in range(8):
                    unscrubbed_data[line_count][i] = row[i]
                line_count += 1
    # scrubs matrix for duplicates
    scrubbed_data = []
    for val in range(0, len(unscrubbed_data)):
        if unscrubbed_data[val][2] in scrubbed_data:
            continue
        scrubbed_data.append(unscrubbed_data[val])
    # writes everyone to the main canvas page import document
    file = open('Courses/SU2021-ccmS483457.csv', 'w')
    file.write('user_id,role,section_id\n')
    for p in range(1, line_count):
        UMID = scrubbed_data[p][2]
        file.write(UMID + ',student,SU2021-ccmS483457\n')

    sisid = []
    taking_classes = []
    # just opening our files
    with open('sisid.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            sisid.append(row)
    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            taking_classes.append(row)
    # populate the main matrix with class codes
    for row in sisid:
        num_taken = 0
        if row == 'Title':
            continue
        class_name = row[1]
        for row1 in taking_classes:
            classes_taken = row1[4]
            if class_name in classes_taken:
                student_email = row1[3]
                # compares sign up email with personal email to match people to their courses
                for row2 in scrubbed_data:
                    if row2[7] == student_email:
                        if row2[8] == 0:
                            row2[8] = row[0]
                        else:
                            scrubbed_data.append([0] * 9)
                            line_count += 1
                            for g in range(0,8):
                                scrubbed_data[line_count - 1][g] = row2[g]
                            scrubbed_data[line_count - 1][8] = row[0]
                        break
    for row in sisid:
        file = open('Courses/' + row[0] + '.csv', 'w')
        file.write('user_id,role,section_id\n')
        for p in range(0, line_count):
            if row[0] == scrubbed_data[p][8]:
                UMID = scrubbed_data[p][2]
                file.write(UMID + ',student,' + row[0] + '\n')