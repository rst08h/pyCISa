import sqlite3 
import pandas as pd
from tkinter import filedialog as fd

def btn_upload():
    print("upload")
    cisfile=fd.askopenfilename()
    #เปิดไฟล์ด้วย panda    

    #cisfile='ALL_CUSTOMER1205.xlsx'

    xl=pd.ExcelFile(cisfile)
    xl.sheet_names
    if xl.sheet_names[0] == 'ผู้ใช้น้ำทั้งหมด':
        print("ok ผู้ใช้น้ำทั้งหมด")
        dtypes={'ประเภท':'category'
        }
        df=pd.read_excel(cisfile,xl.sheet_names[0],dtype=dtypes)
        conn=sqlite3.connect('userinfo/info.sqlite3')
        c = conn.cursor()
        df.to_sql('ALL_CUSTOMER', conn, if_exists='replace', index = False) 
        conn.commit()
        conn.close()