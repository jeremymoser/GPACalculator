# Jeremy G. Moser - jeremygmoser@icloud.com
# Thursday, April 7, 2022
# GPA Calculator

numClasses = input("Enter the number of classes you are taking this semester: ")
semesterGPA = [numClasses]

x = 0
while x < int(numClasses):
    print("\nCourse #" + str(x + 1) + " Details:")
    courseName = input(">> Enter course name: ")
    courseCreditHours = float(input(">> Enter course credit hour(s): "))
    courseLetterGrade = input(">> Enter course letter grade: ")
    semesterGPA.append([courseName, courseLetterGrade, courseCreditHours])
    x += 1

c = 1
cumGradeValues = 0
cumCreditHours = 0
cumGradePoints = 0

print("\n{:*^117}".format(str("  SEMESTER SUMMARY  ")))
print("\n{:10}".format(str("Course #")) + "{:50}".format(str("Course Name"))
    + "{:>10}".format(str("Grade")) + "{:>15}".format(str("Grade Value"))
    + "{:>13}".format(str("Credit(s)")) + "{:>12}".format(str("Point(s)"))
    + "{:>7}".format(str("GPA")))
print("{:-<117}".format(str("")))

while c < len(semesterGPA):
    courseName = semesterGPA[c][0]
    courseLetterGrade = semesterGPA[c][1]
    courseCreditHours = semesterGPA[c][2]
    courseGradeValue = 0
    if courseLetterGrade.upper() == "A":
        courseGradeValue = 4.0
    elif courseLetterGrade.upper() == "B":
        courseGradeValue = 3.0
    elif courseLetterGrade.upper() == "C":
        courseGradeValue = 2.0
    elif courseLetterGrade.upper() == "D":
        courseGradeValue = 1.0
    elif courseLetterGrade.upper() == "F":
        courseGradeValue = 0.0
    else:
        courseGradeValue = 0.0
    courseGPA = (float(courseCreditHours) * float(courseGradeValue)) / float(courseCreditHours)
    cumGradeValues += float(courseGradeValue)
    cumCreditHours += float(courseCreditHours)
    cumGradePoints += float(courseCreditHours) * float(courseGradeValue)

    print("{:10}".format("#" + str(c) + ":") + "{:50}".format(str(courseName))
          + "{:>10}".format(str(courseLetterGrade)) + "{:>15}".format(str(courseGradeValue))
          + "{:>13}".format(str(courseCreditHours)) + "{:>12}".format(str(float(courseGradeValue) * float(courseCreditHours)))
          + "{:>7}".format(str(courseGPA)))
    print("{:-<117}".format(str("")))
    c += 1

print("{:60}".format(str("Total Course(s): " + str(numClasses))) + "{:>10}".format("")
    + "{:>15}".format(str(cumGradeValues))
    + "{:>13}".format(str(cumCreditHours)) + "{:>12}".format(str(cumGradePoints))
    + "{:>7}".format(str(float(cumGradePoints) / float(cumCreditHours))))
print("{:=<117}".format(str("")))
print()
print("{:*<117}".format(str("")))