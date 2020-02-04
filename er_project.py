import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.minsize(800, 500)
root.title('Project for Warium')


# --------- Data ---------------

employeeList = [['First Name', 'Second Name', 'Age', 'Salary', 'Department'],
                ['Jose', 'Alex', 29, 2000, 'Marketing'],
                ['Maria', 'Alex', 28, 1500, 'Accounts'],
                ['John', 'Michael', 45, 1200, 'Administration'],
                ['Yasar', 'Ikrimah', 33, 3500, 'HR'],
                ['Fahad', 'Abdulla', 48, 4000, 'Engineering'],
                ['Noufal', 'Rahman', 29, 1500, 'Marketing'],
                ['Rick', 'Novak', 55 , 4000 , 'R & D'],
                ['Susan', 'Connor', 35 , 1500 , 'Accounts'],
                ['Margaret', 'Adelman', 32 , 3100 , 'Administration'],
                ['Ronald', 'Barr', 41 , 2800 , 'R & D'],
                ['Marie', 'Broadbet', 51 , 1200 , 'Accounts'],
                ['Roger', 'Lum', 30 , 3600 , 'Marketing'],
                ['Marlene', 'Donahue', 57 , 2100 , 'HR'],
                ['Jeff', 'Johnson', 38 , 2800 , 'Administration'],
                ['Melvin', 'Forbis', 46 , 4000 , 'R & D '],
                ['Ernest', 'Elliot', 58 , 2500 , 'Marketing'],
                ['Helen', 'Emmert', 36 , 3900 , 'Accounts'],
                ['Eric', 'Hoestra', 45 , 1200 , 'Administration'],
                ['Miguel', 'Thomas', 30 , 2500 , 'R & D'],
                ['Robert', 'Hall', 45 , 1400 , 'Marketing'],
                ['Gary', 'Cole', 37 , 3800 , 'Engineering'],
                ['Augustine', 'Ebrone', 48 ,  2100, 'Accounts'],
                ['Orpha', 'Insley',59 , 1400 , 'HR'],
                ['Anne', 'Green', 31 , 2400 , 'Administration'],
                ['Jose', 'Lee', 44 , 3900 , 'Marketing'],
                ['Justin', 'White', 58 , 3800 , 'R & D'],
                ['Mia', 'Law',32  , 2100 , 'Accounts'],
                ['Nicole', 'Christin', 60 , 3900 , 'HR'],
                ['Olivia', 'King',42 , 2400 , 'Administration'],
                ['Sophia', 'Wood', 51 , 1400 , 'Marketing'],
                ['Robert', 'Western', 34 , 4000 , 'Engineering'],
                ['Tyler', 'Linken', 48 ,  3900, 'Accounts'],
                ['Victoria', 'Adcox', 43 , 2400 , 'R & D'],
                ['John', 'Smith', 33 , 3800 , 'Marketing'],
                ['Suzan', 'Mayne', 52 , 1400 , 'Engineering'],
                ['Craig', 'Peters', 47 ,  2400, 'HR'],
                ['Rajesh', 'Menon', 35 , 3900 , 'Accounts'],
                ['Kriti', 'Sharma', 46 , 2400 , 'Administration'],
                ['Pallavi', 'Roy', 53 , 3800 , 'Marketing'],
                ['Aman', 'Varma', 36 , 3900 , 'R & D'],
                ['Cooper', 'Judy', 44 , 2100 ,'Accounts'],
                ['Lily', 'Kate', 54 ,  2100, 'Administration'],
                ['Jim', 'Nancy', 42 , 2400 , 'HR'],
                ['Ueee', 'Henry', 37 , 3800 , 'Engineering'],
                ['Melody', 'Bob', 55 ,  1400, 'Accounts'],
                ['Yoyo', 'Teddy', 40 ,3900  , 'Marketing'],
                ['Huston', 'Rose', 38 ,3800  , 'R & D'],
                ['Gary', 'Frank', 56 , 2100 , 'Administration'],
                ['Grace', 'Judy', 41 , 2400 , 'HR'],
                ['Aaaqil', 'Hakeem ', 40 , 1000 , 'Accounts'],
                ['Ayub', 'Farid', 59 , 3200 , 'Engineering'],
                ['Sawsan', 'Dymek', 39 , 2400 , 'Marketing'],
                ['Nijah', 'Fadel', 41 , 1100 , 'Administration'],
                ['Yeira', 'Aijaz', 58 , 1500 , 'R & D'],
                ['Zeinab', 'Issam', 38 , 3800, 'Accounts'],
                ['Casildo', 'Murat', 42 , 3200 , 'HR'],
                ['Aahil', 'Baadi', 57 , 1200 , 'Engineering'],
                ['Elaf', 'Hamd', 37 , 2700 , 'Administration'],
                ['Ghani', 'Hasan', 43 , 2000 , 'Marketing'],
                ['Arqa', 'Matin', 56 , 3800 , 'Accounts'],
                ['Zahrah', 'Arvio', 36 , 1200 , 'R & D'],
                ['Fawaz ', 'Imara', 44 , 3200 , 'Administration'],
                ['Amjad', 'Ali', 55 , 2500 , 'Engineering'],
                ['Wijdan', 'Khayr', 35 , 1200 , 'HR'],
                ['Izaan', 'Aabid', 45 , 3200 , 'Engineering'],
                ['Sahil', 'Rashid', 54 , 3800 , 'Accounts'],
                ['Mehul', 'Gulzar', 34 , 3200 , 'R & D'],
                ['Zivah', 'Qadir', 46 , 1200 , 'Marketing'],
                ['Muzaffar', 'Khader', 53 , 3200 , 'Administration'],
                ['Sajjad', 'Rafiq', 33 , 3000 , 'Engineering'],
                ['Aadeel', 'Daleel', 47 , 3800 , 'Accounts'],
                ['Ghalib', 'Mazhar', 32 , 3200 , 'Engineering'],
                ['Zul', 'Najaf', 52 , 1200 , 'Accounts'],
                ['Waheed', 'Saleh', 48 , 3200 , 'R & D'],
                ['Jawad', 'Aashir', 31 , 3500 , 'Marketing'],
                ['Fadwa', 'Azhar', 51 , 1200 , 'Administration'],
                ['Sanam', 'Heer', 49 , 3200 , 'Engineering'],
                ['Bajes', 'Kabir', 30 , 3200 , 'Engineering'],
                ['Muhammed', 'Hayee', 50 , 3800 , 'HR'],
                ['Sayyid', 'Mehul', 50 , 1200 , 'R & D'],
                ['Baasit', ' Kareem', 41 , 2400 , 'Accounts'],
                ['Sameer', 'Rahman', 49 , 4000 , 'Marketing'],
                ['Abdul ', 'Wahid', 51 , 1900 , 'Engineering'],
                ['Uhuru', 'Pal', 42 , 3200 , 'Accounts'],
                ['Muhammad ', 'Safi', 48 , 1200 , 'Administration'],
                ['Rahim', 'Firyal', 52 , 3800 , 'R & D'],
                ['Talora', 'Farukh', 43 , 3200 , 'HR'],
                ['Zafir', ' Atqa ', 47 , 4000 , 'Engineering'],
                ['Muhammed', 'Arzan', 53 , 1200 , 'Administration'],
                ['Gulam', 'Omar', 44 , 4000 , 'Marketing'],
                ['Shaia', 'Bari', 46 , 3200 , 'Engineering'],
                ['Mahid', 'Safwan ', 54 , 1200 , 'Accounts'],
                ['Sezen', 'Alim', 45 , 3800 , 'Engineering'],
                ['Hiten', 'Haroon', 45 , 2600 , 'HR'],
                ['Naved', 'Mustafa', 55 , 3800 , 'Engineering'],
                ['Zaeem', 'Anum', 46 , 3200 , 'R & D'],
                ['Faraz', 'Malik', 44 , 1200 , 'Accounts'],
                ['Dina', 'Ekbal', 56 , 4000 , 'Administration'],
                ['Nasir', 'Abbudin', 47 , 3800 , 'Marketing'],
                ['Kanz', 'Rafayet ', 43 , 3800 , 'HR']]

