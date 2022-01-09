import random
import sys
sys.setrecursionlimit(10**6)

print("hello")


class yeargroupclass():
    def __init__(self, name, year, form):
        self.name = name
        self.year = year
        self.form = form
        self.reqlist = []
        self.studentlist = []
        self.emptyDay = []
        self.week = [["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
                    ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],]


    def changename(self,name):
        yeargroupclass.__name__ = name

    def addreq(self, req):
        temp = self.reqlist
        temp.append(req)
        self.reqlist = temp

    def getreq(self):
        return self.reqlist

    def addstudent(self, student):
        temp = self.studentlist
        temp.append(student)
        self.studentlist = temp

    def clearWeek(self):
        self.week = [["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"],
                     ["SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT", "SUBJECT"], ]

    def addSubjectToWeek(self,day, period, subject):
        temp = self.week
        temp[day][period] = subject
        self.week = temp

    def isSubject(self, day,period, subject):
        if self.week[day][period] == subject:
            return True
        else:
            return False

    def countFree(self):
        count = 0
        for x in range(len(self.week)):
            for y in range(len(self.week[x])):
                if self.week[x][y] == "SUBJECT":
                    count = count + 1

                    temp = [x, y]
                    self.emptyDay.append(temp)

        return count





class schoolset():
    def __init__(self):
        self.yeargroup = [7,8,9,10,11,12,13]
        self.classlist = []
        self.mastertable = []
        self.simutaneousClass = {
            "Maths" : 6,
            "English" : 6,
            "Science" : 6,
            "Languages" : 6,
            "Humanity" : 6,
            "PE" : 12,
        }


    def getclasslist(self):
        return self.classlist

    def addclasslist(self, addclass):
        temp = self.classlist
        temp.append(addclass)
        self.classlist = temp

    def addmastertable(self,mastertable):
        self.mastertable = mastertable
    def getmastertable(self):
        return self.mastertable

    def iterateTable(self):
        randomClassint = random.randint(0,len(self.classlist) - 1)
        assignSubjectClass = self.classlist[randomClassint]
        subjectlist = assignSubjectClass.reqlist
        if len(subjectlist) != 0:
            randomSubject = random.randint(0,len(subjectlist) -1)

            if subjectlist[randomSubject][1] > 0:
                assignSubjectClass.countFree()
                randomDayPeriod = random.randint(0,len(assignSubjectClass.emptyDay)-1)
                dayPeriod = assignSubjectClass.emptyDay[randomDayPeriod]
                day = dayPeriod[0]
                period = dayPeriod[1]
                assignSubjectClass.addSubjectToWeek(day,period,subjectlist[randomSubject][0])
                print(assignSubjectClass.countFree())

                subjectlist[randomSubject][1] = subjectlist[randomSubject][1] - 1
            else:
                del(subjectlist[randomSubject])

        assignSubjectClass.reqlist = subjectlist

        self.classlist[randomClassint] = assignSubjectClass

    def checkDone(self):
        done = True
        lowVal = 100
        indexLow = 0
        for x in range(len(self.classlist)):
            if self.classlist[x].countFree() != 0:
                done = False
                if self.classlist[x].countFree() < lowVal:
                    lowVal = self.classlist[x].countFree()
                    indexLow = x

        print(self.classlist[x].week)
        print(lowVal)
        return done

    def process(self):
        while self.checkDone() == False:
            self.iterateTable()







class student():
    def __init__(self,fname,sname, year, form):
        self.fname = fname
        self.sname = sname
        self.year = year
        self.form = form

    def changename(self):
        fname = self.fname
        lname = self.sname
        fullname = fname + lname
        student.changename(fullname)



school = schoolset()

formlist = ["H1","H2","E1","E2","F1","F2"]
yeargroup = [7,8,9,10,11,12,13]

for x in range(len(yeargroup)):
    for y in range(len(formlist)):
        tempname = str(yeargroup[x])+formlist[y]
        #print(tempname)
        temp = yeargroupclass(tempname,yeargroup[x],formlist[y])
        school.addclasslist(temp)
        school.getclasslist()[-1].changename(tempname)

        for z in range(30):
            fname = "Student" + tempname
            lname = "Student" + str(z)
            temp = student(fname,lname, x, y)


#print(school.getclasslist())

#requirements

requirements = [[7,["Maths",9],["English",9],["Languages",9],["Science",9],["Humanity",9],["PE",3],["Oracy",1],["PSHE",1]],
                [8,["Maths",9],["English",9],["Languages",9],["Science",9],["Humanity",9],["PE",3],["Oracy",1],["PSHE",1]],
                [9,["Maths",6],["English",6],["LanguagesChoice",6],["Physics",6],["Chemistry",6],["Biology",6],["Humanity",6],["Creative",6],["PE",1],["PSHE",1]],
                [10,["Maths",6],["English",6],["LanguagesChoice",6],["Physics",6],["Chemistry",6],["Biology",6],["Humanity",6],["Creative",6],["PE",1],["PSHE",1]],
                [11,["Maths",6],["English",6],["LanguagesChoice",6],["Physics",6],["Chemistry",6],["Biology",6],["Humanity",6],["Creative",6],["PE",1],["PSHE",1]],
                [12,["Maths",9],["English",9],["Languages",9],["Science",9],["Humanity",9],["PE",3],["Oracy",1],["PSHE",1]],
                [13,["Maths",9],["English",9],["Languages",9],["Science",9],["Humanity",9],["PE",3],["Oracy",1],["PSHE",1]],]

for x in range(len(requirements)):
    temp = school.getclasslist()
    for y in range(len(temp)):
        if temp[y].year == requirements[x][0]:
            for a in range(1,len(requirements[x])):
                school.getclasslist()[y].addreq(requirements[x][a])


print(school.getclasslist()[15].name)
print(school.getclasslist()[15].getreq())

school.process()
"""
week = [["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],
        ["SUBJECT","SUBJECT","SUBJECT","SUBJECT","SUBJECT"],]
mastertable = []

for x in range(len(school.getclasslist())):
    metadata = []
    metadata.append(school.getclasslist()[x].name)
    metadata.append(week)
    mastertable.append(metadata)

print(mastertable)
#STRUCTURE
#[ CLASSNAME [WEEK],[ CLASS, [WEEK] ],]..
#WEEK =  [SUBJECT,SUBJECT,SUBJECT ...]
#WEEK index refers to period and position, index/5 gives the day in the 2 week cycle.

"""








#ASSIGN SUBJECTS

