import pandas as pd
import numpy as np
#from openpyxl.workbook import workbook as wb #แก้ไข ms excel
#from openpyxl import worksheet as ws #แก้ไข ms excel
from docxtpl import DocxTemplate #แก้ไข ms word
from tkinter import *
import tkinter.ttk as ttk
from ttkbootstrap.constants import *
import ttkbootstrap as ttb

qrdata = ''
def cmdsearch():
    global qrdata, qrframe, filter1, showdata
    if serial_box.get() != '':
        errmessage.config(text=serial_box.get(), foreground='green')
        df = pd.read_excel('D:\\Github Repository\\unclechangit\\excel\\Otherasset2.xlsx', index_col='Serial_Number', usecols=['Serial_Number','Owner_Name','Department','Site_Owner_Name'])
        filter1 = serial_box.get()
        qrdata = df.query('Serial_Number == @filter1')
        
    else:
        errmessage.config(text='Please enter Serial Number', foreground='red')
        

root = ttb.Window(themename='vapor')
root.title('ระบบออกใบแจ้งงาน')
root.geometry('1080x720')

frame_search = ttb.Frame(root,width=50, height=50, borderwidth=10, padding=5 , relief=GROOVE)
lbl_serial = ttb.Label(frame_search, text='Serial Number : ', bootstyle="success")
lbl_serial.grid(row=0, column=0, padx=10, pady=10)

serial_box = ttb.Entry(frame_search)
serial_box.grid(row=0, column=1, padx=10, pady=10)

btn_search = ttb.Button(frame_search, text='Search', bootstyle="success,outline", command=cmdsearch)
btn_search.grid(row=0, column=2, padx=10)
frame_search.pack(side='top', fill='both', padx=5, pady=5)

fram_data = ttb.Frame(root, width=650, height=410, borderwidth=10, padding=10 , relief=GROOVE)
lbl2 = ttb.Label(fram_data, text='Serial Number')
lbl2.grid(row=1, column=1, padx=20)
lbl3 = ttb.Label(fram_data, text='User ID')
lbl3.grid(row=1, column=2, padx=20)
lbldata = ttb.Label(fram_data,text=qrdata)
lbldata.grid(row=2, column=1)
fram_data.pack(side='left', fill='both', expand=True, padx=5, pady=5)

# error message label
errmessage = ttb.Label(frame_search, text='')
errmessage.grid(row=0, column=4)



root.mainloop()