# ------ functions ------------


def ResetClick():
    entryNames.delete(0, tk.END)
    entryAgeFrom.delete(0, tk.END)
    entryAgeTo.delete(0, tk.END)
    entrySalaryFrom.delete(0, tk.END)
    entrySalaryTo.delete(0, tk.END)


def FilterNames():
    temp = varNamesEntry.split(',')
    nameList = []

    for i in range(len(temp)):
        nameList.append(temp[i].strip().lower())

    for name in nameList:
        for i in range(1, len(employeeList)):
            if str(name) in employeeList[i][0].lower() or name in employeeList[i][1].lower():
                indexList.append(i)


def FilterAge():
    global varAgeFrom
    global varAgeTo
    global messageString

    messageString=''

    if varAgeFrom == '':
        varAgeFrom = 0

    if varAgeTo == '':
        varAgeTo = 199

    try:
        int(varAgeFrom)
        int(varAgeFrom)
    except ValueError:
        messageString = 'Wrong input format in Age Field' 
    else:
        global indexList
        tempList = indexList.copy()
        indexList = []
        for i in tempList:
            if employeeList[i][2] in range(int(varAgeFrom), int(varAgeTo)+1):
                indexList.append(i)


def FilterSalary():
    global varSalaryFrom
    global varSalaryTo
    global messageString
    
    if varSalaryFrom == '':
        varSalaryFrom = 0

    if varSalaryTo == '':
        varSalaryTo = 99999999999999

    try:
        int(varSalaryFrom)
        int(varSalaryTo)
    except ValueError:
        if messageString:
            messageString = 'Wrong input format in Age and Salary Fields'
        else:
            messageString = 'Wrong input format in Salary Field'
    else:
        global indexList
        tempList = indexList.copy()
        indexList = []
        for i in tempList:
            if employeeList[i][3] in range(int(varSalaryFrom), int(varSalaryTo)+1):
                indexList.append(i)


