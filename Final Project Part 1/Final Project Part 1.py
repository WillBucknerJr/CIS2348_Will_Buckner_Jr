# Will Buckner Jr#
# PSID: 2101260#
from datetime import datetime

file_opener_majors = open("StudentsMajorsList-1.csv", "r")
file_opener_GPA = open("GPAList.csv", "r")
file_opener_graduation = open("GraduationDatesList.csv", "r")

full_roster_outfile = open("FullRoster.csv", "w")
scholarship_candidate_outfile = open("ScholarshipCandidates.csv", "w")
disciplined_student_outfile = open("DisciplinedStudents.csv", "w")

Read_majors = file_opener_majors.readlines()
Read_GPAs = file_opener_GPA.readlines()
Read_GRAD_dates = file_opener_graduation.readlines()
new_lists = []
sort_list = []
Sort_dictionary = {}
GPA_dictionary = {}
Grad_dictionary = {}
Major_dictionary = {}
testdictionarySTDNTID = {}

with file_opener_majors, file_opener_GPA, file_opener_graduation:
    for x in Read_majors:
        new_list = x.split(",")
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
    for j in sort_list:
        new_lists.append(Sort_dictionary[j])

    for y in Read_GPAs:
        listA = y.split(",")
        updateA = listA[1]
        if len(updateA) == 5:
            listA[1] = updateA[0:4]
        elif len(updateA) == 4:
            listA[1] = updateA[0:3]
        else:
            listA[1] = updateA[0]
        GPA_dictionary[listA[0]] = listA[1]

    for w in Read_GRAD_dates:
        listB = w.split(",")
        updateB = listB[1]
        if len(updateB) == 9:
            listB[1] = updateB[0:8]
        elif len(updateB) == 10:
            listB[1] = updateB[0:9]
        else:
            listB[1] = updateB[0:10]
        Grad_dictionary[listB[0]] = listB[1]

    for z in new_lists:
        if z[len(z) - 1] == "Y":
            z.insert(4, GPA_dictionary[z[0]])
            z.insert(5, Grad_dictionary[z[0]])
        else:
            z.append(GPA_dictionary[z[0]])
            z.append(Grad_dictionary[z[0]])
# File for Full Roster
        merge_list = ",".join(z)
        full_roster_outfile.write(f'{merge_list}\n')

# sort by GPA high to low
    testlist = [x for x in new_lists]
    for newGPA in testlist:
        newGPA.insert(0, newGPA[4])
        testlist = sorted(testlist, reverse=True)
    for delete in testlist:
        del delete[0]
    for sorted_gpas in testlist:
        check = datetime.strptime(sorted_gpas[5], '%m/%d/%Y')
# File for scholarship candidates
        if sorted_gpas[4] > "3.8" and check > datetime.now() and sorted_gpas[-1] != "Y":
            scholarship_candidate_outfile.write(f"{sorted_gpas[0]},{sorted_gpas[3]},{sorted_gpas[2]},{sorted_gpas[1]},{sorted_gpas[4]}\n")


# sort by graduation date old to new for disciplined students
    testlist_dates = [x for x in new_lists]
    for newDATE in testlist_dates:
        newDATE.insert(0, newDATE[5])
        newDATE[0] = datetime.strptime(newDATE[0], '%m/%d/%Y')
    testlist_dates = sorted(testlist_dates)
    for delete in testlist_dates:
        del delete[0]
# Files for disciplined students
    for bad in testlist_dates:
        if bad[-1] == "Y":
            disciplined_student_outfile.write(f"{bad[0]},{bad[3]},{bad[2]},{bad[5]}\n")


# sort by student id
    sortSTDNTID = sorted([x[0] for x in new_lists])
    for x in new_lists:
        Major_dictionary[x[0]] = x
    checkSTDNTID = [Major_dictionary[x] for x in sortSTDNTID]   # Files for each Major
    for major in checkSTDNTID:
        major_filename = f"{major[1].replace(' ', '')}.csv"
        if major[1] not in testdictionarySTDNTID.keys():
            if major[-1] == "Y":
                majors_student_outfile = open(f"{major_filename}", "w")
                majors_student_outfile.write(f"{major[0]},{major[3]},{major[2]},{major[5]},{major[6]}")
                testdictionarySTDNTID[major[1]] = 1
            else:
                majors_student_outfile = open(f"{major_filename}", "w")
                majors_student_outfile.write(f"{major[0]},{major[3]},{major[2]},{major[5]},")
                testdictionarySTDNTID[major[1]] = 1
        else:
            if major[-1] == "Y":
                majors_student_outfile = open(f"{major_filename}", "a")
                majors_student_outfile.write(f"\n{major[0]},{major[3]},{major[2]},{major[5]},{major[6]}")
            else:
                majors_student_outfile = open(f"{major_filename}", "a")
                majors_student_outfile.write(f"\n{major[0]},{major[3]},{major[2]},{major[5]},")

    majors_student_outfile.close()
    full_roster_outfile.close()
    scholarship_candidate_outfile.close()
    disciplined_student_outfile.close()
