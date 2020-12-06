from tkinter import *
from beautifultable import BeautifulTable
h0=['Код валюти', 'Курс грн.', 'Курс грн.', 'Курс грн.', 'Рік']
h1 = ['---------', 'на 1.10', 'на 1.11', 'на 1.12', '---------']
h2 = ['103', '5,65', '6,05', '10,03', '2003']
h3 = ['104 ', '1,13', '1,23', '2,00', '2003']
h4 = ['105', '2,28', '2,52', '4,12', '2003']
h5 = ['106', '2,02', '2,24', '3,66', '2003']
h6 = ['109', '2,68', '3,18', '5,12', '2003']
h7 = ['111', '3,34', '3,96', '6,53', '2003']
h8 = ['103', '1,10', '11,21', '13,50', '2004']
h9 = ['104', '2,50', '2,60', '2,75', '2004']
h10 = ['105', '4,44', '4,65', '4,70', '2004']
h11 = ['106', '4,05', '4,25', '4,50', '2004']
h12 = ['109', '6,05', '6,30', '6,80', '2004']
h13 = ['111', '7,00', '7,25', '7,50', '2004']
h14 = ['103', '13,64', '13,70', '13,80', '2005']
h15 = ['104', '2,80', '2,83', '2,85', '2005']
h16 = ['105', '4,75', '4,80', '4,85', '2005']
h17 = ['106', '4,62', '4,64', '4,66', '2005']
h18 = ['109', '6,90', '6,95', '7,00', '2005']
h19 = ['111', '7,65', '7,75', '7,85', '2005']

ha0=['Курс грн.', 'Рік']
ha1 = ['на 1.10', '---']
ha2 = ['5,65', '2003']
ha3 = ['1,13', '2003']
ha4 = ['2,28', '2003']
ha5 = ['2,02', '2003']
ha6 = ['2,68', '2003']
ha7 = ['3,34', '2003']
ha8 = ['1,10', '2004']
ha9 = ['2,50', '2004']
ha10 = ['4,44', '2004']
ha11 = ['4,05', '2004']
ha12 = ['6,05', '2004']
ha13 = ['7,00', '2004']
ha14 = ['13,64', '2005']
ha15 = ['2,80', '2005']
ha16 = ['4,75', '2005']
ha17 = ['4,62', '2005']
ha18 = ['6,90', '2005']
ha19 = ['7,65', '2005']

table = BeautifulTable()
table.column_headers = h0
table.append_row(h1)
table.append_row(h2)
table.append_row(h3)
table.append_row(h4)
table.append_row(h5)
table.append_row(h6)
table.append_row(h7)
table.append_row(h8)
table.append_row(h9)
table.append_row(h10)
table.append_row(h11)
table.append_row(h12)
table.append_row(h13)
table.append_row(h14)
table.append_row(h15)
table.append_row(h16)
table.append_row(h17)
table.append_row(h18)
table.append_row(h19)

atable = BeautifulTable()
atable.column_headers = ha0
atable.append_row(ha1)
atable.append_row(ha2)
atable.append_row(ha3)
atable.append_row(ha4)
atable.append_row(ha5)
atable.append_row(ha6)
atable.append_row(ha7)
atable.append_row(ha8)
atable.append_row(ha9)
atable.append_row(ha10)
atable.append_row(ha11)
atable.append_row(ha12)
atable.append_row(ha13)
atable.append_row(ha14)
atable.append_row(ha15)
atable.append_row(ha16)
atable.append_row(ha17)
atable.append_row(ha18)
atable.append_row(ha19)

