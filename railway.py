import os
bo_his={1:{"pnr number":"101","seat no":"-","Boarding point":"CBE","Destination piont":"CHE","booking status":"waiting"}}
userl={"user1":{"password":"u111","bookings":{}}}
stations=["CBE","TIR","ERO","SAL","CHE"]
seats=[[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
def tic_can_s(us_l,ca_p,se_nu):
    usc_bp=userl[us_l]["bookings"][ca_p]["Boarding point"]
    usc_dp=userl[us_l]["bookings"][ca_p]["Destination point"]
    for i in range(len(stations)):
        if stations[i]==usc_bp:
            start=i
        if stations[i]==usc_dp:
            end=i
    for j in range(start,end+1):
        seats[int(se_nu)][j]=0
def cancel_tic(us_l):
    d=0
    os.system('cls')
    print("\tBookings")
    print("--------")
    if len(userl[us_l]["bookings"])!=0:
        for i in range(len(userl[us_l]["bookings"])):
            if userl[us_l]["bookings"][i+1]["booking status"]!="cancelled":
                d=1
                print("booking -",i+1)
                for j in userl[us_l]["bookings"][i+1].keys():
                    print(j,end="-->")
                    print(userl[us_l]["bookings"][i+1][j])
                print("--------")
        if d!=0:
            try:
                us_pnc=int(input("Enter pnr number of ticket you want to cancel : "))
                c=0
                for i in range(len(userl[us_l]["bookings"])):
                    if str(us_pnc)==userl[us_l]["bookings"][i+1]["pnr number"]:
                        c=1
                        ca_p=i+1
                        se_nu=userl[us_l]["bookings"][i+1]["seat no"]
                if c==1:
                    if userl[us_l]["bookings"][i+1]["booking status"]!="waiting":
                        tic_can_s(us_l,ca_p,se_nu)
                    a_e=us_pnc%10
                    bo_his[a_e]["booking status"]="cancelled"
                    for i in range(len(userl[us_l]["bookings"])):
                        if userl[us_l]["bookings"][i+1]["pnr number"]==str(us_pnc):
                            userl[us_l]["bookings"][i+1]["booking status"]="cancelled"
                            print("Your ticket is succesfully cancelled")
                            input("Press Enter to continue")
                else:
                    print("pnr number is not in your bookings")
                    input("\tPress Enter to continue")
            except:
                print("Invalid Input")
                input("\tPress Enter to continue")
        else:
            print("No bookings for cancellation")
            input("\tPress Enter to continue") 
    else:
        print("No bookings")
        input("\tPress Enter to continue")
def view_bo(us_l):
    #os.system("cls")
    print("\tBookings")
    print("--------")
    if len(userl[us_l]["bookings"])!=0:
        for i in range(len(userl[us_l]["bookings"])):
            print("booking -",i+1)
            for j in userl[us_l]["bookings"][i+1].keys():
                print(j,end="-->")
                print(userl[us_l]["bookings"][i+1][j])
            print("--------")
        input("\tPress Enter to continue")
        #os.system("cls")
    else:
        print("No bookings")
        print("--------")
        input("\tPress Enter to continue")
    os.system("cls")
def book_wait(us_l,us_bp,us_dp):
    us_bop={"pnr number":str(101+len(bo_his)),"seat no":"-","Boarding point":us_bp,"Destination point":us_dp,"booking status":"waiting"}
    bo_his.update({len(bo_his)+1:us_bop})
    userl[us_l]["bookings"].update({len(userl[us_l]["bookings"])+1:us_bop})
    print("Your booking is succesfully added for waiting list")
def bookticket(us_l):
    os.system('cls')
    print("Borading pionts",*stations)
    us_bp=input("Enter boarding station : ")
    if us_bp in stations:
        us_dp=input("Enter destination station : ")
        if (us_dp in stations) and (us_dp!=us_bp):
            boo=0
            for i in range(5):
                if stations[i]==us_bp:
                    start=i
                elif stations[i]==us_dp:
                    end=i
            count1=abs(start-end)+1
            for i in range(5):
                c=0
                for j in range(start,end+1):
                    if seats[i][j]==0:
                        c+=1
                if count1==c:
                    for j in range(start,end+1):
                        seats[i][j]=1
                    us_bop={"pnr number":str(101+len(bo_his)),"seat no":str(i),"Boarding point":us_bp,"Destination point":us_dp,"booking status":"booked"}
                    #a_l=len(bo_his)
                    #bo_his.update({len(bo_his)})
                    bo_his.update({len(bo_his)+1:us_bop})
                    userl[us_l]["bookings"].update({len(userl[us_l]["bookings"])+1:us_bop})
                    #print("seat",i,"booked succesfully")
                    boo=1
                    break
            if boo==1:
                #print(bo_his)
                print("seat",i,"booked succesfully")
                input("Press Enter to continue")
            else:
                print("All seats are filled")
                print("Enter 1 to book waiting list\nEnter 0 to go back")
                bo_us=input()
                if bo_us=="1":
                    book_wait(us_l,us_bp,us_dp)
                elif bo_us=="0":
                    pass
                else:
                    print("Invalid Input")
                    input("\tPress Enter to continue")
        else:
            print("Invalid destination piont")
            input("\tPress Enter to continue")
    else:
        print("Invalid boarding piont")
        input("\tPress Enter to continue")
def existuser():
    os.system("cls")
    print("\tExisting User Login")
    us_l=input("Enter your username : ")
    us_p=input("Enter your password : ")
    if us_l in userl:
        if us_p==userl[us_l]["password"]:
            print("\t",us_l,"Login successful")
            while True:
                print("1.Book ticket\n2.cancel ticket\n3.view booking\n4.Exit")
                us_dc=input("Enter your choice : ")
                if us_dc=="1":
                    bookticket(us_l)
                elif us_dc=="2":
                    cancel_tic(us_l)
                elif us_dc=="3":
                    os.system("cls")
                    view_bo(us_l)
                elif us_dc=="4":
                    break
                else:
                    print("Invalid Input")
                    input("\tPress enter to continue")
        else:
            print("Wrong password")
            input("\tPress Enter to continue")
    else:
        print("Invalid login credentils")
        input("\tPress Enter to continue")
def newuser():
    os.system("cls")
    print("New user signup")
    us_nl=input("Enter username : ")
    if us_nl not in userl:
        us_np=input("Enter password : ")
        us_fl={us_nl:{"password":us_np,"bookings":{}}}
        userl.update(us_fl)
        print("Account created succesfully")
        input("\tPress Enter to continue")
    else:
        print("User alredy exist\ntry differrent username")
        input("\tPress Enter to continue")
def book_hy():
    os.system("cls")
    print("\tBookings")
    print("--------")
    c=0
    for i in range(len(bo_his)):
        if bo_his[i+1]["booking status"]!="waiting":
            print("booking -",i+1)
            for j in bo_his[i+1].keys():
                print(j,end="-->")
                print(bo_his[i+1][j])
            c=1
            print("--------")
    if c==0:
        print("No bookings")
        print("--------")
    input("\tPress Enter to continue")
    os.system('cls')
def wait_ly():
    os.system("cls")
    print("\tBookings for waiting list")
    print("--------")
    c=0
    for i in range(len(bo_his)):
        if bo_his[i+1]["booking status"]=="waiting":
            print("booking -",i+1)
            for j in bo_his[i+1].keys():
                print(j,end="-->")
                print(bo_his[i+1][j])
            c=1
            print("--------")
    if c==0:
        print("No bookings in waiting list")
        print("--------")
    print("--------")    
    input("\tPress Enter to continue")
    os.system('cls')
def admin():
    os.system("cls")
    print("\tAdmin login")
    ad_in=input("Enter your username : ")
    ad_p=input("Enter your password : ")
    if ad_in=="admin1" and ad_p=="a111":
        print("\t",ad_in,"Login successful")
        while True:
            print("1.view booking history\n2.waiting list\n3.exit")
            ad_ch=input("Enter your choice : ")
            if ad_ch=="1":
                book_hy()
            elif ad_ch=="2":
                wait_ly()
            elif ad_ch=="3":
                break
            else:
                print("Invalid Input")
                input("\tPress enter to continue")
    else:
        print("Invalid login credentials")
        input("\tPress enter to continue")
def user():
    os.system("cls")
    print("\tUser login")
    while True:
        print("1.Existing User\n2.New User\n3.Exit")
        us_ch=input("Enter your choice : ")
        if us_ch=="1":
            existuser()
        elif us_ch=="2":
            newuser()
        elif us_ch=="3":
            break
        else:
            print("Invalid Input")
            input("\tPress Enter to continue")
while True:
    os.system("cls")
    print("\tWELCOME TO MYRAILS\n1.Admin\n2.user\n3.exit")
    a=input("enter choice : ")
    if a=="1":
        admin()
    elif a=="2":
        user()
    elif a=="3":
        break
    else:
        print("Invalid Input")
        input("\tPress Enter to continue")
