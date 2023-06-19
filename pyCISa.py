import tkinter as tk
import tkinter.font as tkFont

table_neme=('1. ผู้ใช้น้ำทั้งหมด',
            '2. การรับเงินค่าติดตั้ง',
            '3. การรับเงินรายได้ค่าน้ำ',
            '4. รายได้อื่น ๆ',
            '_4.1 เกียวกับผู้ใช้น้ำ',
            '_4.2 ไม่เกี่ยวกับผู้ใช้น้ำ',
            '5. ฝากมาตรครบกำหนด',
            '6. ทะเบียนคุมน้ำท่อธาร',
            '7. ตั้งหนี้ประจำเดือน',
            '_7.1 ตั้งหนี้ประจำเดือน',
            '_7.2 ตั้งหนี้ผู้ใช้น้ำ',
            '8. หลักประกันสัญญา',
            '9. หนี้ค้างชำระ',
            '11. ประวัติการเปลี่ยนสถานะมาตร',
            '12. มาตรตาย',
            '13. ยกเลิกใบเสร็จรับเงินค่าน้ำ')

table_status=[]

frmMain=tk.Tk()
frmMain.title("pyCISa")
#tk.Label(image=tk.PhotoImage(file="pwalogo.png")).grid(row=0,column=0)
panel_Lmenu=tk.Frame()
panel_Lmenu.pack(side="left",fill='y')
tk.Label(text="โปรแกรมสนับสนุนงานตรวจสอบระบบสารสนเทศด้านผู้ใช้น้ำ (CIS)",font=tkFont.Font(size=20)).pack()
panel_line1=tk.Frame()
panel_line1.pack(fill='x')
panel_line2=tk.Frame()
panel_line2.pack(fill='x')
panel_status=tk.Frame(bg='khaki1')
panel_status.pack(side="left",fill='y')
panel_workingpaper=tk.Frame(highlightbackground='brown2',highlightthickness=1)
panel_workingpaper.pack(side="left",fill='both')
panel_Rmenu=tk.Frame(bg='magenta')
panel_Rmenu.pack(side="right",fill='y')

#เมนูซ้าย


#บันทัดแรก
tk.Label(panel_line1,text="ชื่อหน่วยรับตรวจ").pack(side="left")
tk.Entry(panel_line1).pack(side="left")
tk.Checkbutton(panel_line1).pack(side="left")
tk.Label(panel_line1,text="กปภ.เขต").pack(side="left")
tk.Label(panel_line1,text="ชื่อผู้จัดทำ").pack(side="left")
tk.Entry(panel_line1).pack(side="left")
tk.Label(panel_line1,text="วันที่จัดทำ").pack(side="left")
tk.Entry(panel_line1).pack(side="left")

#บันทัดสอง
tk.Label(panel_line2,text="งวดการตรวจสอบ วันที่").pack(side="left")
tk.Entry(panel_line2).pack(side="left")
tk.Label(panel_line2,text="ถึงวันที่").pack(side="left")
tk.Entry(panel_line2).pack(side="left")
tk.Label(panel_line2,text="ชื่อผู้สอบทาน").pack(side="left")
tk.Entry(panel_line2).pack(side="left")
tk.Label(panel_line2,text="วันที่สอบทาน").pack(side="left")
tk.Entry(panel_line2).pack(side="left")
tk.Checkbutton(panel_line2).pack(side="left")
tk.Label(panel_line2,text="ไม่ระบุวันที่").pack(side="left")

logo=tk.PhotoImage(file="pwalogo.png")
canvas=tk.Canvas(panel_Lmenu,width=100,height=100)
canvas.pack()
canvas.create_image(50,50,image=logo)

tk.Label(panel_Lmenu,text="BA 1211").pack()
tk.Button(panel_Lmenu,text="Upload").pack(side='bottom',fill='x')
tk.Button(panel_Lmenu,text="Credit").pack(side='bottom',fill='x')
tk.Button(panel_Lmenu,text="เว็บไซต์").pack(fill='x')

#สถานะข้อมูล
tk.Label(panel_status,text="สถานะข้อมูล",font=tkFont.Font(size=16),bg='khaki1').grid(row=0,column=0,columnspan=2)
tk.Label(panel_status,text="สถานะ",bg='khaki1').grid(row=1,column=1)
i=2
for tab in table_neme:
    if tab[0:1] == '_' :
        tk.Label(panel_status,text=tab[1:],bg='khaki1',justify='left').grid(row=i,column=0,sticky='w',padx=10) 
    else:
        tk.Label(panel_status,text=tab,bg='khaki1',justify='left').grid(row=i,column=0,sticky='w') 
    
    if (i != 5) and (i != 10) :
        tk.Label(panel_status,text="มี",fg='green',bg='khaki1').grid(row=i,column=1)
    
    i+=1


#กระดาษทำการ
tk.Label(panel_workingpaper,text="รายการกระดาษทำการ",font=tkFont.Font(size=16)).pack()
panel_workingpaperL=tk.Frame(panel_workingpaper)
panel_workingpaperL.pack(side='left')
panel_workingpaperR=tk.Frame(panel_workingpaper)
panel_workingpaperR.pack(side='right')

tk.Button(panel_workingpaperL,text='1. การขึ้นทะเบียนผู้ใช้น้ำรายใหม่').pack(fill='x')
tk.Button(panel_workingpaperL,text='2. คำนวณค่าน้ำ').pack(fill='x')
tk.Button(panel_workingpaperL,text='3. สิทธิส่วนลดค่าน้ำ').pack(fill='x')
tk.Button(panel_workingpaperL,text='4. มาตรตาย').pack(fill='x')
tk.Button(panel_workingpaperL,text='5. ปรับปรุงหนี้').pack(fill='x')
tk.Button(panel_workingpaperL,text='6. การสุ่มอ่านมาตรวัดน้ำ').pack(fill='x')
tk.Button(panel_workingpaperL,text='7. ท่อธาร').pack(fill='x')
tk.Button(panel_workingpaperL,text='8. รายได้อื่น ๆ เกี่ยวกับผู้ใช้น้ำ').pack(fill='x')
tk.Button(panel_workingpaperR,text='9. รายได้อื่น ๆ ไม่เกี่ยวกับผู้ใช้น้ำ').pack(fill='x')
tk.Button(panel_workingpaperR,text='10. ฝากมาตรวัดน้ำ').pack(fill='x')
tk.Button(panel_workingpaperR,text='11. กระทบยอดรายได้').pack(fill='x')
tk.Button(panel_workingpaperR,text='12. ยืนยันยอดค่าน้ำ').pack(fill='x')

tk.Button(panel_workingpaperR,text='13. หนี้ค้างชำระ').pack(fill='x')
tk.Button(panel_workingpaperR,text='14. การรับเงินค่าติดตั้ง').pack(fill='x')
tk.Button(panel_workingpaperR,text='15. หลักประกันสัญญา').pack(fill='x')


frmMain.mainloop()

