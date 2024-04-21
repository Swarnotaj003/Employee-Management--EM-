# EMPLOYEE MANAGEMENT PROJECT
# Reference: TABLE 'empl' in DATABASE 'company'
import mysql.connector as mc

def DBconnect():
    try:
        mydb = mc.connect(host="localhost",user="root",password="taj325",database="company")
        mycur = mydb.cursor()
        return mydb,mycur
    except:
        return False
    
def Login():
    # For log-in screen
    userid = input("Enter your user ID:")
    password = input("Enter your password:")
    flag = False
    sql = "SELECT * FROM login"
    mycur.execute(sql)
    data = mycur.fetchall()
    for i in data:
        if userid==i[0] and password==i[1]:
            flag = True
            break
    return flag

def display():
    # To display the whole table
    global mydb
    global mycur
    sql = "SELECT * FROM empl"
    mycur.execute(sql)
    results = mycur.fetchall()
    print("*"*100)
    print('%-10s'%"EMP NO",'%-20s'%'EMP NAME','%-20s'%'JOB','%-18s'%"HIRE DATE",'%-15s'%"BASE SALARY",'%-15s'%"COMM")
    print("*"*100)
    count = 0
    for row in results:
        print('%-10s'%row[0],'%-20s'%row[1],'%-20s'%row[2],'%-18s'%row[3],'%-15s'%row[4],'%-10s'%row[5])
        count += 1
    print("-"*100)
    print("Number of records:",count)

def staff():
    # To display staff details by job/post
    global mydb
    global mycur
    sql = "SELECT job,COUNT(job),MIN(sal),MAX(sal) FROM empl GROUP BY job"
    mycur.execute(sql)
    results = mycur.fetchall()
    print("*"*68)
    print('%-15s'%'JOB','%-18s'%"NO. OF EMPLOYEES",'%15s'%"MIN SALARY",'%15s'%"MAX SALARY")
    print("*"*68)
    count = 0
    for row in results:
        print('%-20s'%row[0],'%-18s'%row[1],'%-15s'%row[2],'%-15s'%row[3])
        count += 1
    print("-"*68)
    sql = "SELECT COUNT(*) FROM empl"
    mycur.execute(sql)
    result = mycur.fetchone()
    print("No. of posts:",count)
    print("Staff employed:",result[0])
    
def add_emp():
    # To add a new employee
    global mydb
    global mycur
    try:
        empno = int(input("Enter employee number (Max. 4 digits):"))
        ename = input("Enter employee name (Max. 30 characters):")
        job = input("Enter the job (Max. 30 characters):")
        hdate = input("Enter hire date (yyyy-mm-dd):")
        sal = int(input("Enter the base salary (Max. 8 digits):"))
        record = (empno, ename, job, hdate, sal, "NULL")
        sql = "INSERT INTO empl VALUES(%d, '%s','%s','%s', %d, %s)"%record
        mycur.execute(sql)
        mydb.commit()
        print("## Employee ADDED successfully! ##")
    except:
        print("ERROR! Something went wrong")
    
def search_emp():
    # To search for an employee
    global mydb
    global mycur
    dct = {1:"empno",2:"ename",3:"job"}
    print("Available SEARCH FIELDS:",dct)
    choice = int(input("Enter the search field(1-3):"))
    if choice==1:
        num = int(input("Enter the employee no. to search:"))
        val = str(num)
    elif choice==2:
        val = input("Enter the employee name to search:")
    elif choice==3:
        val = input("Enter the job to search:")
    else:
        print("Please enter a valid choice")
    if choice in range(1,4):
        field = dct[choice]
        sql = "SELECT * FROM empl WHERE %s ='%s'" %(field,val)
        mycur.execute(sql)
        results = mycur.fetchall()
        if mycur.rowcount<=0:
            print("Sorry! No matching details found")
        else:
            print("*"*100)
            print('%-10s'%"EMP NO",'%-20s'%'EMP NAME','%-20s'%'JOB','%-18s'%"HIRE DATE",'%-15s'%"BASE SALARY",'%-15s'%"COMM")
            print("*"*100)
            for row in results:
                print('%-10s'%row[0],'%-20s'%row[1],'%-20s'%row[2],'%-18s'%row[3],'%-15s'%row[4],'%-10s'%row[5])
            print("-"*100)
        
