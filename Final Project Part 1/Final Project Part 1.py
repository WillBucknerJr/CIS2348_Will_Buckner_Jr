# Will Buckner Jr#
# PSID: 2101260#

from datetime import datetime

file_opener_majors = open("StudentsMajorsList-1.csv", "r")
file_opener_GPA = open("GPAList.csv", "r")
file_opener_graduation = open("GraduationDatesList.csv", "r")

full_roster_outfile = open("FullRoster.csv", "w")
scholarship_candidate_outfile = open("ScholarshipCandidates.csv", "w")
disciplined_student_outfile = open("DisciplinedStudents.csv", "w")

FOM = file_opener_majors.readlines()
FOGPA = file_opener_GPA.readlines()
FOGRAD = file_opener_graduation.readlines()
new_lists = []
sort_list = []
Sort_dicta = {}
GPA_dicta = {}
Grad_dicta = {}
Major_dicta = {}
testdictionary = {}
testdictionaryb = {}
testdictionaryc = {}

with file_opener_majors, file_opener_GPA, file_opener_graduation:
    for x in FOM:
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
        Sort_dicta[sort_list[-1]] = new_list

    sort_list = sorted(sort_list)
    for j in sort_list:
        new_lists.append(Sort_dicta[j])

    for y in FOGPA:
        listA = y.split(",")
        updateA = listA[1]
        if len(updateA) == 5:
            listA[1] = updateA[0:4]
        elif len(updateA) == 4:
            listA[1] = updateA[0:3]
        else:
            listA[1] = updateA[0]
        GPA_dicta[listA[0]] = listA[1]

    for w in FOGRAD:
        listB = w.split(",")
        updateB = listB[1]
        if len(updateB) == 9:
            listB[1] = updateB[0:8]
        elif len(updateB) == 10:
            listB[1] = updateB[0:9]
        else:
            listB[1] = updateB[0:10]
        Grad_dicta[listB[0]] = listB[1]

    for z in new_lists:
        if z[len(z) - 1] == "Y":
            z.insert(4, GPA_dicta[z[0]])
            z.insert(5, Grad_dicta[z[0]])
        else:
            z.append(GPA_dicta[z[0]])
            z.append(Grad_dicta[z[0]])

        line = ",".join(z)
        full_roster_outfile.write(f'{line}\n')  # File for Full Roster

    testlist = sorted([x[4] for x in new_lists], reverse=True)  # sort by GPA high to low
    for x in new_lists:
        testdictionary[x[4]] = x
    new_lists_GPA = [testdictionary[x] for x in testlist]
    for new in new_lists_GPA:
        check = datetime.strptime(new[5], '%m/%d/%Y')
        if new[4] > "3.8" and check > datetime.now() and new[-1] != "Y":  # File for scholarship candidates
            scholarship_candidate_outfile.write(f"{new[0]},{new[3]},{new[2]},{new[1]},{new[4]}\n")

    check = sorted([datetime.strptime(x[5], '%m/%d/%Y') for x in new_lists])  # sort by graduation date old to new
    check2 = [datetime.strftime(x, '%m/%d/%Y') for x in check]
    for x in new_lists:
        testdictionaryb[x[5]] = x
    new_lists_Discipline = [testdictionaryb[x] for x in check2]
    for bad in new_lists_Discipline:
        if bad[-1] == "Y":  # Files for disciplined students
            disciplined_student_outfile.write(f"{bad[0]},{bad[3]},{bad[2]},{bad[5]}\n")

    check = sorted([x[0] for x in new_lists])  # sort by student id
    for x in new_lists:
        testdictionaryc[x[0]] = x
    check3 = [testdictionaryc[x] for x in check]
    for major in check3:
        major_filename = f"{z[1].replace(' ', '')}.csv"  # Files for each Major
        if major[1] not in Major_dicta.keys():
            if major[-1] == "Y":
                majors_student_outfile = open(f"{major_filename}.csv", "w")
                majors_student_outfile.write(f"{major[0]},{major[3]},{major[2]},{major[5]},{major[6]}")
                Major_dicta[major[1]] = 1
            else:
                majors_student_outfile = open(f"{major_filename}.csv", "w")
                majors_student_outfile.write(f"{major[0]},{major[3]},{major[2]},{major[5]},")
                Major_dicta[major[1]] = 1
        else:
            if major[-1] == "Y":
                majors_student_outfile = open(f"{major_filename}.csv", "a")
                majors_student_outfile.write(f"\n{major[0]},{major[3]},{major[2]},{major[5]},{major[6]}")
            else:
                majors_student_outfile = open(f"{major_filename}.csv", "a")
                majors_student_outfile.write(f"\n{major[0]},{major[3]},{major[2]},{major[5]},")

    majors_student_outfile.close()
    full_roster_outfile.close()
    scholarship_candidate_outfile.close()
    disciplined_student_outfile.close()
