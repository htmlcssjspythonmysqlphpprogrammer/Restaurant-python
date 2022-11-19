from tkinter import *
import time
import datetime
import tkinter.ttk as ttk
from tkinter import messagebox
import sqlite3
import random

global framemenuimage
global imagecorner
global BlIdentity
global BlName
global GenderBl
global BlAge
global BlDisease
global BlPhone
global BlAddress
global BlDoctorname
global BlDoctorcharges
global BlLabtest
global TreatmentchargesBl
global BlProcedurecharges
global BlOthercharges
global BlMiscellaneouscharges
global BlRoomcharges
global BlTotal
global framereceiptimage
global frameprintbill
global imagemenu
global receiptimage
global receiptimager
global imagehome
global framehome
global framepatientregistration
global framepatientadmit
global framerinfo
global frameainfo
global framestaffregistration
global framestaffinformation
global framemenuroot
global framerrecord
global framedoctorrecord
global framebill
global framereceipt
global PrPatientid
global PrName
global GenderPr
global PrAge
global PrPhone
global PrAddress
global PrDisease
global PrCheckIn
global PrBloodgroup
global PrDoctorname
global PrRoomNo
global RiPatientid
global RiName
global GenderRi
global RiAge
global RiPhone
global RiAddress
global RiDisease
global RiCheckIn
global RiBloodgroup
global RiDoctorname
global RiRoomNo
global PaPatientid
global PaName
global GenderPa
global PaAge
global PaPhone
global PaAddress
global PaDisease
global PaCheckIn
global PaBloodgroup
global PaDoctorname
global PaCheckOut
global PaRoomNo
global PaRoomtype
global PaPrice
global AiPatientid
global AiName
global GenderAi
global AiAge
global AiPhone
global AiAddress
global AiDisease
global AiCheckIn
global AiBloodgroup
global AiDoctorname
global AiCheckOut
global AiRoomNo
global AiRoomtype
global AiPrice
global SrID
global SrName
global GenderSr
global SrPosition
global SrDepartment
global SrMailid
global SrSalary
global SrPhone
global SrAddress
global SiID
global SiName
global GenderSi
global SiPosition
global SiDepartment
global SiMailid
global SiSalary
global SiPhone
global SiAddress
global Patient_table
global Patient_tables

global counterlogin
global counterhome
global counterpreg
global counterrinfo
global counterpadmit
global counterainfo
global countersreg
global countersinfo
global counterrrecord
global counterdrecord
global counterbill
global counterreceipt
global counterprintbill

counterhome=0
counterlogin=0
counterpreg=0
counterrinfo=0
counterpadmit=0
counterainfo=0
countersreg=0
countersinfo=0
counterrrecord=0
counterdrecord=0
counterbill=0
counterreceipt=0
counterprintbill=0

root= Tk()
root.title("login page")
root.geometry("1000x1000")

PrCheckIn = StringVar()
PrCheckIn.set(time.strftime("%d/%m/%y"))


