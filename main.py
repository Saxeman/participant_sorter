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
    unscrubbed_data = [[0] * 7 for _ in range(total_entries)]
    line_count = 0
    for file_num in range(len(sys.argv) - 2):
        with open(str(sys.argv[file_num + 2])) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # populates matrix with values
            for row in csv_reader:
                for i in range(6):
                    unscrubbed_data[line_count][i] = row[i]
                line_count += 1
    # scrubs matrix for duplicates based on UMID
    participants = []
    for val in range(0, len(unscrubbed_data)):
        if unscrubbed_data[val][1] in participants:
            continue
        participants.append(unscrubbed_data[val])
    # writes everyone to the main canvas page import document
    file = open('Courses/SU2021-ccmS483457.csv', 'w')
    file.write('user_id,role,section_id\n')
    for p in range(1, line_count):
        offset = 0
        if int(participants[p][1]) < 10000000:
            val = 100000000 - int(participants[p][1])
            for i in map(int, str(val)):
                if i != 9:
                    break
                offset += 1
        UMID = participants[p][1]
        file.write('0' * offset + UMID + ',student,SU2021-ccmS483457\n')

    sisid = []
    enrollment = []
    # just opening our files
    with open('sisid.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            sisid.append(row)
    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            enrollment.append(row)
    # populate the main matrix with class codes
    for row in sisid:
        num_taken = 0
        if row[0] == 'uniqname':
            continue
        class_name = row[1]
        for enrolled in enrollment:
            course_list = enrolled[4]
            if class_name in course_list:
                student_email = enrolled[3]
                # compares sign up email with personal email to match people to their courses
                for participant in participants:
                    if participant[5] == student_email:
                        if [6] == 0:
                            participant[6] = row[0]
                        else:
                            participants.append([0] * 7)
                            line_count += 1
                            for g in range(0,6):
                                participants[line_count - 1][g] = participant[g]
                            participants[line_count - 1][6] = row[0]
                        break
    # writes everything into saved CSV's
    for row in sisid:
        file = open('Courses/' + row[0] + '.csv', 'w')
        file.write('user_id,role,section_id\n')
        for p in range(0, line_count):
            if row[0] == participants[p][6]:
                offset = 0
                if int(participants[p][1]) < 10000000:
                    val = 100000000 - int(participants[p][1])
                    # print(val)
                    for i in map(int, str(val)):
                        if i != 9:
                            break
                        offset += 1
                UMID = participants[p][1]
                file.write('0' * offset + UMID + ',student,' + row[0] + '\n')