hb0 = ['Найменування валюти', 'Код валюти', 'Рік', 'Курс на 1.10', 'Курс крб. на 1.11', 'Рівень курсу на 1.11', 'Курс крб. на 1.12', 'Рівень курсу на 1.12', 'Рівень за три місяці']
hb1 = ['1 англійський фунт стерлінг', '103', '2003', '565,46', '604,57', '1,07', '1003,17', '1,66', '1,77']
hb2 = ['1 англійський фунт стерлінг', '103', '2004', '110,25', '1120,60', '10,16', '1350,40', '1,21', '12,25']
hb3 = ['1 англійський фунт стерлінг', '103', '2005', '1364,20', '1370,10', '1,00', '1380,15', '1,01', '1,01']
hb4 = ['10 бельгійських франків', '104', '2003', '113,03', '122,60', '1,08', '200,38', '1,63', '1,77']
hb5 = ['10 бельгійських франків', '104', '2004', '250,45', '260,45', '1,04', '275,20', '1,06', '1,10']
hb6 = ['10 бельгійських франків', '104', '2005', '280,10', '283,40', '1,01', '285,10', '1,01', '1,02']
hb7 = ['1 німецька марка', '105', '2003', '227,91', '252,07', '1,11', '412,02', '1,63', '1,81']
hb8 = ['1 німецька марка', '105', '2004', '444,23', '465,40', '1,05', '470,20', '1,01', '1,06']
hb9 = ['1 німецька марка', '105', '2005', '475,23', '480,30', '1,01', '485,20', '1,01', '1,02']
hb10 = ['1 голандський гульден', '106', '2003', '202,42', '224,00', '1,11', '366,26', '1,64', '1,81']
hb11 = ['1 голандський гульден', '106', '2004', '405,05', '425,35', '1,05', '450,30', '1,06', '1,11']
hb12 = ['1 голандський гульден', '106', '2005', '462,20', '464,10', '1,00', '466,15', '1,00', '1,01']
hb13 = ['1 канадський долар', '109', '2003', '267,88', '318,00', '1,19', '511,92', '1,61', '1,91']
hb14 = ['1 канадський долар', '109', '2004', '605,20', '630,15', '1,04', '680,25', '1,08', '1,12']
hb15 = ['1 канадський долар', '109', '2005', '690,10', '695,15', '1,01', '699,80', '1,01', '1,01']
hb16 = ['1 долар США', '111', '2003', '334,00', '396,00', '1,19', '652,62', '1,65', '1,95']
hb17 = ['1 долар США', '111', '2004', '700,30', '725,15', '1,04', '750,10', '1,03', '1,07']
hb18 = ['1 долар США', '111', '2005', '765,15', '775,10', '1,01', '785,20', '1,01', '1,03']

btable = BeautifulTable()
btable.column_headers = hb0
btable.append_row(hb1)
btable.append_row(hb2)
btable.append_row(hb3)
btable.append_row(hb4)
btable.append_row(hb5)
btable.append_row(hb6)
btable.append_row(hb7)
btable.append_row(hb8)
btable.append_row(hb9)
btable.append_row(hb10)
btable.append_row(hb11)
btable.append_row(hb12)
btable.append_row(hb13)
btable.append_row(hb14)
btable.append_row(hb15)
btable.append_row(hb16)
btable.append_row(hb17)
btable.append_row(hb18)

hbc0 = ['Найменування валюти', 'Рівень за три місяці']
hbc1 = ['1 англійський фунт стерлінг', '1,77']
hbc2 = ['1 англійський фунт стерлінг', '12,25']
hbc3 = ['1 англійський фунт стерлінг', '1,01']
hbc4 = ['10 бельгійських франків', '1,77']
hbc5 = ['10 бельгійських франків', '1,10']
hbc6 = ['10 бельгійських франків', '1,02']
hbc7 = ['1 німецька марка', '1,81']
hbc8 = ['1 німецька марка', '1,06']
hbc9 = ['1 німецька марка', '1,02']
hbc10 = ['1 голандський гульден', '1,81']
hbc11 = ['1 голандський гульден', '1,11']
hbc12 = ['1 голандський гульден', '1,01']
hbc13 = ['1 канадський долар', '1,91']
hbc14 = ['1 канадський долар', '1,12']
hbc15 = ['1 канадський долар', '1,01']
hbc16 = ['1 долар США', '1,95']
hbc17 = ['1 долар США', '1,07']
hbc18 = ['1 долар США', '1,03']

bctable = BeautifulTable()
bctable.column_headers = hbc0
bctable.append_row(hbc1)
bctable.append_row(hbc2)
bctable.append_row(hbc3)
bctable.append_row(hbc4)
bctable.append_row(hbc5)
bctable.append_row(hbc6)
bctable.append_row(hbc7)
bctable.append_row(hbc8)
bctable.append_row(hbc9)
bctable.append_row(hbc10)
bctable.append_row(hbc11)
bctable.append_row(hbc12)
bctable.append_row(hbc13)
bctable.append_row(hbc14)
bctable.append_row(hbc15)
bctable.append_row(hbc16)
bctable.append_row(hbc17)
bctable.append_row(hbc18)

root = Tk()

def btn_click():
    print(table)
def abtn_click():
    print(atable)
def bbtn_click():
    print(btable)
def cbtn_click():
    print(bctable)

root ['bg'] = '#fafafa'
root.title('таблиці')
root.wm_attributes('-alpha', 1)
root.geometry('600x400')


canvas = Canvas(root, height=600, width=400)
canvas.pack()

frame = Frame(root, bg='purple')
frame.place(relwidth=0.7 , relheight=0.7)

title = Label(frame, text='таблиці', bg='orange', font=40)
title.pack()
btn = Button(frame, text='повна таблиця 1', bg='white', command=btn_click)
btn.pack()
abtn = Button(frame, text='фільтрувати без років', bg='white', command=abtn_click)
abtn.pack()
bbtn = Button(frame, text='повна таблиця 2', bg='white', command=bbtn_click)
bbtn.pack()
cbtn = Button(frame, text='повна таблиця 2', bg='white', command=cbtn_click)
cbtn.pack()

root.mainloop()
