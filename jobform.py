import pandas as pd
import numpy as np
#from openpyxl.workbook import workbook as wb #แก้ไข ms excel
#from openpyxl import worksheet as ws #แก้ไข ms excel
from docxtpl import DocxTemplate #แก้ไข ms word
from tkinter import *
import tkinter.ttk as ttk
from ttkbootstrap.constants import *
import ttkbootstrap as ttb
from datetime import datetime

qrdata = ''
def cmdsearch():
    global qrdata, qrframe, filter1, showdata
    if serial_box.get() != '':
        errmessage.config(text=serial_box.get(), foreground='green')
        df = pd.read_excel('D:\\Github Repository\\unclechangit\\excel\\Otherasset2.xlsx', 
                           usecols=['Serial_Number','Owner_Name','Department','Site_Owner_Name',
                                    'Status_OtherAsset','Model','Manufacturer','Warranty_Start_Date','Warranty_End_Date'])
        
                # รับ input จาก textbox(Entry)
        filter1 = serial_box.get().strip() # stripเป็นการตัดช่องว่างหน้าหลัง
        qrdata = df.query('Serial_Number == @filter1')
        
        # แสดงข้อมูลจาก qrdata ด้วย treeview
        # กำหนดหัว coloumn
        columntree = ('Serial_Number','Status_OtherAsset','Manufacturer','Model','Owner_Name','Department','Warranty_Start_Date','Warranty_End_Date','Site_Owner_Name','Warranty Status')
        treevi = ttb.Treeview(fram_data, show='headings', columns=columntree, height=5, padding=5)
        treevi.heading('Serial_Number', text='Serial Number')
        treevi.heading('Status_OtherAsset', text='Status_OtherAsset')
        treevi.heading('Owner_Name', text='Owner Name')
        treevi.heading('Department', text='Department')
        treevi.heading('Site_Owner_Name', text='Site Owner Name')
        treevi.heading('Model', text='Model')
        treevi.heading('Manufacturer', text='Manufacturer')
        treevi.heading('Warranty_Start_Date', text='Warranty_Start_Date')
        treevi.heading('Warranty_End_Date', text='Warranty_End_Date')
        #treevi.heading('Warranty_Status', text='Warranty_Status')

        # กำหนดความกว้างของ column
        treevi.column(0, anchor='center', stretch=NO, width=90)
        treevi.column(1, anchor='center', stretch=NO, width=90)
        treevi.column(2, anchor='center', stretch=NO, width=90)
        treevi.column(3, anchor='center', stretch=NO, width=90)
        treevi.column(4, anchor='center', stretch=NO, width=130)
        treevi.column(5, anchor='center', stretch=NO, width=130)
        treevi.column(6, anchor='center', stretch=NO, width=130)
        treevi.column(7, anchor='center', stretch=NO, width=130)
        treevi.column(8, anchor='center', stretch=NO, width=180)
        #treevi.column(9, anchor='center', stretch=NO, width=180)

        style = ttk.Style()
        style.configure('Treeview.Heading', background='darkblue')
        
        # insert to tree view
        for item in qrdata.values:
            treevi.insert("", 'end',text='', values=(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8]))
        treevi.grid(row=2, column=0, padx=10, pady=10, columnspan=True)
        btn_preview.config(state='enable')
    else:
        errmessage.config(text='Please enter Serial Number', foreground='red')

    
    

# -----------------------------------------------------------------------------------------------------------------
# create preview data from preview button
def previewdata():
    print('dfsdsdsdfsdfdsfdsfsdfsdfsdfsdfsd')


root = ttb.Window(themename='superhero')
root.title('ระบบออกใบแจ้งงาน')
root.geometry('1200x720')

frame_search = ttb.Frame(root,width=500, height=50, borderwidth=10, padding=5 , relief=GROOVE)
lbl_serial = ttb.Label(frame_search, text='Serial Number : ', bootstyle="success")
lbl_serial.grid(row=0, column=0, padx=10, pady=10)
# เพิ่ม textbox รับค่า serial number
serial_box = ttb.Entry(frame_search)
serial_box.grid(row=0, column=1, padx=10, pady=10)
# เพิ่มปุ่ม search
btn_search = ttb.Button(frame_search, text='Search', bootstyle="success,outline", command=cmdsearch)
btn_search.grid(row=0, column=2, padx=10)

btn_preview = ttb.Button(frame_search, text=' Preview ', bootstyle="success,outline", state='disable', command = lambda:previewdata())
btn_preview.grid(row=0, column=5, pady=5, padx=700, columnspan=50)

frame_search.pack(side='top', fill='both', padx=5, pady=5)
#end of search frame

fram_data = ttb.Frame(root, width=1100, height=100, borderwidth=10, padding=10 , relief=GROOVE)
fram_data.pack(side='top', fill='both', expand=True, padx=5, pady=5)

#frame_preview = ttb.Frame(root, width=500, height=50, borderwidth=1, relief=GROOVE)    
#btn_preview = ttb.Button(frame_preview, text=' Preview ', bootstyle="success,outline", command = lambda:previewdata())
#btn_preview.grid(row=0, column=0, pady=5, padx=5)
#frame_preview.pack(side='right', padx=5, pady=2, fill='none', expand=True)

# error message label
errmessage = ttb.Label(frame_search, text='')
errmessage.grid(row=0, column=4)



root.mainloop()
