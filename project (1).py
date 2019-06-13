from tkinter import Tk, Label,OptionMenu,StringVar,Button,Entry,messagebox
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
import matplotlib.pyplot as plt
import requests
from sklearn.linear_model import LinearRegression
from datetime import date , timedelta
from get_data import get_data_of_stocks
from prdict_data import predict_data
import project_databases as db
import sqlite3

plt.style.use('ggplot')

def show_prediction():
    predicted = predict_data(variable1.get())
    days = [i for i in range(1,31)]

    plt.plot(days,predicted)
    plt.xlabel('Number of Days')
    plt.ylabel('Predicted closing price')
    plt.title(variable1.get())
    plt.show()
    
def buttonClick1():
    close , opens , low , high , dates ,volume = get_data_of_stocks(variable1.get())

    new_dates = []
    new_close = []

    for i in range(0, len(close), 15):
        new_dates.append(dates[i])
        new_close.append(close[i])
    
    plt.plot(new_dates,new_close)
    plt.xlabel("Dates($)")
    plt.ylabel("Closing Price($)")
    plt.title(variable1.get())
    plt.show()

def insert():
    share = StringVar
    quantity = IntVar
    share = variable1.get()
    quantity = E1.get()
    amount = round(get_data_of_stocks(share)[2][0], 2)
    invest = round(float(quantity) * float(amount), 2)
    stock = db.Stocks(share, quantity, amount, invest)
    db.insert_stocks(stock)
    message = "Company: {}\nQuantity: {}\nPrice: {}\nInvestment: {}".format(share, quantity, amount, invest)
    tab1_display.insert(INSERT, message)
    
def buttonClick2():
    window1 = Toplevel(root)
    window1.geometry("450x450+50+50")
    window1.title("Fund Manage")
    t = StringVar()
    l = Label(window1, textvariable = t)
    t.set("Are you sure?")
    l.pack()
    b1 = Button(window1, text = 'Yes', command = insert).pack(fill=X)
    b2 = Button(window1, text = 'No', command = window1.destroy).pack(fill=X)
    
root = Tk()

root.title("Stock Market")
root.geometry("1050x700+50+50")

main_menu = Menu(root, tearoff=0)
main_menu.add_command(label="Buy")
main_menu.add_command(label="Sell")
root.config(menu=main_menu)

label1 = Label(root, text="Stock Market Management", font="none 24 bold",bg="orange",fg = "White").place(x=230,y=0,width=600,height=40)

label21 = Label(root, text="Stocks", font="none 16 bold",bg="grey",fg = "black").place(x=525,y=55,width=100,height=40)

OPTIONS = [
"Microsoft",
"Apple",
"Google"
]

variable1 = StringVar(root)
variable1.set(OPTIONS[0]) # default value

w1 = OptionMenu(root, variable1, *OPTIONS).place(x=525,y=102,width=100,height=40)

variable2 = StringVar(root)
variable2.set(OPTIONS[0]) # default value

button2= Button(root, text='Buy',bg = "Green",command=buttonClick2)
button2.place(x = 525,y = 190,width = 120,height = 30)

my_text = Label(root,text="Quantity")
my_text.place(x = 475,y = 150,width = 60,height = 30)

E1=Entry(root,bg='white',fg='black',font=('Georgia',10))
E1.place(x = 540,y = 150,width = 120,height = 30)

label1 = Label(root, text=" CURRENT PORTFOLIO", font="none 24 bold",bg="orange",fg = "White").place(x=230,y=290,width=600,height=40)

tab1_display = Text(root, height = 5)
tab1_display.grid(columnspan = 2, pady = 3, padx = 5)
tab1_display.place(x = 180,y = 370,width = 700)

labe112 = Label(root, text="Stock History:", font="none 16 bold",bg="grey",fg = "black").place(x=515,y=550,width=180,height=30)

button11= Button(root, text='Stock Details',bg = "Blue",command=buttonClick1)
button11.place(x = 525,y = 590,width = 150,height = 30)

next_30_price_pred = Button(root, text='Price of next 30 days',bg = "Blue",command=show_prediction)
next_30_price_pred.place(x = 525,y = 640,width = 150,height = 30)

root.mainloop()
