#    1/30/2020  joel moore dictionary01.py

'''
this will access a dictionary of student grades 
not all students have the same number of grades
the code below will calculate the average for each student

'''

gradebook = {
            'jack': [85, 98, 74], 
            'susan': [55, 66, 88, 97], 
            'fred': [88, 55, 78, 94, 81],
            'slacker': [33, 0, 29,],
            'noshow': [0]
         }

for thisUser in gradebook:
    theseGrades = gradebook.get(thisUser)
    sumOfGrades = 0

    for aGrade in theseGrades:
        sumOfGrades += aGrade
    averageGrade = sumOfGrades/len(theseGrades)

    print('The average grade for', thisUser, 'is', format(averageGrade,'.2f'))
        