def PrintTable():
    global messageString
    elements = listView.get_children()
    if elements != '()':
        for child in elements:
            listView.delete(child)
    if messageString:
        tk.messagebox.showwarning("warning",messageString)
        return
    global indexList
    indexList = list(dict.fromkeys(indexList))

    index = iid = 0
    for row in indexList:
        listView.insert('', index, iid, values=employeeList[row])
        index = iid = index + 1

def InsightData():
    
    if messageString or indexList == []:
        insightString = ''
    else:
        totalRows = len(indexList)
        avgAge = 0
        avgSalary = 0

        for i in indexList:
            avgAge += employeeList[i][2]
            avgSalary += employeeList[i][3]

        insightString = ('Number of Employees : {}              Average Age of Emloyees: {}             Average Salary : {} '
        .format(totalRows,avgAge/totalRows,avgSalary/totalRows))

    insightLabel.configure(text=insightString)


def SearchClick():
    global varNamesEntry
    global varAgeFrom
    global varAgeTo
    global varSalaryFrom
    global varSalaryTo
    global indexList
    global messageString

    varNamesEntry = entryNames.get()
    varAgeFrom = entryAgeFrom.get()
    varAgeTo = entryAgeTo.get()
    varSalaryFrom = entrySalaryFrom.get()
    varSalaryTo = entrySalaryTo.get()

    indexList = []

    FilterNames()
    FilterAge()
    FilterSalary()
    InsightData()
    PrintTable()
    

# Frames and LabelFrames


mainFrame1 = tk.Frame(root)
mainFrame1.pack()

mainFrame2 = tk.LabelFrame(root, text='Search')
mainFrame2.pack(fill='x', padx=5, pady=5)

mainFrame3 = tk.LabelFrame(root, text='Employee List')
mainFrame3.pack(fill='both', expand=1, padx=5)

