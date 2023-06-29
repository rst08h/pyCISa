import tkinter as tk
import tkinter.font as tkFont
import json
#from tkinter import ttk
from tkcalendar import Calendar,DateEntry
import cmd_upload
import pyCISa_misc as misc



userinfo = json.load(open('user.json',encoding='UTF-8'))

print(userinfo['user'])
print(userinfo['reviewer'])



table_status=[]

frmMain=tk.Tk()
frmMain.title("pyCISa")

# เมนูบาร์
menubar=tk.Menu(frmMain)
filemenu=tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='ใหม่...')
filemenu.add_command(label='เปิด...')
filemenu.add_command(label='บันทึก...')
filemenu.add_separator()
filemenu.add_command(label="ปิดโปรแกรม", command=frmMain.quit)
menubar.add_cascade(label="ไฟล์", menu=filemenu)

frmMain.config(menu=menubar)

#frmMain.geometry('2478x1381')
#frmMain.geometry('478x381')
#tk.Label(image=tk.PhotoImage(file="pwalogo.png")).grid(row=0,column=0)
panel_Lmenu=tk.Frame(padx=10,pady=10)
panel_Lmenu.pack(side="left",fill='y')

tk.Label(text="โปรแกรมสนับสนุนงานตรวจสอบระบบสารสนเทศด้านผู้ใช้น้ำ (CIS)",font=tkFont.Font(size=20)).pack()
panel_top=tk.Frame()
panel_top.pack(fill='x')
panel_topR=tk.Frame(panel_top)
panel_topR.pack(side='right')

panel_line1=tk.Frame(panel_top)
panel_line1.pack(fill='x')
panel_line2=tk.Frame(panel_top)
panel_line2.pack(fill='x')
panel_status=tk.Frame(bg='blanchedalmond',padx=10,pady=10,highlightbackground='black',highlightthickness=1)
panel_status.pack(side="left",fill='y')
panel_workingpaper=tk.Frame(highlightbackground='black',highlightthickness=1,padx=10,pady=10)
panel_workingpaper.pack(side='top')
panel_Rmenu=tk.Frame(bg='magenta')
panel_Rmenu.pack(side="right",fill='y')

#เมนูซ้าย



#บันทัดแรก
tk.Label(panel_line1,text="ชื่อหน่วยรับตรวจ").pack(side="left")
tk.Entry(panel_line1).pack(side="left")
tk.Checkbutton(panel_line1).pack(side="left")
tk.Label(panel_line1,text="กปภ.เขต").pack(side="left")
tk.Label(panel_topR,text="ชื่อผู้จัดทำ").grid(row=0,column=0)
tb_user=tk.Entry(panel_topR)
tb_user.grid(row=0,column=1)
tb_user.insert(0,userinfo['user'])
tk.Label(panel_topR,text="วันที่จัดทำ").grid(row=0,column=2)
tk.Entry(panel_topR).grid(row=0,column=3)

#บันทัดสอง
tk.Label(panel_line2,text="งวดการตรวจสอบ วันที่").pack(side="left")
tk.Entry(panel_line2).pack(side="left")
tk.Label(panel_line2,text="ถึงวันที่").pack(side="left")
tk.Entry(panel_line2).pack(side="left")
tk.Label(panel_topR,text="ชื่อผู้สอบทาน").grid(row=1,column=0)
tb_reviewer=tk.Entry(panel_topR)
tb_reviewer.grid(row=1,column=1)
tb_reviewer.insert(0,userinfo['reviewer'])
tk.Label(panel_topR,text="วันที่สอบทาน").grid(row=1,column=2)
tk.Entry(panel_topR).grid(row=1,column=3)
tk.Checkbutton(panel_topR).grid(row=1,column=4)
tk.Label(panel_topR,text="ไม่ระบุวันที่").grid(row=1,column=5)

logo=tk.PhotoImage(file="pwalogo.png")
canvas=tk.Canvas(panel_Lmenu,width=200,height=200)
canvas.pack()
canvas.create_image(50,50,image=logo)

tk.Label(panel_Lmenu,text="BA 1211").pack()
tk.Button(panel_Lmenu,text="Upload",command=cmd_upload.btn_upload).pack(side='bottom',fill='x')
tk.Button(panel_Lmenu,text="Credit",command=misc.credit).pack(side='bottom',fill='x')
tk.Button(panel_Lmenu,text="เว็บไซต์",command=misc.openweb).pack(fill='x')

#สถานะข้อมูล
tk.Label(panel_status,text="สถานะข้อมูล",font=tkFont.Font(size=16),bg='blanchedalmond').grid(row=0,column=0,columnspan=2)
tk.Label(panel_status,text="สถานะ",bg='blanchedalmond').grid(row=1,column=1)
i=2
for tab in misc.table_neme:
    if tab[0:1] == '_' :
        tk.Label(panel_status,text=tab[1:],bg='blanchedalmond',justify='left').grid(row=i,column=0,sticky='w',padx=10) 
    else:
        tk.Label(panel_status,text=tab,bg='blanchedalmond',justify='left').grid(row=i,column=0,sticky='w') 
    
    if (i != 5) and (i != 10) :
        tk.Label(panel_status,text="มี",fg='green',bg='blanchedalmond').grid(row=i,column=1)
    
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

cal=Calendar(locale="th_TH")
#cal.pack()

frmMain.mainloop()

