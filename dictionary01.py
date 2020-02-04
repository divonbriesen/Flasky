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
            'noshow': [],
            'oneshow': [3],
            'twoshow': [4, 0],
            'threeshow': [0, 44, 99]
         }

for thisUser in gradebook:
    theseGrades = gradebook.get(thisUser)
    sumOfGrades = 0

    summaryMessage = thisUser

    if len(theseGrades) == 0:
        summaryMessage += "has no grades."

    elif len(theseGrades) == 1:
        summaryMessage += "'s grade is: ", theseGrades[0],
        " - which averages to: ", format(theseGrades[0], '.2f')
    else:
        for aGrade in theseGrades:
            sumOfGrades += aGrade

        averageGrade = sumOfGrades/len(theseGrades)

        listOfGrades = theseGrades[0], theseGrades[1], theseGrades[2]

        summaryMessage = "'s grades are: and so on - which average to: ", format(averageGrade, '.2f')

    print(summaryMessage)
# end for thisUser in gradebook

aListOfAttributeValues = {
                            "Personal Background"        : 'I was born in the mountains of North Carolina in a small town called "Linville Falls". I\'ve spent most of my years here in NC but also lived for a few  years in Palmetto, Florida.',
                            "Professional Background"    : 'In high school I worked as a cashier at Food Lion. To help pay for my first degree I worked as a Veterinary Assistant at two different clinics. Once	I	completed my degree I taught high school band for 8 years. I continue to work as a Private Music Teacher as well as a Woodwind Instructor for East Lincoln HS and Butler HS. I primarily teach Flute but I also have Clarinet, Saxophone, Oboe, and Bassoon students. In my spare time I still perform on flute with other professionals at area concerts and local arts festivals. ',
                            "Academic Background"       : 'BSED in Music Education from Western Carolina University \'07',
                            "Background in this Field"  : 'Blargh',
                            "Primary Computer Platform" : 'PC/Windows 10',
                            "My Courses"                : [
                            ["WEB115-85", "Web Markup and Scripting", "Have you met D.I.?"], 
																["CSC151-91", "JAVA Programming", "Required for program"],
																["CSC152-90", "SAS", "I thought it might be wise to expose myself to some financial programming"], 
																["CTS240-51", "Project Management", "Required for program"]
															 ],
															 
							"Something to Remember me by" : "My hair. It's been every color and is currently purple.",
							"I Would Also Like to Share"  : "I am a gamer. I love Star Trek and Star Wars and all things geeky and nerdy. I play Pokemon Go. "
                        }