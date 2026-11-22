import pickle

#adding doctor
def addDoc():
    Id=int(input("Enter doctor's id:"))
    name=input("Enter doctor's name:")
    specialization=input("Enter doctor's specialization")
    phone=int(input("Enter doctor's phone no:"))

    #Creating the dict
    rec={'Id':Id,'Name':name,'Specialization':specialization,'Phone':phone}

    #Writing the Dictionary
    f = open('doctor.dat','ab')
    pickle.dump(rec,f)
    f.close()
    
#Deleting doc
def delDoc(r):
    f = open('doctor.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f = open('doctor.dat','wb')
    for x in reclst:
        if x['Id']==r:
            continue
        pickle.dump(x,f)
    f.close()
    
#Viewing Doc
def viewDoc():
    f = open('doctor.dat','rb')
    while True:
        try:
            rec = pickle.load(f)
            print('Id:',rec['Id'])
            print('Name:',rec['Name'])
            print('Specialization',rec['Specialization'])
            print('Phone',rec['Phone'])
        except EOFError:
            break
    f.close()

#Searching doc
def searchDoc(Id):
    f = open('doctor.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['Id'] == Id:
                print('Id:',rec['Id'])
                print('Name:',rec['Name'])
                print('Specialization:',rec['Specialization'])
                print('Phone',rec['Phone'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print('Doctor not found')
    f.close()

#adding patients
def addPatients():
    Id=int(input("Enter patient's id:"))
    name=input("Enter patient's name:")
    age=int(input("Enter patient's age:"))
    gender=input("Enter patient's gender:")
    phone=int(input("Enter patient's phone no:"))

    #Creating the dict
    rec={'Id':Id,'Name':name,'Age':age,'Gender':gender,'Phone':phone}

    #Writing the Dictionary
    f1 = open('patient.dat','ab')
    pickle.dump(rec,f1)
    f1.close()

#Deleting patient
def delPatient(r1):
    f1 = open('patient.dat','rb')
    reclst = []
    while True:
        try:
            rec = pickle.load(f1)
            reclst.append(rec)
        except EOFError:
            break
    f1.close()
    f1 = open('patient.dat','wb')
    for x in reclst:
        if x['Id']==r1:
            continue
        pickle.dump(x,f1)
    f1.close()

#view patient
def viewPatient():
    f1 = open('patient.dat','rb')
    while True:
        try:
            rec = pickle.load(f1)
            print('Id:',rec['Id'])
            print('Name:',rec['Name'])
            print('Age:',rec['Age'])
            print('Gender:',rec['Gender'])
            print('Phone',rec['Phone'])
        except EOFError:
            break
    f1.close()

#Searching patient
def searchPatient(Id1):
    f1 = open('patient.dat','rb')
    flag = False
    while True:
        try:
            rec = pickle.load(f1)
            if rec['Id'] == Id1:
                print('Id:',rec['Id'])
                print('Name:',rec['Name'])
                print('Age:',rec['Age'])
                print('Gender:',rec['Gender'])
                print('Phone',rec['Phone'])
                flag = True
        except EOFError:
            break
    if flag == False:
        print('Patient not found')
    f1.close()

#booking
def Booking():
    BId=int(input("Enter booking id:"))
    Id=int(input("Enter doctor's id:"))
    Id1=int(input("Enter patient's id:"))
    date=input("Enter date")
    reason=input("Enter reason")

    #Creating the dict
    rec={'BId':BId,'Id':Id,'Id1':Id1,'date':date,'Reason':reason}

    #Writing the Dictionary
    f2 = open('booking.dat','ab')
    pickle.dump(rec,f2)
    f2.close()

#Display Booking
def display():
    f2 = open('booking.dat','rb')
    while True:
        try:
            rec = pickle.load(f2)
            print('BId:',rec['BId'])
            print('Id:',rec['Id'])
            print('Id1:',rec['Id1'])
            print('Date',rec['date'])
            print('Reason',rec['Reason'])
        except EOFError:
            break
    f2.close()

while True:
    print('Type 1 to add doc')
    print('Type 2 to del doc')
    print('Type 3 to view doc')
    print('Type 4 to search doc')
    print('Type 5 to add patients')
    print('Type 6 to del patients')
    print('Type 7 to view patients')
    print('Type 8 to search patients')
    print('Type 9 for booking')
    print('Type 10 to display booking')
    choice = int(input('Enter you choice:'))
    if choice == 1:
        addDoc()
    if choice == 2:
        r = int(input('Enter ID to search:'))
        delDoc(r)
    if choice == 3:
        viewDoc()
    if choice == 4:
        ID = int(input('Enter ID to search:'))
        searchDoc(ID)
    if choice == 5:
        addPatients()
    if choice == 6:
        r1 = int(input('Enter ID to search:'))
        delPatient(r1)
    if choice == 7:
        viewPatient()
    if choice == 8:
        ID1 = int(input('Enter ID to search:'))
        searchPatient(ID1)
    if choice == 9:
        Booking()
    if choice == 10:
        display()
    if choice == 11:
        exit()