def PD_emp():
    # To update job & salary of an existing employee
    global mydb
    global mycur
    empno = int(input("Enter the employee no. to Promote/Demote:"))
    sql = "SELECT * FROM empl WHERE empno="+ str(empno)
    mycur.execute(sql)
    results = mycur.fetchall()
    if mycur.rowcount<=0:
        print("Sorry! No matching details found")
    else:
        print("*"*100)
        print('%-10s'%"EMP NO",'%-20s'%'EMP NAME','%-20s'%'JOB','%-18s'%"HIRE DATE",'%-15s'%"BASE SALARY",'%-15s'%"COMM")
        print("*"*100)
        for row in results:
            print('%-10s'%row[0],'%-20s'%row[1],'%-20s'%row[2],'%-18s'%row[3],'%-15s'%row[4],'%-10s'%row[5])
        print("-"*100)
        ch = input("Are you sure to Promote/Demote? (y/n)")
        if ch.lower()=='y':
            try:
                job = input("Enter the new job:")
                sal = int(input("Enter the updated salary:"))
                sql = "UPDATE empl SET job='%s',sal=%d WHERE empno=%d" %(job,sal,empno)
                mycur.execute(sql)
                mydb.commit()
                print("## Employee's Post UPDATED! ##")
            except:
                print("ERROR! Something went wrong")
        else:
            print("Okay! Process aborted")

def grantComm():
    # To grant commission to an existing employee
    global mydb
    global mycur
    empno = int(input("Enter the employee no. to grant Commission:"))
    sql = "SELECT * FROM empl WHERE empno="+ str(empno)
    mycur.execute(sql)
    results = mycur.fetchall()
    if mycur.rowcount<=0:
        print("Sorry! No matching details found")
    else:
        print("*"*100)
        print('%-10s'%"EMP NO",'%-20s'%'EMP NAME','%-20s'%'JOB','%-18s'%"HIRE DATE",'%-15s'%"BASE SALARY",'%-15s'%"COMM")
        print("*"*100)
        for row in results:
            print('%-10s'%row[0],'%-20s'%row[1],'%-20s'%row[2],'%-18s'%row[3],'%-15s'%row[4],'%-10s'%row[5])
        print("-"*100)
        ch = input("Are you sure to grant Commission? (y/n)")
        if ch.lower()=='y':
            try:
                pct = float(input("Enter the percentage of salary for granting commission:"))
                comm = float(row[4])*pct/100
                sql = "UPDATE empl SET comm=%d WHERE empno=%d" %(comm,empno)
                mycur.execute(sql)
                mydb.commit()
                print("## Commission GRANTED! ##")
            except:
                print("ERROR! Something went wrong")
        else:
            print("Okay! Process aborted")
            
def del_emp():
    # To remove an existing employee
    global mydb
    global mycur
    empno = int(input("Enter the employee no. to delete:"))
    sql = "SELECT * FROM empl WHERE empno="+ str(empno)
    mycur.execute(sql)
    results = mycur.fetchall()
    if mycur.rowcount<=0:
        print("Sorry! No matching details found")
    else:
        print("*"*100)
        print('%-10s'%"EMP NO",'%-20s'%'EMP NAME','%-20s'%'JOB','%-18s'%"HIRE DATE",'%-15s'%"BASE SALARY",'%-15s'%"COMM")
        print("*"*100)
        for row in results:
            print('%-10s'%row[0],'%-20s'%row[1],'%-20s'%row[2],'%-18s'%row[3],'%-15s'%row[4],'%-10s'%row[5])
        print("-"*100)
        ch = input("Are you sure to delete details? (y/n)")
        if ch.lower()=='y':
            sql = "DELETE FROM empl WHERE empno="+ str(empno)
            mycur.execute(sql)
            mydb.commit()
            print("## Employee REMOVED! ##")
        else:
            print("Okay! Process aborted")

def payscale():
    # To print the pay slip
    global mydb
    global mycur
    empno = int(input("Enter the employee no. to print pay slip:"))
    sql = "SELECT * FROM empl WHERE empno="+ str(empno)
    mycur.execute(sql)
    results = mycur.fetchone()
    if mycur.rowcount<=0:
        print("Sorry! No matching details found")
    else:
        print("\n"*5)
        print("="*60)
        print("TECHNOSTAR Pvt. Ltd.".center(60))
        print()
        print("EMPNO :",results[0]," "*20,"NAME :",results[1])
        print("DEPARTMENT :",results[2])
        print("*"*60)
        s = int(results[4]) #Base Salary
        hra = s * 12/100 #House Rent Allowance
        da = s * 15/100 #Dearness Allowance
        it = s * 20/100  #Income Tax
        nps = (s+hra)*10/100 #National Pension System
        gross = s+hra+da+nps
        ded = it + nps
        net = gross - ded
        tded=it + nps
        print(" "*10,"EARNING"," "*16,"DEDUCTION")
        print("-"*60)
        print(" "*10,"Basic  :"+str(s)," "*10,"INC. TAX :"+str(it))
        print(" "*10,"HRA    :"+str(hra)," "*9,"NPS      :"+str(nps))
        print(" "*10,"DA     :"+str(da))
        print(" "*10,"NPS    :"+str(nps))
        print("-"*60)
        print(" "*10,"GROSS  :"+str(gross)," "*8,"TOTAL DED :",tded)
        print("-"*60)
        print(" "*10,"NET SALARY :",net)
        print("="*60)
        
