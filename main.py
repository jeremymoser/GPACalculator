# Jeremy G. Moser - jeremygmoser@icloud.com
# Wednesday, March 30, 2022
# GPA Calculator

numClasses = input("Enter the number of classes you are taking this semester: ")
semesterGPA = [numClasses]

x = 0
while x < int(numClasses):
    print("\nCourse #" + str(x + 1) + " Details:")
    courseName = input(">> Enter course name: ")
    courseCreditHours = input(">> Enter course credit hour(s): ")
    courseLetterGrade = input(">> Enter course letter grade: ")
    semesterGPA.append([courseName, courseLetterGrade, courseCreditHours])
    x += 1

c = 1
cumCreditHours = 0
cumGradePoints = 0
print("\n***** SEMESTER SUMMARY *****")
print("\n{:10}".format(str("Course #")) + "{:50}".format(str("Course Name")) + "{:10}".format(str("Grade"))
      + "{:10}".format(str("Credits")) + "{:10}".format(str("Points")) + "{:10}".format(str("GPA")))
print(str("----------------------------------------------------------------------------------------------------"))
while c < len(semesterGPA):
    courseName = semesterGPA[c][0]
    courseLetterGrade = semesterGPA[c][1]
    courseCreditHours = semesterGPA[c][2]
    courseGradeValue = 0
    if courseLetterGrade.upper() == "A":
        courseGradeValue = 4
    elif courseLetterGrade.upper() == "B":
        courseGradeValue = 3
    elif courseLetterGrade.upper() == "C":
        courseLetterValue = 2
    elif courseLetterGrade.upper() == "D":
        courseGradeValue = 1
    elif courseLetterGrade.upper() == "F":
        courseGradeValue = 0
    else:
        courseGradeValue = 0
    courseGPA = (int(courseCreditHours) * int(courseGradeValue)) / int(courseCreditHours)
    cumCreditHours += int(courseCreditHours)
    cumGradePoints += int(courseCreditHours) * int(courseGradeValue)

    print("{:10}".format("#" + str(c)) + "{:50}".format(str(courseName))
          + "{:10}".format(str(courseLetterGrade)) + "{:10}".format(str(courseCreditHours))
          + "{:10}".format(str(courseGradeValue)) + "{:10}".format(str(courseGPA)))
    print(str("----------------------------------------------------------------------------------------------------"))
    c += 1
print("Total course(s): " + str(numClasses))
print("\nSemester Cumulative GPA: " + str(int(cumGradePoints) / int(cumCreditHours)))