def login():
    global framemenuimage
    global framereceiptimage
    global framehome
    global imagemenu
    global imagehome
    global framepatientregistration
    global framepatientadmit
    global framerinfo
    global frameainfo
    global framemenuroot
    global framestaffregistration
    global framestaffinformation
    global framerrecord
    global framedoctorrecord
    global framebill
    global framereceipt
    global PrPatientid
    global PrName
    global GenderPr
    global PrAge
    global PrPhone
    global PrAddress
    global PrDisease
    global PrCheckIn
    global PrBloodgroup
    global PrDoctorname
    global PrRoomNo
    global RiPatientid
    global RiName
    global GenderRi
    global RiAge
    global RiPhone
    global RiAddress
    global RiDisease
    global RiCheckIn
    global RiBloodgroup
    global RiDoctorname
    global RiRoomNo
    global PaPatientid
    global PaName
    global GenderPa
    global PaAge
    global PaPhone
    global PaAddress
    global PaDisease
    global PaCheckIn
    global PaBloodgroup
    global PaDoctorname
    global PaCheckOut
    global PaRoomNo
    global PaRoomtype
    global PaPrice
    global AiPatientid
    global AiName
    global GenderAi
    global AiAge
    global AiPhone
    global AiAddress
    global AiDisease
    global AiCheckIn
    global AiBloodgroup
    global AiDoctorname
    global AiCheckOut
    global AiRoomNo
    global AiRoomtype
    global AiPrice
    global SrID
    global SrName
    global GenderSr
    global SrPosition
    global SrDepartment
    global SrMailid
    global SrSalary
    global SrPhone
    global SrAddress

    global counterlogin
    global counterhome
    global counterpreg
    global counterrinfo
    global counterpadmit
    global counterainfo
    global countersreg
    global countersinfo
    global counterrrecord
    global counterdrecord
    global counterbill
    global counterreceipt
    global counterprintbill

    counterlogin+=1
    counterhome=0
    counterpreg=0
    counterrinfo=0
    counterpadmit=0
    counterainfo=0
    countersreg=0
    countersinfo=0
    counterrrecord=0
    counterdrecord=0
    counterbill=0
    counterdrecord=0
    counterreceipt=0
    counterprintbill=0

    if usernameVar.get()=="HOSPITAL" and passwordVar.get()=="yash":
        try:
            frame1.destroy()
        except:
            pass
        try:
            framereceiptimage.destroy()
        except:
            pass
        try:
            frameprintbill.destroy()
        except:
            pass
        try:
            framehome.destroy()
        except:
            pass
        try:
            framemenuroot.destroy()
        except:
            pass
        try:
            framerinfo.destroy()
        except:
            pass
        try:
            framepatientregistration.destroy()
        except:
            pass
        try:
            frameainfo.destroy()
        except:
            pass
        try:
            framestaffregistration.destroy()
        except:
            pass
        try:
            framestaffinformation.destroy()
        except:
            pass
        try:
            framerrecord.destroy()
        except:
            pass
        try:
        	framedoctorrecord.destroy()
        except:
        	pass
        try:
            framebill.destroy()
        except:
            pass
        try:
            framereceipt.destroy()
        except:
            pass
    if counterlogin==1:
        def Bill():
            global framemenuimage
            global framereceiptimage
            global frameprintbill
            global framehome
            global BlIdentity
            global BlName
            global GenderBl
            global BlAge
            global BlDisease
            global BlPhone
            global BlAddress
            global BlDoctorname
            global BlDoctorcharges
            global BlLabtest
            global TreatmentchargesBl
            global BlProcedurecharges
            global BlOthercharges
            global BlMiscellaneouscharges
            global BlRoomcharges
            global BlTotal
            global imagemenu
            global imagehome
            global framereceipt
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framestaffregistration
            global framestaffinformation
            global framebill
            global framerrecord
            global framedoctorrecord

            global counterpreg
            global counterhome
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterrrecord
            global counterdrecord
            global counterbill
            global counterreceipt
            global counterprintbill


            counterbill+=1
            counterhome=0
            counterpreg=0
            counterrinfo=0
            counterainfo=0
            countersreg=0
            countersinfo=0
            counterpadmit=0
            counterrrecord=0
            counterdrecord=0
            counterreceipt=0
            counterprintbill=0


            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass    
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
            	framedoctorrecord.destroy()
            except:
            	pass
            if counterbill==1:
                framebill=Frame(root,relief="solid",borderwidth=2,bg="lightgreen")
                framebill.pack(side="right",fill=BOTH,expand=True)

                framexbill=Frame(framebill,bg="sandybrown",relief="solid",borderwidth=2)
                framexbill.pack(side=TOP,fill=X)

                labelbill=Label(framexbill,text="Billing",bg="sandybrown",fg="black",font=("calibri",20,"bold"))
                labelbill.pack()

                frametbill=Frame(framebill,height="200",bg="lightgreen")
                frametbill.pack(side=TOP,fill=X)

                framebleft=Frame(frametbill,height="200",width="685",bg="lightgreen")
                framebleft.pack(side=LEFT)

                labelPatient_id=Label(framebleft,text="Identity:",bg="lightgreen",font=("calibri",17,"bold"))
                labelPatient_id.grid(row=0,column=0,sticky="w",padx="50",pady=2)

                BlIdentity=StringVar()
                Identity=Entry(framebleft,textvariable=BlIdentity,font=("calibri",17,"bold"))
                Identity.grid(row=0,column=1)

                labelName=Label(framebleft,text="Name:",bg="lightgreen",font=("calibri",17,"bold"))
                labelName.grid(row=1,column=0,sticky="w",padx="50")

                BlName=StringVar()
                Name=Entry(framebleft,textvariable=BlName,font=("calibri",17,"bold"))
                Name.grid(row=1,column=1)

                GenderBl=StringVar()
                GenderBl.set("")

                labelGender=Label(framebleft,text="Gender:",bg="lightgreen",font=("calibri",17,"bold"))
                labelGender.grid(row=2,column=0)
                                
                i= IntVar()
                r1 = Radiobutton(framebleft,text="male",value='Male',variable=GenderBl,bg="lightgreen",font=("calibri",17,"bold"))
                r2 = Radiobutton(framebleft,text="female",value='Female',variable=GenderBl,bg="lightgreen",font=("calibri",17,"bold"))
                r1.grid(row=2,column=1,sticky="w")
                r2.grid(row=2,column=1,sticky="e",padx=0)

                labelAge=Label(framebleft,text="Age:",bg="lightgreen",font=("calibri",17,"bold"))
                labelAge.grid(row=3,column=0,sticky="w",padx="50")

                BlAge=StringVar()
                Age=Entry(framebleft,textvariable=BlAge,font=("calibri",17,"bold"))
                Age.grid(row=3,column=1)

                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)

                framebright=Frame(frametbill,height="200",bg="lightgreen",width="685")
                framebright.pack(side=RIGHT)

                labelAge=Label(framebright,text="Disease:",bg="lightgreen",font=("calibri",17,"bold"))
                labelAge.grid(row=0,column=0,sticky="w")

                BlDisease=StringVar()
                Disease=Entry(framebright,textvariable=BlDisease,font=("calibri",17,"bold"))
                Disease.grid(row=0,column=1,padx="50")

                labelPhone=Label(framebright,text="Phone:",bg="lightgreen",font=("calibri",17,"bold"))
                labelPhone.grid(row=1,column=0,sticky="w")

                BlPhone=StringVar()
                Phone=Entry(framebright,textvariable=BlPhone,font=("calibri",17,"bold"))
                Phone.grid(row=1,column=1,padx="50")

                labelAddress=Label(framebright,text="Address:",bg="lightgreen",font=("calibri",17,"bold"))
                labelAddress.grid(row=2,column=0,sticky="w")

                BlAddress=StringVar()
                Address=Entry(framebright,textvariable=BlAddress,font=("calibri",17,"bold"))
                Address.grid(row=2,column=1,padx="50")

                labelDisease=Label(framebright,text="Doctor Name:",bg="lightgreen",font=("calibri",17,"bold"))
                labelDisease.grid(row=3,column=0,sticky="w")

                BlDoctorname=StringVar()
                Doctorname=Entry(framebright,textvariable=BlDoctorname,font=("calibri",17,"bold"))
                Doctorname.grid(row=3,column=1,padx="50")

                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)

                framebottom=Frame(framebill,relief="solid",bg="lightgreen",borderwidth=2)
                framebottom.pack(side=TOP,fill=X,pady=16)

                labelPatient_id=Label(framebottom,text="Sr. No :",bg="lightgreen",fg="Purple",font=("calibri",20,"bold"))
                labelPatient_id.grid(row=0,column=0,sticky="w",padx=100)
                labelPatient_id=Label(framebottom,text="Particulars :",bg="lightgreen",fg="Purple",font=("calibri",20,"bold"))
                labelPatient_id.grid(row=0,column=1,sticky="w",padx=70)
                labelPatient_id=Label(framebottom,text="Amount :",bg="lightgreen",fg="Purple",font=("calibri",20,"bold"))
                labelPatient_id.grid(row=0,column=2,sticky="e",padx=130)

                root.grid_rowconfigure(0,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)
                root.grid_columnconfigure(2,weight=1)

                framebo=Frame(framebill,bg="lightgreen")
                framebo.pack(side=TOP,fill=BOTH,expand=True,pady="10")

                labelPatient_id=Label(framebo,text="01 :",bg="lightgreen",font=("calibri",17,"bold"))
                labelPatient_id.grid(row=0,column=0,sticky="w",padx=105)
                labelPatient_id=Label(framebo,text="Doctor Charges:",bg="lightgreen",font=("calibri",17,"bold"))
                labelPatient_id.grid(row=0,column=1,sticky="w",padx=105)

                BlDoctorcharges=StringVar()
                Doctorcharges=Entry(framebo,textvariable=BlDoctorcharges,font=("calibri",17,"bold"))
                Doctorcharges.grid(row=0,column=2,sticky="w")

                labelName=Label(framebo,text="02 :",bg="lightgreen",font=("calibri",17,"bold"))
                labelName.grid(row=1,column=0,sticky="w",padx=105)
                labelName=Label(framebo,text="Lab Test:",bg="lightgreen",font=("calibri",17,"bold"))
                labelName.grid(row=1,column=1,sticky="w",padx=105)

                BlLabtest=StringVar()
                Labtest=Entry(framebo,textvariable=BlLabtest,font=("calibri",17,"bold"))
                Labtest.grid(row=1,column=2,sticky="w")

                labelGender=Label(framebo,text="03 :",bg="lightgreen",font=("calibri",17,"bold"))
                labelGender.grid(row=2,column=0,sticky="w",padx=105)
                labelGender=Label(framebo,text="Treatment Charges:",bg="lightgreen",font=("calibri",17,"bold"))
                labelGender.grid(row=2,column=1,sticky="w",padx=105)

                TreatmentchargesBl=StringVar()
                Treatmentcharges=Entry(framebo,textvariable=TreatmentchargesBl,font=("calibri",17,"bold"))
                Treatmentcharges.grid(row=2,column=2,sticky="w")

                labelAge=Label(framebo,text="04 :",bg="lightgreen",font=("calibri",17,"bold"))
                labelAge.grid(row=3,column=0,sticky="w",padx=105)
                labelAge=Label(framebo,text="Procedure Charges:",bg="lightgreen",font=("calibri",17,"bold"))
                labelAge.grid(row=3,column=1,sticky="w",padx=105)

                BlProcedurecharges=StringVar()
                Procedurecharges=Entry(framebo,textvariable=BlProcedurecharges,font=("calibri",17,"bold"))
                Procedurecharges.grid(row=3,column=2,sticky="w")

                labelPhone=Label(framebo,text="05 :",bg="lightgreen",font=("calibri",17,"bold"))
                labelPhone.grid(row=4,column=0,sticky="w",padx=105)
                labelPhone=Label(framebo,text="Other Charges:",bg="lightgreen",font=("calibri",17,"bold"))
                labelPhone.grid(row=4,column=1,sticky="w",padx=105)

                BlOthercharges=StringVar()
                Othercharges=Entry(framebo,font=("calibri",17,"bold"))
                Othercharges.grid(row=4,column=2,sticky="w")

                labelAddress=Label(framebo,text="06 :",bg="lightgreen",font=("calibri",17,"bold"))
                labelAddress.grid(row=5,column=0,sticky="w",padx=105)
                labelAddress=Label(framebo,text="Miscellaneous Charges:",bg="lightgreen",font=("calibri",17,"bold"))
                labelAddress.grid(row=5,column=1,sticky="w",padx=105)

                BlMiscellaneouscharges=StringVar()
                Miscellaneouscharges=Entry(framebo,textvariable=BlMiscellaneouscharges,font=("calibri",17,"bold"))
                Miscellaneouscharges.grid(row=5,column=2,sticky="w")

                labelAddress=Label(framebo,text="07 :",bg="lightgreen",font=("calibri",17,"bold"))
                labelAddress.grid(row=6,column=0,sticky="w",padx=105)
                labelAddress=Label(framebo,text="Room Charges:",bg="lightgreen",font=("calibri",17,"bold"))
                labelAddress.grid(row=6,column=1,sticky="w",padx=105)

                BlRoomcharges=StringVar()
                Roomcharges=Entry(framebo,textvariable=BlRoomcharges,font=("calibri",17,"bold"))
                Roomcharges.grid(row=6,column=2,sticky="w")

                labelDisease=Label(framebo,text="",bg="lightgreen",font=("calibri",17,"bold"))
                labelDisease.grid(row=7,column=0,sticky="w",padx=105)
                labelDisease=Label(framebo,text="Total:",bg="lightgreen",font=("calibri",17,"bold"))
                labelDisease.grid(row=7,column=1,sticky="w",padx=105)

                BlTotal=StringVar()
                Total=Entry(framebo,textvariable=BlTotal,font=("calibri",17,"bold"))
                Total.grid(row=7,column=2,sticky="w")

                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_rowconfigure(4,weight=1)
                root.grid_rowconfigure(5,weight=1)
                root.grid_rowconfigure(6,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)
                root.grid_columnconfigure(2,weight=1)

                frameprint=Frame(framebill,bg="lightgreen")
                frameprint.pack(side=RIGHT)

                buttonPrint=Button(frameprint,text="Print",bg="yellow",command=printbill,bd=7,width=10,font=("calibri",15,"bold"))
                buttonPrint.pack(side=RIGHT,padx="50",pady="20");

        def fetch_datas():
            connection=sqlite3.connect("YASH.db")
            cursor=connection.cursor()

            query="select * from sr"
            cursor.execute(query)

            rows=cursor.fetchall()
            if len(rows)!=0:
                Patient_tables.delete(*Patient_tables.get_children())
                for row in rows:
                    Patient_tables.insert('',END,values=row)

                    connection.commit()
            connection.close()

        def drecord():
            global framemenuimage
            global framehome
            global frameprintbill
            global framereceiptimage
            global imagemenu
            global imagehome
            global framereceipt
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framestaffregistration
            global framestaffinformation
            global framebill
            global framerrecord
            global framedoctorrecord
            global Patient_tables

            global counterpreg
            global counterhome
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterrrecord
            global counterdrecord
            global counterbill
            global counterprintbill

            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass    
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass

            counterdrecord+=1
            counterhome=0
            counterpreg=0
            counterrinfo=0
            counterainfo=0
            countersreg=0
            countersinfo=0
            counterpadmit=0
            counterrrecord=0
            counterbill=0
            counterreceipt=0
            counterprintbill=0

            if counterdrecord==1:
                framedoctorrecord=Frame(root,relief="solid",borderwidth=2,bg="lightgreen")
                framedoctorrecord.pack(side="right",fill=BOTH,expand=True)



                scroll1=Scrollbar(framedoctorrecord,orient=HORIZONTAL)
                scroll1.pack(side=BOTTOM,fill=X)
                scroll2=Scrollbar(framedoctorrecord,orient=VERTICAL)
                scroll2.pack(side=RIGHT,fill=Y)     
                Patient_tables=ttk.Treeview(framedoctorrecord,columns=("SrID", "SrName", "GenderSr", "SrPosition","SrDepartment","SrMailid","SrSalary","SrPhone","SrAddress"),xscrollcommand=scroll1.set,yscrollcommand=scroll2.set)
                scroll1.config(command=Patient_tables.xview)   
                scroll2.config(command=Patient_tables.yview)
                Patient_tables.heading('SrID', text="  ID", anchor=W)
                Patient_tables.heading('SrName', text="Name", anchor=W)
                Patient_tables.heading('GenderSr', text="Gender", anchor=W)
                Patient_tables.heading('SrPosition', text="Position", anchor=W)
                Patient_tables.heading('SrDepartment', text="Department", anchor=W)
                Patient_tables.heading('SrMailid', text="Mailid", anchor=W)
                Patient_tables.heading('SrSalary', text="Salary", anchor=W)
                Patient_tables.heading('SrPhone', text="Phone", anchor=W)
                Patient_tables.heading('SrAddress', text="Address", anchor=W)

                Patient_tables['show']='headings'
                Patient_tables.column("SrID",width=100)
                Patient_tables.column("SrName",width=100)
                Patient_tables.column("GenderSr",width=100)
                Patient_tables.column("SrPosition",width=100)
                Patient_tables.column("SrDepartment",width=100)
                Patient_tables.column("SrMailid",width=100)
                Patient_tables.column("SrSalary",width=100)
                Patient_tables.column("SrPhone",width=100)
                Patient_tables.column("SrAddress",width=100)
                

                Patient_tables.pack(fill=BOTH,expand=True)
                fetch_datas()





        def fetch_data():
            connection=sqlite3.connect("YASH.db")
            cursor=connection.cursor()

            query="select * from pr"
            cursor.execute(query)

            rows=cursor.fetchall()
            if len(rows)!=0:
                Patient_table.delete(*Patient_table.get_children())
                for row in rows:
                    Patient_table.insert('',END,values=row)

                    connection.commit()
            connection.close()

        def RRecord():
            global framemenuimage
            global framehome
            global frameprintbill
            global framereceiptimage
            global imagehome
            global imagemenu
            global framereceipt
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framestaffregistration
            global framestaffinformation
            global framedoctorrecord
            global framebill
            global framerrecord
            global PrPatientid
            global PrName
            global GenderPr
            global PrAge
            global PrPhone
            global PrAddress
            global PrDisease
            global PrCheckIn
            global PrBloodgroup
            global PrDoctorname
            global PrRoomNo
            global RiPatientid
            global RiName
            global GenderRi
            global RiAge
            global RiPhone
            global RiAddress
            global RiDisease
            global RiCheckIn
            global RiBloodgroup
            global RiDoctorname
            global RiRoomNo
            global Patient_table

            global counterpreg
            global counterhome
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterbill
            global counterrrecord
            global counterdrecord
            global counterreceipt
            global counterprintbill


            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass    
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
            	framedoctorrecord.destroy()
            except:
            	pass
            try:
                framebill.destroy()
            except:
                pass

            counterrrecord+=1
            counterhome=0
            countersinfo=0
            counterpreg=0
            counterpadmit=0
            counterrinfo=0
            counterainfo=0
            countersreg=0
            counterdrecord=0
            counterbill=0
            counterreceipt=0
            counterprintbill=0

            if counterrrecord==1:
                framerrecord=Frame(root,relief="solid",borderwidth=2)
                framerrecord.pack(fill=BOTH,expand=True)

                scroll1=Scrollbar(framerrecord,orient=HORIZONTAL)
                scroll1.pack(side=BOTTOM,fill=X)
                scroll2=Scrollbar(framerrecord,orient=VERTICAL)
                scroll2.pack(side=RIGHT,fill=Y)     
                Patient_table=ttk.Treeview(framerrecord,columns=("PrPatientid", "PrName", "GenderPr", "PrAge","PrPhone","PrAddress","PrDisease","PrCheckIn","PrBloodgroup","PrDoctorname","PrRoomNo"),xscrollcommand=scroll1.set,yscrollcommand=scroll2.set)
                scroll1.config(command=Patient_table.xview)
                scroll2.config(command=Patient_table.yview)
                Patient_table.heading('PrPatientid', text="Patientid", anchor=W)
                Patient_table.heading('PrName', text="Name", anchor=W)
                Patient_table.heading('GenderPr', text="Gender", anchor=W)
                Patient_table.heading('PrAge', text="Age", anchor=W)
                Patient_table.heading('PrPhone', text="Phone", anchor=W)
                Patient_table.heading('PrAddress', text="Address", anchor=W)
                Patient_table.heading('PrDisease', text="Disease", anchor=W)
                Patient_table.heading('PrCheckIn', text="CheckIn", anchor=W)
                Patient_table.heading('PrBloodgroup', text="Bloodgroup", anchor=W)
                Patient_table.heading('PrDoctorname', text="Doctorname", anchor=W)
                Patient_table.heading('PrRoomNo', text="RoomNo", anchor=W)

                Patient_table['show']='headings'
                Patient_table.column("PrPatientid",width=100)
                Patient_table.column("PrName",width=100)
                Patient_table.column("GenderPr",width=85)
                Patient_table.column("PrAge",width=70)
                Patient_table.column("PrPhone",width=100)
                Patient_table.column("PrAddress",width=140)
                Patient_table.column("PrDisease",width=100)
                Patient_table.column("PrCheckIn",width=100)
                Patient_table.column("PrBloodgroup",width=100)
                Patient_table.column("PrDoctorname",width=100)
                Patient_table.column("PrRoomNo",width=100)

                Patient_table.pack(fill=BOTH,expand=True)

                fetch_data()
        

        def Siupdate():
            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="update sr set SrID = '{}',SrName = '{}',GenderSr = '{}',SrPosition = '{}',SrDepartment = '{}',SrMailid = '{}',SrSalary = '{}',SrPhone = '{}',SrAddress = '{}'".format(SiID.get(),SiName.get(),GenderSi.get(),SiPosition.get(),SiDepartment.get(),SiMailid.get(),SiSalary.get(),SiPhone.get(),SiAddress.get())
            cursor.execute(query)
            connection.commit()
            messagebox.showinfo("Congratulations ", "Data Updated Successfully")

            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from sr"
            cursor.execute(query)
            for row in cursor:
                SiID.set(row[0])
                SiName.set(row[1])
                GenderSi.set(row[2])
                SiPosition.set(row[3])
                SiDepartment.set(row[4])
                SiMailid.set(row[5])
                SiSalary.set(row[6])
                SiPhone.set(row[7])
                SiAddress.set(row[8])

        def Sisearch(ID):
            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from Sr where SrID='{}'".format(ID)
            cursor.execute(query)
            for row in cursor:
                SiID.set(row[0])
                SiName.set(row[1])
                GenderSi.set(row[2])
                SiPosition.set(row[3])
                SiDepartment.set(row[4])
                SiMailid.set(row[5])
                SiSalary.set(row[6])
                SiPhone.set(row[7])
                SiAddress.set(row[8])

        def Sradd():
            global framemenuimage
            global framepatientregistration
            global imagehome
            global frameprintbill
            global framereceiptimage
            global imagemenu
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framestaffregistration
            global framestaffinformation
            global framebill
            global framedoctorrecord
            global framereceipt
            global SrID
            global SrName
            global GenderSr
            global SrPosition
            global SrDepartment
            global SrMailid
            global SrSalary
            global SrPhone
            global SrAddress
            global SiID
            global SiName
            global GenderSi
            global SiPosition
            global SiDepartment
            global SiMailid
            global SiSalary
            global SiPhone
            global SiAddress

            global counterpreg
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            connection = sqlite3.connect("YASH.db")  
            cursor=connection.cursor()

            x=random.randint(0, 1000)
            randomRef = str(x)
            randomRef = 'Staff2019-' + randomRef
            SrID.set(randomRef)

            query = "insert into sr values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(SrID.get(),SrName.get(),GenderSr.get(),SrPosition.get(),SrDepartment.get(),SrMailid.get(),SrSalary.get(),SrPhone.get(),SrAddress.get())
            cursor.execute(query)
            connection.commit()

            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from sr"
            cursor.execute(query)
            messagebox.showinfo("Congratulations ", "Data Added Successfully ")

        def sinfo():
            global framemenuimage
            global framehome
            global frameprintbill
            global framereceiptimage
            global imagemenu
            global imagehome
            global framereceipt
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framedoctorrecord
            global SrID
            global SrName
            global GenderSr
            global SrPosition
            global SrDepartment
            global SrMailid
            global SrSalary
            global SrPhone
            global SrAddress
            global SiID
            global SiName
            global GenderSi
            global SiPosition
            global SiDepartment
            global SiMailid
            global SiSalary
            global SiPhone
            global SiAddress

            global counterpreg
            global counterhome
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterrrecord
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            countersinfo+=1
            counterhome=0
            counterpreg=0
            counterpadmit=0
            counterrinfo=0
            counterainfo=0
            countersreg=0
            counterrrecord=0
            counterbill=0
            counterdrecord=0
            counterreceipt=0
            counterprintbill=0

            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
            	framedoctorrecord.destroy()
            except:
            	pass
            
            if countersinfo==1:
                framestaffinformation=Frame(root,bg="lightgreen",)
                framestaffinformation.pack(side="right",fill=BOTH,expand=True)

                framestaffinformationtop=Frame(framestaffinformation,height="200",relief="solid",bg="sandybrown",borderwidth=2)
                framestaffinformationtop.pack(side=TOP,fill=X);

                labelstaffinformation=Label(framestaffinformationtop,text="Doctor Information",bg="sandybrown",font=("calibri",23,"bold"))
                labelstaffinformation.pack(anchor="center")

                framestaffinformationleft=Frame(framestaffinformation,height="60",width="300",bg="lightgreen",relief="solid",borderwidth=2)
                framestaffinformationleft.pack(side=LEFT,fill=Y);

                labelUsername=Label(framestaffinformationleft,text="User ID",bg="lightgreen",font=("calibri",20,"bold"))
                labelUsername.pack(anchor=CENTER,pady=20)
                
                searchID=StringVar()
                Username=Entry(framestaffinformationleft,width="20",textvariable=searchID,font=("calibri",15,"bold"))
                Username.pack()

                Searchbutton=Button(framestaffinformationleft,text="Search",command=lambda:Sisearch(searchID.get()),bg="yellow",font=("calibri",15,"bold"))
                Searchbutton.pack(side=TOP,pady=8);

                framestaffinformationright=Frame(framestaffinformation,height="60",bg="lightgreen",width="300",relief="solid",borderwidth=2)
                framestaffinformationright.pack(side=RIGHT,fill=Y);

                buttonUpdate=Button(framestaffinformationright,text="Update",command=Siupdate,bd=7,bg="yellow",width=10,font=("calibri",15,"bold"))
                buttonUpdate.pack(side=TOP,padx="70",pady=100);



                framestaffinformationcenter=Frame(framestaffinformation,height="60",width="130",bg="lightgreen",relief="solid",borderwidth=2)
                framestaffinformationcenter.pack(anchor="center",fill=BOTH,expand=True);

                labelid=Label(framestaffinformationcenter,text="ID:                 ",bg="lightgreen",font=("calibri",20,"bold"))
                labelid.grid(row=0,column=0,padx=10,pady=15)

                SiID=StringVar()
                ID=Entry(framestaffinformationcenter,textvariable=SiID,font=("calibri",20,"bold"))
                ID.grid(row=0,column=1,padx=0)

                labelName=Label(framestaffinformationcenter,text="Name:            ",bg="lightgreen",font=("calibri",20,"bold"))
                labelName.grid(row=1,column=0,padx=10,pady=15)
                
                SiName=StringVar()
                Name=Entry(framestaffinformationcenter,textvariable=SiName,font=("calibri",20,"bold"))
                Name.grid(row=1,column=1,padx=0)

                GenderSi=StringVar()
                GenderSi.set("")

                labelGender=Label(framestaffinformationcenter,text="Gender:          ",bg="lightgreen",font=("calibri",20,"bold"))
                labelGender.grid(row=2,column=0)
                        
                i= IntVar()
                r1 = Radiobutton(framestaffinformationcenter,text="male",value=1,bg="lightgreen",variable=GenderSi,font=("calibri",20,"bold"))
                r2 = Radiobutton(framestaffinformationcenter,text="female",value=2,bg="lightgreen",variable=GenderSi,font=("calibri",20,"bold"))
                r1.grid(row=2,column=1,sticky="w")
                r2.grid(row=2,column=1,sticky="e",padx=0)


                labelPosition=Label(framestaffinformationcenter,text="Position:         ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPosition.grid(row=3,column=0,padx=10,pady=15)
                SiPosition=StringVar()
                Position=Entry(framestaffinformationcenter,textvariable=SiPosition,font=("calibri",20,"bold"))
                Position.grid(row=3,column=1,padx=0)

                labelDepartment=Label(framestaffinformationcenter,text="Department:         ",bg="lightgreen",font=("calibri",20,"bold"))
                labelDepartment.grid(row=4,column=0,padx=10,pady=15)
                SiDepartment=StringVar()
                Department=Entry(framestaffinformationcenter,textvariable=SiDepartment,font=("calibri",20,"bold"))
                Department.grid(row=4,column=1,padx=0)

                labelMailid=Label(framestaffinformationcenter,text="Mail ID:         ",bg="lightgreen",font=("calibri",20,"bold"))
                labelMailid.grid(row=5,column=0,padx=10,pady=15)
                SiMailid=StringVar()
                Mailid=Entry(framestaffinformationcenter,textvariable=SiMailid,font=("calibri",20,"bold"))
                Mailid.grid(row=5,column=1,padx=0)

                labelSalary=Label(framestaffinformationcenter,text="Salary:            ",bg="lightgreen",font=("calibri",20,"bold"))
                labelSalary.grid(row=6,column=0,padx=10,pady=15)
                SiSalary=StringVar()
                Salary=Entry(framestaffinformationcenter,textvariable=SiSalary,font=("calibri",20,"bold"))
                Salary.grid(row=6,column=1,padx=0)

                labelPhone=Label(framestaffinformationcenter,text="Phone:           ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPhone.grid(row=7,column=0,padx=10,pady=15)

                SiPhone=StringVar()
                Phone=Entry(framestaffinformationcenter,textvariable=SiPhone,font=("calibri",20,"bold"))
                Phone.grid(row=7,column=1,padx=0)

                labelAddress=Label(framestaffinformationcenter,text="Address:         ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAddress.grid(row=8,column=0,padx=10,pady=15)

                SiAddress=StringVar()
                Address=Entry(framestaffinformationcenter,textvariable=SiAddress,font=("calibri",20,"bold"))
                Address.grid(row=8,column=1,padx=0)

                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_rowconfigure(4,weight=1)
                root.grid_rowconfigure(5,weight=1)
                root.grid_rowconfigure(6,weight=1)
                root.grid_rowconfigure(7,weight=1)
                root.grid_rowconfigure(8,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)

        def sreg():
            global framemenuimage
            global framehome
            global frameprintbill
            global framereceiptimage
            global imagemenu
            global imagehome
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framebill
            global framedoctorrecord
            global framereceipt
            global SrID
            global SrName
            global GenderSr
            global SrPosition
            global SrDepartment
            global SrMailid
            global SrSalary
            global SrPhone
            global SrAddress
            global SiID
            global SiName
            global GenderSi
            global SiPosition
            global SiDepartment
            global SiMailid
            global SiSalary
            global SiPhone
            global SiAddress

            global counterpreg
            global counterhome
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterrrecord
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            countersreg+=1
            counterhome=0
            counterpreg=0
            counterpadmit=0
            counterrinfo=0
            counterainfo=0
            countersinfo=0
            counterrrecord=0
            counterbill=0
            counterdrecord=0
            counterreceipt=0
            counterprintbill=0

            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
            	framedoctorrecord.destroy()
            except:
            	pass
            

            if countersreg==1:
                framestaffregistration=Frame(root,bg="lightgreen")
                framestaffregistration.pack(side="right",fill=BOTH,expand=True)

                framestaffregistrationtop=Frame(framestaffregistration,height="200",bg="sandybrown",relief="solid",borderwidth=2,)
                framestaffregistrationtop.pack(side=TOP,fill=X);

                labelstaffregistration=Label(framestaffregistrationtop,text="Doctor Registration",bg="sandybrown",font=("calibri",23,"bold"))
                labelstaffregistration.pack(anchor="center")

                framestaffregistrationcenter=Frame(framestaffregistration,height="60",width="130",relief="solid",bg="lightgreen",borderwidth=2)
                framestaffregistrationcenter.pack(side=LEFT,fill=BOTH,expand=True);

                labelid=Label(framestaffregistrationcenter,text="ID:                 ",bg="lightgreen",font=("calibri",21,"bold"))
                labelid.grid(row=0,column=0,padx=120,pady=15)

                SrID=StringVar()
                ID=Entry(framestaffregistrationcenter,textvariable=SrID,font=("calibri",20,"bold"))
                ID.grid(row=0,column=1,padx=0)

                labelName=Label(framestaffregistrationcenter,text="Name:            ",bg="lightgreen",font=("calibri",21,"bold"))
                labelName.grid(row=1,column=0,padx=10,pady=15)
                
                SrName=StringVar()
                Name=Entry(framestaffregistrationcenter,textvariable=SrName,font=("calibri",20,"bold"))
                Name.grid(row=1,column=1,padx=0)

                GenderSr=StringVar()
                GenderSr.set("")

                labelGender=Label(framestaffregistrationcenter,text="Gender:          ",bg="lightgreen",font=("calibri",21,"bold"))
                labelGender.grid(row=2,column=0)
                        
                i= IntVar()
                r1 = Radiobutton(framestaffregistrationcenter,text="male",value="Male",bg="lightgreen",variable=GenderSr,font=("calibri",20,"bold"))
                r2 = Radiobutton(framestaffregistrationcenter,text="female",value="Female",variable=GenderSr,bg="lightgreen",font=("calibri",20,"bold"))
                r1.grid(row=2,column=1,sticky="w")
                r2.grid(row=2,column=1,sticky="e",padx=0)

                labelPosition=Label(framestaffregistrationcenter,text="Position:         ",bg="lightgreen",font=("calibri",21,"bold"))
                labelPosition.grid(row=3,column=0,padx=10,pady=15)

                SrPosition=StringVar()
                Position=Entry(framestaffregistrationcenter,textvariable=SrPosition,font=("calibri",20,"bold"))
                Position.grid(row=3,column=1,padx=0)

                labelDepartment=Label(framestaffregistrationcenter,text="Department:         ",bg="lightgreen",font=("calibri",21,"bold"))
                labelDepartment.grid(row=4,column=0,padx=10,pady=15)

                SrDepartment=StringVar()
                Department=Entry(framestaffregistrationcenter,textvariable=SrDepartment,font=("calibri",20,"bold"))
                Department.grid(row=4,column=1,padx=0)

                labelMailid=Label(framestaffregistrationcenter,text="Mail ID:         ",bg="lightgreen",font=("calibri",21,"bold"))
                labelMailid.grid(row=5,column=0,padx=10,pady=15)

                SrMailid=StringVar()
                Mailid=Entry(framestaffregistrationcenter,textvariable=SrMailid,font=("calibri",20,"bold"))
                Mailid.grid(row=5,column=1,padx=0)

                labelSalary=Label(framestaffregistrationcenter,text="Salary:            ",bg="lightgreen",font=("calibri",21,"bold"))
                labelSalary.grid(row=6,column=0,padx=10,pady=15)

                SrSalary=StringVar()
                Salary=Entry(framestaffregistrationcenter,textvariable=SrSalary,font=("calibri",20,"bold"))
                Salary.grid(row=6,column=1,padx=0)

                labelPhone=Label(framestaffregistrationcenter,text="Phone:           ",bg="lightgreen",font=("calibri",21,"bold"))
                labelPhone.grid(row=7,column=0,padx=10,pady=15)

                SrPhone=StringVar()
                Phone=Entry(framestaffregistrationcenter,textvariable=SrPhone,font=("calibri",20,"bold"))
                Phone.grid(row=7,column=1,padx=0)

                labelAddress=Label(framestaffregistrationcenter,text="Address:         ",bg="lightgreen",font=("calibri",21,"bold"))
                labelAddress.grid(row=8,column=0,padx=10,pady=15)

                SrAddress=StringVar()
                Address=Entry(framestaffregistrationcenter,textvariable=SrAddress,font=("calibri",20,"bold"))
                Address.grid(row=8,column=1,padx=0)

                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_rowconfigure(4,weight=1)
                root.grid_rowconfigure(5,weight=1)
                root.grid_rowconfigure(6,weight=1)
                root.grid_rowconfigure(7,weight=1)
                root.grid_rowconfigure(8,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)

                framestaffregistrationright=Frame(framestaffregistration,height="60",width="300",bg="lightgreen",relief="solid",borderwidth=2)
                framestaffregistrationright.pack(side=RIGHT,fill=Y);

                buttonAdd=Button(framestaffregistrationright,text="ADD",command=Sradd,bd=7,bg="yellow",width=10,font=("calibri",15,"bold"))
                buttonAdd.pack(side=TOP,padx="70",pady=100);

        def Aisearch(ID):
            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from pa where PaPatientid='{}'".format(ID)
            cursor.execute(query)
            for row in cursor:
                AiPatientid.set(row[0])
                AiName.set(row[1])
                GenderAi.set(row[2])
                AiAge.set(row[3])
                AiPhone.set(row[4])
                AiAddress.set(row[5])
                AiDisease.set(row[6])
                AiCheckIn.set(row[7])
                AiBloodgroup.set(row[8])
                AiDoctorname.set(row[9])
                AiCheckOut.set(row[10])
                AiRoomNo.set(row[11])
                AiRoomtype.set(row[12])
                AiPrice.set(row[13])

        def Aiupdate():
            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="update pa set PaPatientid = '{}',PaName = '{}',GenderPa = '{}',PaAge = '{}',PaPhone = '{}',PaAddress = '{}',PaDisease = '{}',PaCheckIn = '{}',PaBloodgroup = '{}',PaDoctorname = '{}',PaCheckOut = '{}',PaRoomNo = '{}',PaRoomtype = '{}',PaPrice = '{}'".format(AiPatientid.get(),AiName.get(),GenderAi.get(),AiAge.get(),AiPhone.get(),AiAddress.get(),AiDisease.get(),AiCheckIn.get(),AiBloodgroup.get(),AiDoctorname.get(),AiCheckOut.get(),AiRoomNo.get(),AiRoomtype.get(),AiPrice.get())
            cursor.execute(query)
            connection.commit()
            messagebox.showinfo("Congratulations ", "Data Updated Successfully")
                                                                                                                                                                                                                                                                                                                                            
            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from pa"
            cursor.execute(query)
            for row in cursor:
                AiPatientid.set(row[0])
                AiName.set(row[1])
                GenderAi.set(row[2])
                AiAge.set(row[3])
                AiPhone.set(row[4])
                AiAddress.set(row[5])
                AiDisease.set(row[6])
                AiCheckIn.set(row[7])
                AiBloodgroup.set(row[8])
                AiDoctorname.set(row[9])
                AiCheckOut.set(row[10])
                AiRoomNo.set(row[11])
                AiRoomtype.set(row[12])
                AiPrice.set(row[13])

        def ainfo():
            global framemenuimage
            global framehome
            global frameprintbill
            global imagemenu
            global framereceiptimage
            global imagehome
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framebill
            global framedoctorrecord
            global framereceipt
            global AiPatientid
            global AiName
            global GenderAi
            global AiAge
            global AiPhone
            global AiAddress
            global AiDisease
            global AiCheckIn
            global AiBloodgroup
            global AiDoctorname
            global AiCheckOut
            global AiRoomNo
            global AiRoomtype
            global AiPrice

            global counterpreg
            global counterhome
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterrrecord
            global counterbill
            global counterdrecord
            global counterreceipt
            

            counterainfo+=1
            counterhome=0
            counterpreg=0
            counterpadmit=0
            counterrinfo=0
            countersreg=0
            countersinfo=0
            counterrrecord=0
            counterbill=0
            counterdrecord=0
            counterreceipt=0
            counterprintbill=0
            

            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
            	framedoctorrecord.destroy()
            except:
            	pass
            
            if counterainfo==1: 
                frameainfo=Frame(root,width=100,height=100,bg="lightgreen")
                frameainfo.pack(side="right",fill=BOTH,expand=TRUE)

                frameainfotop=Frame(frameainfo,height="200",relief="solid",borderwidth=2,bg="sandybrown")
                frameainfotop.pack(side=TOP,fill=X);

                labelpatientinfotext=Label(frameainfotop,text="Admit Information",bg="sandybrown",font=("calibri",23,"bold"))
                labelpatientinfotext.pack(anchor="center")

                frameainfoleft=Frame(frameainfo,height="60",width="300",relief="solid",bg="lightgreen",borderwidth=2)
                frameainfoleft.pack(side=LEFT,fill=Y);

                labelinputpatientname=Label(frameainfoleft,text="Input Patient's ID",bg="lightgreen",font=("calibri",17,"bold"))
                labelinputpatientname.pack(anchor=CENTER,pady=20)

                searchID=StringVar()
                inputpatientname=Entry(frameainfoleft,textvariable=searchID,width="20",font=("calibri",15,"bold"))
                inputpatientname.pack()

                Search1button=Button(frameainfoleft,text="Search",command=lambda: Aisearch(searchID.get()),bg="yellow",font=("calibri",15,"bold"))
                Search1button.pack(side=TOP,pady=8)

                frameainfocenter=Frame(frameainfo,height="60",width="130",relief="solid",bg="lightgreen",borderwidth=2)
                frameainfocenter.pack(side=LEFT,fill=BOTH,expand=True);

                labelPatientid=Label(frameainfocenter,text="Patient ID:    ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPatientid.grid(row=0,column=0,pady=10,sticky="w")
                
                AiPatientid=StringVar()
                Patientid=Entry(frameainfocenter,textvariable=AiPatientid,font=("calibri",20,"bold"))
                Patientid.grid(row=0,column=1,padx=1,pady=17,sticky="w")
                
                labelPatientid=Label(frameainfocenter,text="",bg="lightgreen",font=("calibri",20,"bold"))
                labelPatientid.grid(row=0,column=2,sticky="e")

                labelName=Label(frameainfocenter,text="Name:       ",bg="lightgreen",font=("calibri",20,"bold"))
                labelName.grid(row=1,column=0,padx=0,pady=17,sticky="w")

                AiName=StringVar()
                Name=Entry(frameainfocenter,textvariable=AiName,font=("calibri",20,"bold"))
                Name.grid(row=1,column=1)

                GenderAi=StringVar()
                GenderAi.set("")

                labelGender=Label(frameainfocenter,text="Gender:        ",bg="lightgreen",font=("calibri",20,"bold"))
                labelGender.grid(row=2,column=0)
                        
                i= IntVar()
                r1 = Radiobutton(frameainfocenter,text="male",value=1,variable=GenderAi,bg="lightgreen",font=("calibri",20,"bold"))
                r2 = Radiobutton(frameainfocenter,text="female",value=2,variable=GenderAi,bg="lightgreen",font=("calibri",20,"bold"))
                r1.grid(row=2,column=1,sticky="w")
                r2.grid(row=2,column=1,sticky="e",padx=0)

                labelAge=Label(frameainfocenter,text="Age:         ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAge.grid(row=3,column=0,sticky="w",padx=0,pady=17)

                AiAge=StringVar()
                Age=Entry(frameainfocenter,textvariable=AiAge,font=("calibri",20,"bold"))
                Age.grid(row=3,column=1)

                labelPhone=Label(frameainfocenter,text="Phone:     ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPhone.grid(row=4,column=0,sticky="w",padx=0,pady=17)

                AiPhone=StringVar()
                Phone=Entry(frameainfocenter,textvariable=AiPhone,font=("calibri",20,"bold"))
                Phone.grid(row=4,column=1)

                labelAddress=Label(frameainfocenter,text="Address:  ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAddress.grid(row=5,column=0,sticky="w",padx=0,pady=17)

                AiAddress=StringVar()
                Address=Entry(frameainfocenter,textvariable=AiAddress,font=("calibri",20,"bold"))
                Address.grid(row=5,column=1)

                labelDisease=Label(frameainfocenter,text="Disease:   ",bg="lightgreen",font=("calibri",20,"bold"))
                labelDisease.grid(row=6,column=0,sticky="w",padx=0,pady=17)

                AiDisease=StringVar()
                Disease=Entry(frameainfocenter,textvariable=AiDisease,font=("calibri",20,"bold"))
                Disease.grid(row=6,column=1)

                labelCheckIn=Label(frameainfocenter,text="Check In",bg="lightgreen",font=("calibri",20,"bold"))
                labelCheckIn.grid(row=7,column=0,sticky="w",padx=0,pady=17)

                AiCheckIn=StringVar()
                CheckIn=Entry(frameainfocenter,textvariable=AiCheckIn,font=("calibri",20,"bold"))
                CheckIn.grid(row=7,column=1)


                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_rowconfigure(4,weight=1)
                root.grid_rowconfigure(5,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)

                frameainforight=Frame(frameainfo,height="60",width="300",relief="solid",borderwidth=2,bg="lightgreen")
                frameainforight.pack(side=RIGHT,fill=Y);

                labelBloodgroup=Label(frameainforight,text="Blood Group",bg="lightgreen",font=("calibri",17,"bold"))
                labelBloodgroup.pack(padx=80,pady=10)

                AiBloodgroup=StringVar()
                Bloodgroup=Entry(frameainforight,textvariable=AiBloodgroup,width="20",font=("calibri",17,"bold"))
                Bloodgroup.pack()

                labelDoctorname=Label(frameainforight,text="Doctor Name",bg="lightgreen",font=("calibri",17,"bold"))
                labelDoctorname.pack(padx=80,pady=10)

                AiDoctorname=StringVar()
                Doctorname=Entry(frameainforight,textvariable=AiDoctorname,width="20",font=("calibri",17,"bold"))
                Doctorname.pack()

                labelCheckOut=Label(frameainforight,text="Check OUT",bg="lightgreen",font=("calibri",17,"bold"))
                labelCheckOut.pack(pady=10)

                AiCheckOut=StringVar()
                CheckOut=Entry(frameainforight,textvariable=AiCheckOut,width="20",font=("calibri",17,"bold"))
                CheckOut.pack()

                labelRoomNo=Label(frameainforight,text="Room No.",bg="lightgreen",font=("calibri",17,"bold"))
                labelRoomNo.pack(pady=10)

                AiRoomNo=StringVar()
                RoomNo=Entry(frameainforight,textvariable=AiRoomNo,width="20",font=("calibri",17,"bold"))
                RoomNo.pack()

                labelRoomType=Label(frameainforight,text="Room Type",bg="lightgreen",font=("calibri",17,"bold"))
                labelRoomType.pack(pady=10)

                list=["Normal Ward","Personal Room"]
                AiRoomtype=StringVar(frameainforight)

                dropdownlist=OptionMenu(frameainforight,AiRoomtype,*list)
                dropdownlist.pack()

                labelPrice=Label(frameainforight,text="Price.",bg="lightgreen",font=("calibri",17,"bold"))
                labelPrice.pack(pady=10)

                AiPrice=StringVar()
                Price=Entry(frameainforight,textvariable=AiPrice,width="20",font=("calibri",17,"bold"))
                Price.pack()

                Updatebutton=Button(frameainforight,text="Update",command=Aiupdate,bg="yellow",width=15,bd=7,font=("calibri",15,"bold"))
                Updatebutton.pack(side=LEFT,padx=50);

        def Paadd():
            global framemenuimage
            global framehome
            global frameprintbill
            global framereceiptimage
            global imagemenu
            global imagehome
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framestaffregistration
            global framestaffinformation
            global framebill
            global framedoctorrecord
            global framereceipt
            global PaPatientid
            global PaName
            global GenderPa
            global PaAge
            global PaPhone
            global PaAddress
            global PaDisease
            global PaCheckIn
            global PaBloodgroup
            global PaDoctorname
            global PaCheckOut
            global PaRoomNo
            global PaRoomtype
            global PaPrice
            global AiPatientid
            global AiName
            global GenderAi
            global AiAge
            global AiPhone
            global AiAddress
            global AiDisease
            global AiCheckIn
            global AiBloodgroup
            global AiDoctorname
            global AiCheckOut
            global AiRoomNo
            global AiRoomtype
            global AiPrice

            global counterpreg
            global counterhome
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            connection = sqlite3.connect("YASH.db")  
            cursor=connection.cursor()

            query = "insert into pa values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(PaPatientid.get(),PaName.get(),GenderPa.get(),PaAge.get(),PaPhone.get(),PaAddress.get(),PaDisease.get(),PaCheckIn.get(),PaBloodgroup.get(),PaDoctorname.get(),PaCheckOut.get(),PaRoomNo.get(),PaRoomtype.get(),PaPrice.get())
            cursor.execute(query)
            connection.commit()

            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from pa"
            cursor.execute(query)
            messagebox.showinfo("Congratulations ", "Data Added Successfully ")
        
        def padmit():
            global framemenuimage
            global framehome
            global frameprintbill
            global framereceiptimage
            global imagemenu
            global imagehome
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framebill
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framebill
            global framedoctorrecord
            global framereceipt
            global PaPatientid
            global PaName
            global GenderPa
            global PaAge
            global PaPhone
            global PaAddress
            global PaDisease
            global PaCheckIn
            global PaBloodgroup
            global PaDoctorname
            global PaCheckOut
            global PaRoomNo
            global PaRoomtype
            global PaPrice

            global counterpreg
            global counterhome
            global counterpadmit
            global counterrinfo
            global counterainfo
            global countersreg
            global countersinfo
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            counterpadmit+=1
            counterhome=0
            counterpreg=0
            counterrinfo=0
            counterainfo=0
            countersreg=0
            countersinfo=0
            counterrrecord=0
            counterbill=0
            counterdrecord=0
            counterreceipt=0
            counterprintbill=0


            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
            	framedoctorrecord.destroy()
            except:
            	pass

            if counterpadmit==1:    
                framepatientadmit=Frame(root,width=100,bg="lightgreen",height=100)
                framepatientadmit.pack(side="right",fill=BOTH,expand=TRUE)

                framepatientadmittop=Frame(framepatientadmit,height="200",relief="solid",borderwidth=2,bg="sandybrown")
                framepatientadmittop.pack(side=TOP,fill=X);

                labelpatientrinfotext=Label(framepatientadmittop,text="Patient Admit",bg="sandybrown",font=("calibri",23,"bold"))
                labelpatientrinfotext.pack(anchor="center")

                framepatientadmitcenter=Frame(framepatientadmit,height="60",width="130",bg="lightgreen",relief="solid",borderwidth=2)
                framepatientadmitcenter.pack(side=LEFT,fill=BOTH,expand=True);

                labelPatientid=Label(framepatientadmitcenter,text="Patient ID:    ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPatientid.grid(row=0,column=0,padx=90,pady=10,sticky="w")
                
                PaPatientid=StringVar()
                Patientid=Entry(framepatientadmitcenter,textvariable=PaPatientid,font=("calibri",20,"bold"))
                Patientid.grid(row=0,column=1,padx=1,pady=17,sticky="w")

                labelName=Label(framepatientadmitcenter,text="Name:       ",bg="lightgreen",font=("calibri",20,"bold"))
                labelName.grid(row=1,column=0,padx=90,pady=17,sticky="w")

                PaName=StringVar()
                Name=Entry(framepatientadmitcenter,textvariable=PaName,font=("calibri",20,"bold"))
                Name.grid(row=1,column=1)

                GenderPa=StringVar()
                GenderPa.set("")

                labelGender=Label(framepatientadmitcenter,text="Gender:        ",bg="lightgreen",font=("calibri",20,"bold"))
                labelGender.grid(row=2,column=0)
                        
                i= IntVar()
                r1 = Radiobutton(framepatientadmitcenter,text="male",value=1,variable=GenderPa,bg="lightgreen",font=("calibri",20,"bold"))
                r2 = Radiobutton(framepatientadmitcenter,text="female",value=2,variable=GenderPa,bg="lightgreen",font=("calibri",20,"bold"))
                r1.grid(row=2,column=1,sticky="w")
                r2.grid(row=2,column=1,sticky="e",padx=0)

                labelAge=Label(framepatientadmitcenter,text="Age:         ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAge.grid(row=3,column=0,sticky="w",padx=90,pady=17)

                PaAge=StringVar()
                Age=Entry(framepatientadmitcenter,textvariable=PaAge,font=("calibri",20,"bold"))
                Age.grid(row=3,column=1)

                labelPhone=Label(framepatientadmitcenter,text="Phone:     ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPhone.grid(row=4,column=0,sticky="w",padx=90,pady=17)

                PaPhone=StringVar()
                Phone=Entry(framepatientadmitcenter,textvariable=PaPhone,font=("calibri",20,"bold"))
                Phone.grid(row=4,column=1)

                labelAddress=Label(framepatientadmitcenter,text="Address:  ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAddress.grid(row=5,column=0,padx=90,pady=17,sticky="w")

                PaAddress=StringVar()
                Address=Entry(framepatientadmitcenter,textvariable=PaAddress,font=("calibri",20,"bold"))
                Address.grid(row=5,column=1)

                labelDisease=Label(framepatientadmitcenter,text="Disease:   ",bg="lightgreen",font=("calibri",20,"bold"))
                labelDisease.grid(row=6,column=0,padx=90,pady=17,sticky="w")

                PaDisease=StringVar()
                Disease=Entry(framepatientadmitcenter,textvariable=PaDisease,font=("calibri",20,"bold"))
                Disease.grid(row=6,column=1)

                labelCheckIn=Label(framepatientadmitcenter,text="Check In",bg="lightgreen",font=("calibri",20,"bold"))
                labelCheckIn.grid(row=7,column=0,padx=90,pady=17,sticky="w")

                PaCheckIn=StringVar()
                CheckIn=Entry(framepatientadmitcenter,textvariable=PaCheckIn,font=("calibri",20,"bold"))
                CheckIn.grid(row=7,column=1)

                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_rowconfigure(4,weight=1)
                root.grid_rowconfigure(5,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)

                framepatientadmitright=Frame(framepatientadmit,height="60",width="300",relief="solid",bg="lightgreen",borderwidth=2)
                framepatientadmitright.pack(side=RIGHT,fill=Y);

                labelBloodgroup=Label(framepatientadmitright,text="Blood group",bg="lightgreen",font=("calibri",17,"bold"))
                labelBloodgroup.pack(padx=80,pady=10)

                PaBloodgroup=StringVar()
                Bloodgroup=Entry(framepatientadmitright,textvariable=PaBloodgroup,width="20",font=("calibri",17,"bold"))
                Bloodgroup.pack()

                labelDoctorname=Label(framepatientadmitright,text="Doctor Name",bg="lightgreen",font=("calibri",17,"bold"))
                labelDoctorname.pack(padx=80,pady=10)

                PaDoctorname=StringVar()
                Doctorname=Entry(framepatientadmitright,textvariable=PaDoctorname,width="20",font=("calibri",17,"bold"))
                Doctorname.pack()

                labelCheckOut=Label(framepatientadmitright,text="Check OUT",bg="lightgreen",font=("calibri",17,"bold"))
                labelCheckOut.pack(pady=10)

                PaCheckOut=StringVar()
                CheckOut=Entry(framepatientadmitright,textvariable=PaCheckOut,width="20",font=("calibri",17,"bold"))
                CheckOut.pack()

                labelRoomNo=Label(framepatientadmitright,text="Room No.",bg="lightgreen",font=("calibri",17,"bold"))
                labelRoomNo.pack(pady=10)

                PaRoomNo=StringVar()
                RoomNo=Entry(framepatientadmitright,textvariable=PaRoomNo,width="20",font=("calibri",17,"bold"))
                RoomNo.pack()

                labelRoomType=Label(framepatientadmitright,text="Room Type",bg="lightgreen",font=("calibri",17,"bold"))
                labelRoomType.pack(pady=10)

                list=["Normal Ward","Personal Room"]
                PaRoomtype=StringVar(framepatientadmitright)

                dropdownlist=OptionMenu(framepatientadmitright,PaRoomtype,*list)
                dropdownlist.pack()

                labelPrice=Label(framepatientadmitright,text="Price.",bg="lightgreen",font=("calibri",17,"bold"))
                labelPrice.pack(pady=10)

                PaPrice=StringVar()
                Price=Entry(framepatientadmitright,textvariable=PaPrice,width="20",font=("calibri",17,"bold"))
                Price.pack()

                ADDAbutton=Button(framepatientadmitright,text="ADD",command=Paadd,bg="yellow",width=15,bd=7,font=("calibri",15,"bold"))
                ADDAbutton.pack(pady=9);




        def Risearch(ID):
            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from pr where PrPatientid='{}'".format(ID)
            cursor.execute(query)
            for row in cursor:
                RiPatientid.set(row[0])
                RiName.set(row[1])
                GenderRi.set(row[2])
                RiAge.set(row[3])
                RiPhone.set(row[4])
                RiAddress.set(row[5])
                RiDisease.set(row[6])
                RiCheckIn.set(row[7])
                RiBloodgroup.set(row[8])
                RiDoctorname.set(row[9])
                RiRoomNo.set(row[10])

        def Riupdate():
            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="update pr set PrPatientid = '{}',PrName = '{}',GenderPr = '{}',PrAge = '{}',PrPhone = '{}',PrAddress = '{}',PrDisease = '{}',PrCheckIn = '{}',PrBloodgroup = '{}',PrDoctorname = '{}',PrRoomNo = '{}'".format(RiPatientid.get(),RiName.get(),GenderRi.get(),RiAge.get(),RiPhone.get(),RiAddress.get(),RiDisease.get(),RiCheckIn.get(),RiBloodgroup.get(),RiDoctorname.get(),RiRoomNo.get())
            cursor.execute(query)
            connection.commit()
            messagebox.showinfo("Congratulations ", "Data Updated Successfully")

            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from pr"
            cursor.execute(query)
            for row in cursor:
                RiPatientid.set(row[0])
                RiName.set(row[1])
                GenderRi.set(row[2])
                RiAge.set(row[3])
                RiPhone.set(row[4])
                RiAddress.set(row[5])
                RiDisease.set(row[6])
                RiCheckIn.set(row[7])
                RiBloodgroup.set(row[8])
                RiDoctorname.set(row[9])
                RiRoomNo.set(row[10])


        def Pradd():
            global framemenuimage
            global framepatientregistration
            global frameprintbill
            global framerinfo
            global framereceiptimage
            global imagemenu
            global imagehome
            global framereceipt
            global PrPatientid
            global PrName
            global GenderPr
            global PrAge
            global PrPhone
            global PrAddress
            global PrDisease
            global PrCheckIn
            global PrBloodgroup
            global PrDoctorname
            global PrRoomNo
            global RiPatientid
            global RiName
            global GenderRi
            global RiAge
            global RiPhone
            global RiAddress
            global RiDisease
            global RiCheckIn
            global RiBloodgroup
            global RiDoctorname
            global RiRoomNo

            global counterpreg
            global counterrinfo
            

            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()

            x=random.randint(0, 10000000)
            randomRef = str(x)
            randomRef = '2019-' + randomRef
            PrPatientid.set(randomRef)
            

            query = "insert into pr values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(PrPatientid.get(),PrName.get(),GenderPr.get(),PrAge.get(),PrPhone.get(),PrAddress.get(),PrDisease.get(),PrCheckIn.get(),PrBloodgroup.get(),PrDoctorname.get(),PrRoomNo.get())
            cursor.execute(query)
            connection.commit()

            connection = sqlite3.connect("YASH.db")
            cursor=connection.cursor()
            query="select * from pr"
            cursor.execute(query)
            messagebox.showinfo("Congratulations ", "Data Added Successfully ")

        def rinfo():
            global framemenuimage
            global framehome
            global frameprintbill
            global framereceiptimage
            global imagemenu
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framemenuroot
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framedoctorrecord
            global framebill
            global framereceipt
            global PrPatientid
            global PrName
            global GenderPr
            global PrAge
            global PrPhone
            global PrAddress
            global PrDisease
            global PrCheckIn
            global PrBloodgroup
            global PrDoctorname
            global PrRoomNo
            global RiPatientid
            global RiName
            global GenderRi
            global RiAge
            global RiPhone
            global RiAddress
            global RiDisease
            global RiCheckIn
            global RiBloodgroup
            global RiDoctorname
            global RiRoomNo

            global counterpreg
            global counterhome
            global counterrinfo
            global counterpadmit
            global counterainfo
            global countersreg
            global countersinfo
            global counterrecord
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            counterrinfo+=1
            counterhome=0
            counterpreg=0
            counterlogin=0
            counterpadmit=0
            counterainfo=0
            countersreg=0
            countersinfo=0
            counterrecord=0
            counterbill=0
            counterdrecord=0
            counterreceipt=0
            counterprintbill=0

            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
            	framedoctorrecord.destroy()
            except:
            	pass
            
            if counterrinfo==1: 
                framerinfo=Frame(root,width=100,height=100)
                framerinfo.pack(side="right",fill=BOTH,expand=TRUE)

                framerinfotop=Frame(framerinfo,height="200",relief="solid",borderwidth=2,bg="sandybrown")
                framerinfotop.pack(side=TOP,fill=X);

                labelpatientrinfotext=Label(framerinfotop,text="Registration Information",bg="sandybrown",font=("calibri",23,"bold"))
                labelpatientrinfotext.pack(anchor="center")

                framerinfoleft=Frame(framerinfo,height="60",width="300",relief="solid",borderwidth=2,bg="lightgreen")
                framerinfoleft.pack(side=LEFT,fill=Y);

                labelinputpatientname=Label(framerinfoleft,text="Input Patient's ID",bg="lightgreen",font=("calibri",17,"bold"))
                labelinputpatientname.pack(anchor=CENTER,pady=20)

                searchID=StringVar()
                inputpatientname=Entry(framerinfoleft,textvariable=searchID,width="20",font=("calibri",15,"bold"))
                inputpatientname.pack()

                Searchbutton=Button(framerinfoleft,text="Search",command=lambda: Risearch(searchID.get()),bg="yellow",font=("calibri",15,"bold"))
                Searchbutton.pack(side=TOP,pady=8);

                framerinfocenter=Frame(framerinfo,height="60",width="130",bg="lightgreen",relief="solid",borderwidth=2)
                framerinfocenter.pack(side=LEFT,fill=BOTH,expand=True);

                labelPatientid=Label(framerinfocenter,text="Patient ID:    ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPatientid.grid(row=0,column=0,pady=10,sticky="w")
                
                RiPatientid=StringVar()
                Patientid=Entry(framerinfocenter,textvariable=RiPatientid,font=("calibri",20,"bold"))
                Patientid.grid(row=0,column=1,padx=1,pady=17,sticky="w")
                
                labelPatientid=Label(framerinfocenter,text="",bg="lightgreen",font=("calibri",20,"bold"))
                labelPatientid.grid(row=0,column=2,sticky="e")

                labelName=Label(framerinfocenter,text="Name:       ",bg="lightgreen",font=("calibri",20,"bold"))
                labelName.grid(row=1,column=0,padx=0,pady=17,sticky="w")

                RiName=StringVar()
                Name=Entry(framerinfocenter,textvariable=RiName,font=("calibri",20,"bold"))
                Name.grid(row=1,column=1)

                GenderRi=StringVar()
                GenderRi.set("")

                labelGender=Label(framerinfocenter,text="Gender:        ",bg="lightgreen",font=("calibri",20,"bold"))
                labelGender.grid(row=2,column=0)
                        
                i= IntVar()
                r1 = Radiobutton(framerinfocenter,text="male",value=1,variable=GenderRi,bg="lightgreen",font=("calibri",20,"bold"))
                r2 = Radiobutton(framerinfocenter,text="female",value=2,variable=GenderRi,bg="lightgreen",font=("calibri",20,"bold"))
                r1.grid(row=2,column=1,sticky="w")
                r2.grid(row=2,column=1,sticky="e",padx=0)


                



                labelAge=Label(framerinfocenter,text="Age:         ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAge.grid(row=3,column=0,sticky="w",padx=0,pady=17)

                RiAge=StringVar()
                Age=Entry(framerinfocenter,textvariable=RiAge,font=("calibri",20,"bold"))
                Age.grid(row=3,column=1)

                labelPhone=Label(framerinfocenter,text="Phone:     ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPhone.grid(row=4,column=0,sticky="w",padx=0,pady=17)

                RiPhone=StringVar()
                Phone=Entry(framerinfocenter,textvariable=RiPhone,font=("calibri",20,"bold"))
                Phone.grid(row=4,column=1)

                labelAddress=Label(framerinfocenter,text="Address:  ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAddress.grid(row=5,column=0,sticky="w",padx=0,pady=17)

                RiAddress=StringVar()
                Address=Entry(framerinfocenter,textvariable=RiAddress,font=("calibri",20,"bold"))
                Address.grid(row=5,column=1)

                labelDisease=Label(framerinfocenter,text="Disease:   ",bg="lightgreen",font=("calibri",20,"bold"))
                labelDisease.grid(row=6,column=0,sticky="w",padx=0,pady=17)

                RiDisease=StringVar()
                Disease=Entry(framerinfocenter,textvariable=RiDisease,font=("calibri",20,"bold"))
                Disease.grid(row=6,column=1)

                labelCheckIn=Label(framerinfocenter,text="Check In",bg="lightgreen",font=("calibri",20,"bold"))
                labelCheckIn.grid(row=7,column=0,sticky="w",padx=0,pady=17)

                RiCheckIn=StringVar()
                CheckIn=Entry(framerinfocenter,textvariable=RiCheckIn,font=("calibri",20,"bold"))
                CheckIn.grid(row=7,column=1)

                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_rowconfigure(4,weight=1)
                root.grid_rowconfigure(5,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)

                framerinforight=Frame(framerinfo,height="60",width="300",bg="lightgreen",relief="solid",borderwidth=2)
                framerinforight.pack(side=RIGHT,fill=Y);

                labelDoctorname=Label(framerinforight,text="Blood Group",bg="lightgreen",font=("calibri",17,"bold"))
                labelDoctorname.pack(padx=80,pady=10)

                RiBloodgroup=StringVar()
                Bloodgroup=Entry(framerinforight,textvariable=RiBloodgroup  ,width="20",font=("calibri",17,"bold"))
                Bloodgroup.pack()

                labelDoctorname=Label(framerinforight,text="Doctor Name",bg="lightgreen",font=("calibri",17,"bold"))
                labelDoctorname.pack(padx=80,pady=10)

                RiDoctorname=StringVar()
                Doctorname=Entry(framerinforight,textvariable=RiDoctorname  ,width="20",font=("calibri",17,"bold"))
                Doctorname.pack()

                labelDoctorname=Label(framerinforight,text="Room No",bg="lightgreen",font=("calibri",17,"bold"))
                labelDoctorname.pack(padx=80,pady=10)

                RiRoomNo=StringVar()
                RoomNo=Entry(framerinforight,textvariable=RiRoomNo,width="20",font=("calibri",17,"bold"))
                RoomNo.pack()

                Updatebutton=Button(framerinforight,text="Update",command=Riupdate,bg="yellow",bd=7,font=("calibri",15,"bold"))
                Updatebutton.pack(side=RIGHT,padx=35,pady=100);

        def home():
            global framemenuimage
            global framehome
            global frameprintbill
            global framereceiptimage
            global imagehome
            global imagemenu
            global framereceipt
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framemenuroot
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framedoctorrecord
            global framebill
            global PrPatientid
            global PrName
            global GenderPr
            global PrAge
            global PrPhone
            global PrAddress
            global PrDisease
            global PrCheckIn
            global PrBloodgroup
            global PrDoctorname
            global PrRoomNo

            global counterhome
            global counterpreg
            global counterlogin
            global counterrinfo
            global counterpadmit
            global counterainfo
            global countersreg
            global counterrrecord
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            counterhome+=1
            counterrinfo=0
            counterlogin=0
            counterpadmit=0
            counterainfo=0
            countersreg=0
            countersinfo=0
            counterrrecord=0
            counterbill=0
            counterdrecord=0
            counterpreg=0
            counterreceipt=0
            counterprintbill=0

            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                frame1.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
                framedoctorrecord.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            if counterhome==1:
                framehome=Frame(root,bg="pink")
                framehome.pack(side=TOP,fill=BOTH,expand=True); 

                imagehome=PhotoImage(file="f.png")
                label=ttk.Label(framehome,image=imagehome)
                label.pack(side=LEFT,fill=BOTH,expand=True)

        def Receipt():
            global framemenuimage
            global framehome
            global frameprintbill
            global BlIdentity
            global BlName
            global GenderBl
            global BlAge
            global BlDisease
            global BlPhone
            global BlAddress
            global BlDoctorname
            global BlDoctorcharges
            global BlLabtest
            global TreatmentchargesBl
            global BlProcedurecharges
            global BlOthercharges
            global BlMiscellaneouscharges
            global BlRoomcharges
            global BlTotal
            global framereceiptimage
            global receiptimage
            global receiptimager
            global imagemenu
            global framereceipt
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framemenuroot
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framedoctorrecord
            global framebill

            global counterpreg
            global counterhome
            global counterlogin
            global counterrinfo
            global counterpadmit
            global counterainfo
            global countersreg
            global counterrrecord
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            counterreceipt+=1
            counterhome=0
            counterrinfo=0
            counterlogin=0
            counterpadmit=0
            counterainfo=0
            countersreg=0
            countersinfo=0
            counterrrecord=0
            counterbill=0
            counterdrecord=0
            counterpreg=0
            counterprintbill=0




            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                frame1.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
                framedoctorrecord.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            if counterreceipt==1:
                framereceiptimage=Frame(root,bg="lightgreen")
                framereceiptimage.pack(side=TOP,fill=X)

                receiptimage=PhotoImage(file="vyas.png")
                label=ttk.Label(framereceiptimage,image=receiptimage)
                label.grid(row=0,column=0)


                label=Label(framereceiptimage,text="NH-62, Pali Road,Kudi Haud, Jodhpur Rajasthan",font=("calibri",15,"bold"),bg="lightgreen")
                label.grid(row=0,column=1,padx=200)



                receiptimager=PhotoImage(file="z.png")
                label=ttk.Label(framereceiptimage,image=receiptimager)
                label.grid(row=0,column=2)

                framereceipt=Frame(root,bg="lightgreen")
                framereceipt.pack(side="top",fill=BOTH,expand=True)

                

                framereceipttop=Frame(framereceipt,bg="lightgreen",height=20)
                framereceipttop.pack(side=TOP,fill=X)

                labelreceipt=Label(framereceipttop,text="Receipt :-",bg="lightgreen",fg="black",font=('arial',20,'bold'))
                labelreceipt.pack(side=LEFT,padx=150,pady=10)

                txtReceipt=Text(framereceipt,width=65,height=12,bg='white',bd=4,font=('arial',12,'bold'))
                txtReceipt.pack(anchor="nw",padx=100)

                txtReceipt.insert(END,'Patient id:\t\t\t'+PrPatientid.get() +'\n')
                txtReceipt.insert(END,'Name:\t\t\t' + PrName.get() +'\n')
                txtReceipt.insert(END,'Gender:\t\t\t'+ GenderPr.get()+'\n')
                txtReceipt.insert(END,'Age:\t\t\t'+ PrAge.get()+'\n')
                txtReceipt.insert(END,'Phone No:\t\t\t'+ PrPhone.get()+'\n')
                txtReceipt.insert(END,'Address:\t\t\t'+ PrAddress.get()+'\n')
                txtReceipt.insert(END,'Disease:\t\t\t'+ PrDisease.get()+'\n')
                txtReceipt.insert(END,'Check In:\t\t\t'+ PrCheckIn.get()+'\n')
                txtReceipt.insert(END,'Bloodgroup:\t\t\t'+ PrBloodgroup.get()+'\n')
                txtReceipt.insert(END,'Doctor Name:\t\t\t'+ PrDoctorname.get()+'\n')
                txtReceipt.insert(END,'Room No:\t\t\t'+ PrRoomNo.get()+'\n')

                labelreceipt=Label(framereceipt,text="Medicine: - ",fg="black",bg="lightgreen",font=('arial',20,'bold'))
                labelreceipt.pack(anchor="nw",padx=150,pady=10)

        def printbill():
            global framemenuimage
            global framehome
            global frameprintbill
            global BlIdentity
            global BlName
            global GenderBl
            global BlAge
            global BlDisease
            global BlPhone
            global BlAddress
            global BlDoctorname
            global BlDoctorcharges
            global BlLabtest
            global TreatmentchargesBl
            global BlProcedurecharges
            global BlOthercharges
            global BlMiscellaneouscharges
            global BlRoomcharges
            global BlTotal
            global framereceiptimage
            global receiptimage
            global receiptimager
            global imagemenu
            global framereceipt
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framemenuroot
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framedoctorrecord
            global framebill
            global frameprintbill

            global counterpreg
            global counterhome
            global counterlogin
            global counterrinfo
            global counterpadmit
            global counterainfo
            global countersreg
            global counterrrecord
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            counterprintbill+=1
            counterhome=0
            counterrinfo=0
            counterlogin=0
            counterpadmit=0
            counterainfo=0
            countersreg=0
            countersinfo=0
            counterrrecord=0
            counterbill=0
            counterdrecord=0
            counterpreg=0
            counterreceipt=0

            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                frame1.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
                framedoctorrecord.destroy()
            except:
                pass
            try:
                framepatientregistration.destroy()
            except:
                pass
            if counterprintbill==1:
                frameprintbill=Frame(root,bg="lightgreen")
                frameprintbill.pack(side="top",fill=BOTH,expand=True)

                txtReceipt=Text(frameprintbill,width=100,height=17,bg='white',bd=4,font=('arial',12,'bold'))
                txtReceipt.pack(anchor="nw",padx=100)

                txtReceipt.insert(END,'Patient id:-\t\t\t'+BlIdentity.get() + '\t\t\t' +'Name:-\t\t\t' + BlName.get() +'\n')
                txtReceipt.insert(END,'Gender:-\t\t\t'+ GenderBl.get()+ '\t\t\t' +'Age:-\t\t\t'+ BlAge.get()+'\n')
                txtReceipt.insert(END,'Disease:-\t\t\t'+ BlDisease.get()+ '\t\t\t' +'Phone No:-\t\t\t'+ BlPhone.get()+'\n')
                txtReceipt.insert(END,'Address:-\t\t\t'+ BlAddress.get()+ '\t\t\t' +'Doctor name:-\t\t\t'+ BlDoctorname.get()+'\n'+'\n')
                txtReceipt.insert(END,'Doctor Charges:\t\t\t'+BlDoctorcharges.get() +'\n')
                txtReceipt.insert(END,'Lab Test:-\t\t\t' + BlLabtest.get() +'\n')
                txtReceipt.insert(END,'Treatment Charges:-\t\t\t'+ TreatmentchargesBl.get()+'\n')
                txtReceipt.insert(END,'Procedure Charges:-\t\t\t'+ BlProcedurecharges.get()+'\n')
                txtReceipt.insert(END,'Other Charges:-\t\t\t'+ BlOthercharges.get()+'\n')
                txtReceipt.insert(END,'Miscellaneous Charges:-\t\t\t'+ BlMiscellaneouscharges.get()+'\n')
                txtReceipt.insert(END,'Room Charges:-\t\t\t'+ BlRoomcharges.get()+'\n')
                txtReceipt.insert(END,'Total:-\t\t\t'+ BlTotal.get()+'\n')
                
                



        def preg():
            global framemenuimage
            global framehome
            global frameprintbill
            global imagemenu
            global framereceiptimage
            global framereceipt
            global framepatientregistration
            global framepatientadmit
            global framerinfo
            global frameainfo
            global framemenuroot
            global framestaffregistration
            global framestaffinformation
            global framerrecord
            global framedoctorrecord
            global framebill
            global PrPatientid
            global PrName
            global GenderPr
            global PrAge
            global PrPhone
            global PrAddress
            global PrDisease
            global PrCheckIn
            global PrBloodgroup
            global PrDoctorname
            global PrRoomNo

            global counterpreg
            global counterhome
            global counterlogin
            global counterrinfo
            global counterpadmit
            global counterainfo
            global countersreg
            global counterrrecord
            global counterbill
            global counterdrecord
            global counterreceipt
            global counterprintbill

            counterpreg+=1
            counterhome=0
            counterrinfo=0
            counterlogin=0
            counterpadmit=0
            counterainfo=0
            countersreg=0
            countersinfo=0
            counterrrecord=0
            counterbill=0
            counterdrecord=0
            counterreceipt=0
            counterprintbill=0

            try:
                framemenuimage.destroy()
            except:
                pass
            try:
                frameprintbill.destroy()
            except:
                pass
            try:
                frame1.destroy()
            except:
                pass
            try:
                framereceiptimage.destroy()
            except:
                pass
            try:
                framereceipt.destroy()
            except:
                pass
            try:
                framehome.destroy()
            except:
                pass
            try:
                framerinfo.destroy()
            except:
                pass
            try:
                framepatientadmit.destroy()
            except:
                pass
            try:
                frameainfo.destroy()
            except:
                pass
            try:
                framestaffregistration.destroy()
            except:
                pass
            try:
                framestaffinformation.destroy()
            except:
                pass
            try:
                framerrecord.destroy()
            except:
                pass
            try:
                framebill.destroy()
            except:
                pass
            try:
            	framedoctorrecord.destroy()
            except:
            	pass
         

            if counterpreg==1:
                framepatientregistration=Frame(root,width=100,height=100,bg="lightgreen")
                framepatientregistration.pack(side="right",fill=BOTH,expand=TRUE)

                framepatientregistrationtop=Frame(framepatientregistration,height="200",relief="solid",borderwidth=2,bg="sandybrown")
                framepatientregistrationtop.pack(side=TOP,fill=X);

                labelpatientregistrationtext=Label(framepatientregistrationtop,text="Patient Registration",bg="sandybrown",font=("calibri",23,"bold"))
                labelpatientregistrationtext.pack(anchor="center")

                framepatientregistrationcenter=Frame(framepatientregistration,bg="lightgreen",height="60",width="130",relief="solid",borderwidth=2)
                framepatientregistrationcenter.pack(side=LEFT,fill=BOTH,expand=True);

                labelPatientid=Label(framepatientregistrationcenter,bg="lightgreen",text="Patient ID:    ",font=("calibri",20,"bold"))
                labelPatientid.grid(row=0,column=0,padx=90,pady=10,sticky="w")
                
                PrPatientid=StringVar()
                Patientid=Entry(framepatientregistrationcenter,textvariable=PrPatientid,font=("calibri",20,"bold"))
                Patientid.grid(row=0,column=1,padx=1,pady=17,sticky="w")
                
                labelName=Label(framepatientregistrationcenter,text="Name:       ",bg="lightgreen",font=("calibri",20,"bold"))
                labelName.grid(row=1,column=0,padx=90,pady=17,sticky="w")

                PrName=StringVar()
                Name=Entry(framepatientregistrationcenter,textvariable=PrName,font=("calibri",20,"bold"))
                Name.grid(row=1,column=1)

                GenderPr=StringVar()
                GenderPr.set("")

                labelGender=Label(framepatientregistrationcenter,text="Gender:    ",bg="lightgreen",font=("calibri",20,"bold"))
                labelGender.grid(row=2,column=0,sticky="w",padx=90)
                        
                i= IntVar()
                r1 = Radiobutton(framepatientregistrationcenter,text="male",value="Male",bg="lightgreen",variable=GenderPr,font=("calibri",20,"bold"))
                r2 = Radiobutton(framepatientregistrationcenter,text="female",value="Female",bg="lightgreen",variable=GenderPr,font=("calibri",20,"bold"))
                r1.grid(row=2,column=1,sticky="w")
                r2.grid(row=2,column=1,sticky="e",padx=0)




                labelAge=Label(framepatientregistrationcenter,text="Age:         ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAge.grid(row=3,column=0,sticky="w",padx=90,pady=17)

                PrAge=StringVar()
                Age=Entry(framepatientregistrationcenter,textvariable=PrAge,font=("calibri",20,"bold"))
                Age.grid(row=3,column=1)

                labelPhone=Label(framepatientregistrationcenter,text="Phone:     ",bg="lightgreen",font=("calibri",20,"bold"))
                labelPhone.grid(row=4,column=0,sticky="w",padx=90,pady=17)

                PrPhone=StringVar()
                Phone=Entry(framepatientregistrationcenter,textvariable=PrPhone,font=("calibri",20,"bold"))
                Phone.grid(row=4,column=1)

                labelAddress=Label(framepatientregistrationcenter,text="Address:  ",bg="lightgreen",font=("calibri",20,"bold"))
                labelAddress.grid(row=5,column=0,sticky="w",padx=90,pady=17)

                PrAddress=StringVar()
                Address=Entry(framepatientregistrationcenter,textvariable=PrAddress,font=("calibri",20,"bold"))
                Address.grid(row=5,column=1)

                labelDisease=Label(framepatientregistrationcenter,text="Disease:   ",bg="lightgreen",font=("calibri",20,"bold"))
                labelDisease.grid(row=6,column=0,sticky="w",padx=90,pady=17)

                PrDisease=StringVar()
                Disease=Entry(framepatientregistrationcenter,textvariable=PrDisease,font=("calibri",20,"bold"))
                Disease.grid(row=6,column=1)

                labelCheckIn=Label(framepatientregistrationcenter,text="Check IN",bg="lightgreen",font=("calibri",20,"bold"))
                labelCheckIn.grid(row=7,column=0,sticky="w",padx=90,pady=17)


                CheckIn=Entry(framepatientregistrationcenter,textvariable=PrCheckIn,font=("calibri",20,"bold"))
                CheckIn.grid(row=7,column=1)

                root.grid_rowconfigure(0,weight=1)
                root.grid_rowconfigure(1,weight=1)
                root.grid_rowconfigure(2,weight=1)
                root.grid_rowconfigure(3,weight=1)
                root.grid_rowconfigure(4,weight=1)
                root.grid_rowconfigure(5,weight=1)
                root.grid_rowconfigure(6,weight=1)
                root.grid_columnconfigure(0,weight=1)
                root.grid_columnconfigure(1,weight=1)

                framepatientregistrationright=Frame(framepatientregistration,height="60",width="300",bg="lightgreen",relief="solid",borderwidth=2)
                framepatientregistrationright.pack(side=RIGHT,fill=Y);

                labelBloodgroup=Label(framepatientregistrationright,text="Blood Group",bg="lightgreen",font=("calibri",17,"bold"))
                labelBloodgroup.pack(pady=10)

                PrBloodgroup=StringVar()
                Bloodgroup=Entry(framepatientregistrationright,textvariable=PrBloodgroup    ,width="20",font=("calibri",17,"bold"))
                Bloodgroup.pack()

                labelDoctorname=Label(framepatientregistrationright,text="Doctor Name",bg="lightgreen",font=("calibri",17,"bold"))
                labelDoctorname.pack(pady=10)

                PrDoctorname=StringVar()
                Doctorname=Entry(framepatientregistrationright,textvariable=PrDoctorname    ,width="20",font=("calibri",17,"bold"))
                Doctorname.pack()

                labelRoomNo=Label(framepatientregistrationright,text="Room No.",bg="lightgreen",font=("calibri",17,"bold"))
                labelRoomNo.pack(pady=10)

                PrRoomNo=StringVar()
                RoomNo=Entry(framepatientregistrationright,textvariable=PrRoomNo,width="20",font=("calibri",17,"bold"))
                RoomNo.pack(padx=5)

                ADDAbutton=Button(framepatientregistrationright,text="ADD",command=Pradd,bg="yellow",width=10,bd=7,font=("calibri",15,"bold"))
                ADDAbutton.pack(side=LEFT,padx=5);

                buttonprintreg=Button(framepatientregistrationright,text="Receipt",command=Receipt,bg="yellow",width=10,bd=7,font=("calibri",15,"bold"))
                buttonprintreg.pack(side=LEFT,padx=5)

        framemenuroot=Frame(root,height="190",bg="lightgreen")
        framemenuroot.pack(side=TOP,fill=X);
        framehospitalname=Label(framemenuroot,text="                                  VYAS HOSPITAL",bg="lightgreen",fg="red",width="35",font=("calibri",27,"bold"))
        framehospitalname.pack(anchor="center")


        framemenuimage=Frame(root)
        framemenuimage.pack(side=RIGHT)

        imagemenu=PhotoImage(file="f.png",height="1200",width="1030")
        label=ttk.Label(framemenuimage,image=imagemenu)
        label.pack(side=RIGHT,fill=BOTH,expand=True)

         


        framemenubackground=Frame(root,bg="lightgreen",height="60",width="50")
        framemenubackground.pack(side=LEFT,fill=Y);
        framemenuheading=Label(framemenubackground,text="Menu",fg="White",bg="sandybrown",width="25",font=("calibri",18,"bold"))
        framemenuheading.pack(anchor="nw")

        Buttonpatienthome=Button(framemenubackground,text="Home",command=home,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        Buttonpatienthome.pack(side="top",fill=X)

        Buttonpatientregistration=Button(framemenubackground,text="Patient Registration",command=preg,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        Buttonpatientregistration.pack(side="top",fill=X)

        Buttonpatientinformation=Button(framemenubackground,text="Patient Admit",command=padmit,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        Buttonpatientinformation.pack(side="top",fill=X)

        Buttonregistrationinfo=Button(framemenubackground,text="Registration Information",command=rinfo,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        Buttonregistrationinfo.pack(side="top",fill=X)

        Buttonadmitinformation=Button(framemenubackground,text="Admit Information",command=ainfo,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        Buttonadmitinformation.pack(side="top",fill=X)

        Buttonstaffregistration=Button(framemenubackground,text="Doctor Registration",command=sreg,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        Buttonstaffregistration.pack(side="top",fill=X)

        Buttonstaffinformation=Button(framemenubackground,text="Doctor Information",command=sinfo,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        Buttonstaffinformation.pack(side="top",fill=X)

        ButtonRegistrationRecord=Button(framemenubackground,text="Registration Record",command=RRecord,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        ButtonRegistrationRecord.pack(side="top",fill=X)

        ButtonStaffRecord=Button(framemenubackground,text="Doctor Record",command=drecord,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        ButtonStaffRecord.pack(side="top",fill=X)

        ButtonBill=Button(framemenubackground,text="Generate Bill",command=Bill,bd=7,bg="sandybrown",font=("calibri",14,"bold"))
        ButtonBill.pack(side="top",fill=X)


    else:
        messagebox.showinfo("INVALID USERNAME OR PASSWORD ", "YOU HAVE ENTERED INVALID USERNAME OR PASSWORD  ")
        usernameVar.delete(0,END)
        passwordVar.delete(0,END)



def exit():
    if messagebox.askyesno("Confirm","Are you Sure,you want to exit"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW",exit)



frame1=Frame(root,height="500",width=500,bg="pink")
frame1.pack(side=TOP,fill=X);

C = Canvas(frame1,bg="blue", height=900,width=800)
filename = PhotoImage(file="f.png")
background_label = Label(frame1, image=filename)
background_label.place(x=0,y=0,relwidth=1, relheight=1)




userright=Frame(frame1,height="400",width="400",bg="pink",relief="solid",borderwidth=2)
userright.pack(side=RIGHT,padx="200")

usernullframe=Frame(userright,height="50",bg="pink")
usernullframe.pack(side=TOP)

image1=PhotoImage(file="ee.png")
label=Label(userright,image=image1,width=150,height=150,bg="pink")
label.pack(side=LEFT,padx=10)


labelUsername=Label(userright,text="Username:",font=("calibri",18,"bold"),bg="pink")
labelUsername.pack(anchor="nw",padx=10)
usernameVar=StringVar()
UsernameEntry=Entry(userright,font=("calibri",14,"bold"),textvariable=usernameVar)
UsernameEntry.pack(anchor="nw",padx=10)

labelPassword=Label(userright,text="Password:",font=("calibri",18,"bold"),bg="pink")
labelPassword.pack(anchor="nw",padx=10)

passwordVar=StringVar()
userEntry=Entry(userright)
Passwordentry=Entry(userright,show="*",font=("calibri",14,"bold"),textvariable=passwordVar)
Passwordentry.pack(anchor="nw",padx=10)




buttonok=Button(userright,text="LOGIN",bg="orange",height=2,width=6,bd=3,font=("calibri",12,"bold"),command=login)
buttonok.pack(side=LEFT,padx="10",pady="10")

buttonexit=Button(userright,text="EXIT",bg="orange",height=2,width=6,bd=3,font=("calibri",12,"bold"),command=exit)
buttonexit.pack(side=RIGHT,padx="10",pady="10")


C.pack()


try:
    connection=sqlite3.connect("YASH.db")
    cursor=connection.cursor()

    query="CREATE TABLE sr (SrID text,SrName text,GenderSr text,SrPosition text,SrDepartment text,SrMailid text,SrSalary text,SrPhone text,SrAddress text)"
    cursor.execute(query)
    connection.commit()
except:
    pass

try:	
    connection=sqlite3.connect("YASH.db")
    cursor=connection.cursor()

    query="CREATE TABLE pa (PaPatientid text,PaName text,GenderPa text,PaAge text,PaPhone text,PaAddress text,PaDisease text,PaCheckIn text,PaBloodgroup text,PaDoctorname text,PaCheckOut text,PaRoomNo text,PaRoomtype text,PaPrice text)"
    cursor.execute(query)
    connection.commit()
except:
    pass


try:
    connection=sqlite3.connect("YASH.db")
    cursor=connection.cursor()

    query="CREATE TABLE pr (PrPatientid text,PrName text,GenderPr text,PrAge text,PrPhone text,PrAddress text,PrDisease text,PrCheckIn text,PrBloodgroup text,PrDoctorname text,PrRoomNo text)"
    cursor.execute(query)
    connection.commit()
except:
    pass

root.mainloop()