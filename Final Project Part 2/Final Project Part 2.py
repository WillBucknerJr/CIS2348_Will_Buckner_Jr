# Will Buckner Jr#
# PSID: 2101260#
from datetime import datetime

file_opener_majors = open("StudentsMajorsList-1.csv", "r")
file_opener_GPA = open("GPAList.csv", "r")
file_opener_graduation = open("GraduationDatesList.csv", "r")

full_roster_outfile = open("TestRoster.csv", "w")

Read_majors = file_opener_majors.readlines()
Read_GPAs = file_opener_GPA.readlines()
Read_GRAD_dates = file_opener_graduation.readlines()
new_lists = []
sort_list = []
Full_roster = []
Sort_dictionary = {}
GPA_dictionary = {}
Grad_dictionary = {}

with file_opener_majors, file_opener_GPA, file_opener_graduation, full_roster_outfile:
    for read_off in Read_majors:
        new_list = read_off.split(",")
        if new_list[4] == "Y\n":
            new_list[4] = "Y"
        else:
            del new_list[4]

        new_list.insert(1, new_list[3])
        del new_list[4]
        new_list.insert(2, new_list[3])
        del new_list[4]

        sort_list.append(new_list[3])
        Sort_dictionary[sort_list[-1]] = new_list

    sort_list = sorted(sort_list)
    for read_sort in sort_list:
        new_lists.append(Sort_dictionary[read_sort])

    for read_gpa in Read_GPAs:
        listA = read_gpa.split(",")
        updateA = listA[1]
        if len(updateA) == 5:
            listA[1] = updateA[0:4]
        elif len(updateA) == 4:
            listA[1] = updateA[0:3]
        else:
            listA[1] = updateA[0]
        GPA_dictionary[listA[0]] = listA[1]

    for read_dates in Read_GRAD_dates:
        listB = read_dates.split(",")
        updateB = listB[1]
        if len(updateB) == 9:
            listB[1] = updateB[0:8]
        elif len(updateB) == 10:
            listB[1] = updateB[0:9]
        else:
            listB[1] = updateB[0:10]
        Grad_dictionary[listB[0]] = listB[1]

    for read_new in new_lists:
        if read_new[len(read_new) - 1] == "Y":
            read_new.insert(4, GPA_dictionary[read_new[0]])
            read_new.insert(5, Grad_dictionary[read_new[0]])
        else:
            read_new.append(GPA_dictionary[read_new[0]])
            read_new.append(Grad_dictionary[read_new[0]])
        # Generates file for TestRoster.csv and Full Roster list
        merge_list = ",".join(read_new)
        full_roster_outfile.write(f'{merge_list}\n')
        Full_roster.append(read_new)


majors_list = []  # Start of Final Project 2
for every_line in Full_roster:  # Creates list with all majors from roster
    if every_line[1] not in majors_list:
        majors_list.append(every_line[1])

query = input(" Enter Major and GPA to search (EX. Computer Science 3.5): ")

while query.casefold() != "q":
    approved_students = []
    consider_students = []
    closest_students = []

    try:
        split_list = query.split(" ")
        gpa_string = split_list[-1]
        del split_list[-1]
        major_query = " ".join(split_list)
        gpa_query = float(gpa_string)

        # checks if the major from the query has a valid input. (valid = list len is 1. invalid = list len is 0, 2 or more.)
        query_major_filter = [major for major in majors_list if major.upper() in major_query.upper()]

        if len(query_major_filter) == 0:  # Not in list of majors
            print("No such student")
        elif len(query_major_filter) >= 2:  # 2 or more majors entered
            print("No such student. Enter major in correct format.")
        else:
            # Creates a list containing only the students within the major query
            major_filter = [line for line in Full_roster if line[1] in query_major_filter]

            gpa_start_boundary = gpa_query - 0.1
            gpa_end_boundary = gpa_query + 0.1
            consider_gpa_start = gpa_query - 0.25
            consider_gpa_end = gpa_query + 0.25

            for every_line2 in major_filter:  # Adds students to lists if within gpa query range
                students_gpa = float(every_line2[4])
                if gpa_start_boundary <= students_gpa <= gpa_end_boundary:
                    approved_students.append(every_line2)
                elif consider_gpa_start <= students_gpa <= consider_gpa_end:
                    consider_students.append(every_line2)
                else:
                    closest_students.append(every_line2)

            # Print the ID, First name, Last name, and GPA for students in ranges
            if approved_students:
                print(f"Your student(s):")
                for approved in approved_students:
                    check1 = datetime.strptime(approved[5], '%m/%d/%Y')
                    if check1 > datetime.now() and approved[-1] != "Y":
                        print(f"{approved[0]},{approved[2]},{approved[3]},{approved[4]}")

            if consider_students:
                print(f"\nYou may also consider:")
                for consider in consider_students:
                    check2 = datetime.strptime(consider[5], '%m/%d/%Y')
                    if check2 > datetime.now() and consider[-1] != "Y":
                        print(f"{consider[0]},{consider[2]},{consider[3]},{consider[4]}")

            if not approved_students and not consider_students:
                print("No such student\nStudents closest to the query:")
                for closest in closest_students:
                    check3 = datetime.strptime(closest[5], '%m/%d/%Y')
                    if check3 > datetime.now() and closest[-1] != "Y":
                        print(f"{closest[0]},{closest[2]},{closest[3]},{closest[4]}")

    except ValueError:
        print("No such student. Enter GPA in correct format.")

    query = input("\nMajor and GPA to search (EX. Computer Science 4.0): ")