mainFrame4 = tk.LabelFrame(root, text='Insight')
mainFrame4.pack(fill='x', padx=5, pady=5)

# ------------ Search Sub Frames -------------

searchFrame1 = tk.LabelFrame(mainFrame2, text='By Name',)
searchFrame1.grid(row=0, column=0, rowspan=2, columnspan=2,  sticky='nsew',
                  padx=10, pady=10, ipadx=10, ipady=5)

searchFrame2 = tk.LabelFrame(mainFrame2, text='By Age')
searchFrame2.grid(row=0, column=2, rowspan=2, columnspan=2, sticky='nsew',
                  padx=20, pady=10, ipadx=10, ipady=10)

searchFrame3 = tk.LabelFrame(mainFrame2, text='By Salary')
searchFrame3.grid(row=0, column=4, rowspan=2, columnspan=2, sticky='nsew',
                  padx=10, pady=10, ipadx=10, ipady=10)

searchFrame4 = tk.Frame(mainFrame2)
searchFrame4.grid(row=0, column=6, rowspan=2, columnspan=2, sticky='nsew',
                  padx=20, pady=10, ipadx=10, ipady=10)

# -------------- Main Heading --------------

mainLabel = tk.Label(mainFrame1, text='Employee Records', pady=10, font=(24))
mainLabel.pack()


# ------------ Search by Name Widgets -------------

entryNames = tk.Entry(searchFrame1, width=28)
entryNames.pack(pady=10)

entryNamesNote = tk.Label(
    searchFrame1, text='Enter the names here. Use comma\nto seperate values', font=('calibri', 8, 'italic'))
entryNamesNote.pack()

# ----------- Search by Age Widgets --------------

labelAgeFrom = tk.Label(searchFrame2, text='From', )
labelAgeFrom.grid(row=0, column=0, padx=10, pady=10, sticky='w')

entryAgeFrom = tk.Entry(searchFrame2,  width=8)
entryAgeFrom.grid(row=0, column=1, pady=16)

labelAgeTo = tk.Label(searchFrame2, text='To', )
labelAgeTo.grid(row=1, column=0, padx=10)

entryAgeTo = tk.Entry(searchFrame2,  width=8)
entryAgeTo.grid(row=1, column=1)

# ----------- Search by Salary Widgets --------------

labelSalaryFrom = tk.Label(searchFrame3, text='From', )
labelSalaryFrom.grid(row=0, column=0, padx=10, pady=8, )

entrySalaryFrom = tk.Entry(searchFrame3,  width=18)
entrySalaryFrom.grid(row=0, column=1, pady=16)

labelSalaryTo = tk.Label(searchFrame3, text='To', )
labelSalaryTo.grid(row=1, column=0, padx=8)

entrySalaryTo = tk.Entry(searchFrame3,  width=18)
entrySalaryTo.grid(row=1, column=1)

# -------------- Search Buttons ---------------------

searchButton = ttk.Button(searchFrame4, text='SEARCH', command=SearchClick)
searchButton.pack(side=tk.BOTTOM, padx=25, pady=10)

resetButton = ttk.Button(searchFrame4, text='RESET', command=ResetClick)
resetButton.pack(side=tk.BOTTOM, padx=25)

# ------------------ List Frame ---------------------

listView = ttk.Treeview(mainFrame3)
listView.pack(padx=5, pady=5, fill=tk.BOTH, expand = 1)
listView["columns"] = ["First Name",
                       "Last Name", 'Age', 'Salary', 'Department']
listView["show"] = "headings"
listView.heading("First Name", text="First Name")
listView.heading("Last Name", text="Last Name")
listView.heading("Age", text="Age")
listView.heading("Salary", text="Salary")
listView.heading("Department", text="Department")

# ------------------ Insight Frame ---------------------

insightLabel = tk.Label(mainFrame4, text='')
insightLabel.pack(side=tk.LEFT, padx = 10, pady=10)



root.mainloop()