def contact():
    # To print the contact details
    print("\n"*5)
    print("*"*100)
    print("TECHNOSTAR Pvt. Ltd.".center(100))
    print("="*100)
    print("CONTACT US".center(100))
    print("-"*100)
    print("While we're good with smoke signals,".center(100))
    print("there are simpler ways for us to get in touch with you.".center(100))
    print()
    print("-------".center(33),"-----".center(33),"-----".center(33))
    print("ADDRESS".center(33),"PHONE".center(33),"EMAIL".center(33))
    print("-------".center(33),"-----".center(33),"-----".center(33))
    print("CONTRACTING".center(33),"CONTRACTING".center(33),"REQUEST FOR PROPOSAL".center(33))
    print("DA-14, Salt Lake City,".center(33),"6247239542 phone".center(33),"request@technostar.com".center(33))
    print("Sector-I, Kolkata-700064".center(33),"797-892-4424 facsimile".center(33))
    print()
    print("INDUSTRIAL DIVISION OFFICE".center(33),"INDUSTRIAL DIVISION OFFICE".center(33),"BID OPPORTUNITIES".center(33))
    print("Automation Drive,KNC Rd, Katgola,".center(33),"9752056857 phone".center(33),"estimating@technostar.com".center(33))
    print("Barasat, Kolkata-700124".center(33),"217-804-8423 facsimile".center(33))
    print()
    print("OTHER OFFICES(1)".center(33),"24/7 SERVICE DEPARTMENT".center(33),"SERVICE CALLS".center(33))
    print("GN-29 Sector-V, Salt Lake,".center(33),"561-392-3422".center(33),"service@technostar.com".center(33))
    print("Street Number 2, Kolkata-700091".center(33),"(Press 2 for emergency calls)".center(33))
    print()
    print("OTHER OFFICES(2)".center(33),"OTHER OFFICES".center(33),"EMPLOYMENT OPPORTUNITIES".center(33))
    print("15, Park Street, Taltala,".center(33),"9449518539 phone(1)".center(33),"careers@technostar.com".center(33))
    print("Kolkata-700016".center(33),"9753372907 phone(2)".center(33))
    print()
    print("="*100)
    print("STILL CAN'T FIND WHAT YOU'RE LOOKING FOR?".center(100))
    print("-"*100)
    print("EMAIL OUR TEAM : swarnotaj003@outlook.com    ".center(100))
    print("               : srivastavatarang@hotmail.com".center(100))
    print("               : basantroy42@hotmail.com     ".center(100))
    print()
    print("="*100)
    print("ADDITIONAL BRANCHES".center(100))
    print("-"*100)
    print("(INDIA)  :    Mumbai          Delhi        Hyderabad      Bengaluru".center(100))
    print("(FOREIGN):    Los Angeles     Bangkok      Brisbane       Birmingham".center(100))
    print("*"*100)
    
#_Main_
if DBconnect():
    mydb,mycur = DBconnect()
    print("## EMPLOYEE MANAGEMENT PROGRAM ##")
    print()
    print("="*35)
    print("LOGIN".center(35))
    print("-"*35)
    if Login():
        print("-"*35)
        print("\nSuccessfully logged in!")
        print()
        while True:
            print()
            print("="*35)
            print("MENU".center(35))
            print("-"*35)
            print("| 1 | SHOW EMPLOYEE LIST")
            print("| 2 | SHOW STAFF DETAILS(BY POST)")
            print("| 3 | ADD A NEW EMPLOYEE")
            print("| 4 | SEARCH EMPLOYEE ")
            print("| 5 | PROMOTE/DEMOTE EMPLOYEE")
            print("| 6 | GRANT COMMISSION")
            print("| 7 | REMOVE AN EMPLOYEE")
            print("| 8 | DISPLAY PAY SCALE")
            print("| 9 | CONTACT US")
            print("| 0 | EXIT")
            print("="*35)
            ch = int(input("Enter your choice (0-9):"))
            print()
            if ch==1:
                display()
                input("\nPress enter to continue...")
            elif ch==2:
                staff()
                input("\nPress enter to continue...")
            elif ch==3:
                add_emp()
                input("\nPress enter to continue...")
            elif ch==4:
                search_emp()
                input("\nPress enter to continue...")
            elif ch==5:
                PD_emp()
                input("\nPress enter to continue...")
            elif ch==6:
                grantComm()
                input("\nPress enter to continue...")
            elif ch==7:
                del_emp()
                input("\nPress enter to continue...")
            elif ch==8:
                payscale()
                input("\nPress enter to continue...")
            elif ch==9:
                contact()
                input("\nPress enter to continue...")
            elif ch==0:
                print("\n## Program ended! ##")
                break
            else:
                print("Invalid choice, enter again")
                input("\nPress enter to continue...")
    else:
        print("-"*35)
        print("\n## Invalid userID or password! ##")
    mydb.close()
else:
    print("## The connection was unsuccessful! ##")