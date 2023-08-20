from tkinter import *
from tkinter import ttk
import pandas as pd
#import data_clean
import PIL.Image
from PIL import Image,ImageTk
import intro_page1

class DataShow():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.state('zoomed')

        #background image


        self.pic=PIL.Image.open('k.jpg')
        self.pictk=ImageTk.PhotoImage(self.pic)
        self.imglb=Label(self.root,image=self.pictk)
        self.imglb.place(x=0,y=0)

        self.heading = Label(self.root, text = 'Population Data Country Wise',fg='#c62f42',bg='#1b2d2d', font = ('Sans-Serif', 25, 'bold','underline'))
        self.heading.place(x=480,y=25)

    #buttons
        self.button1=Button(self.root,text='NEXT',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',14))
        self.button1.place(x=740,y=645,width=90,height=40)
         
         
        self.button2=Button(self.root,text='BACK',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',14),command=self.backwind)
        self.button2.place(x=540,y=645,width=90,height=40)
      


        df = pd.read_csv('2023_Countries by population.csv')
        # df.drop(['index'], axis = 1, inplace = True)

        columns = tuple(df.columns)
        tree = ttk.Treeview(self.root, columns=columns, show='headings')
    

        for col in columns:
            tree.heading(col, text=col) 
            tree.column(col, width=65)   
        
        
    
        #column color
        style=ttk.Style()
        style.configure('Treeview',foreground='#1b2d2d',rowheight=25)#fieldbackground='')
    

        # add data to the treeview
        for index, row in df.iterrows():
            tree.insert('', END, values = tuple(row.values))

        tree.place(x=110, y=150,width=1170,height=500)
    

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=1274, y=151,height=499)

        scrollbar1 = ttk.Scrollbar(self.root, orient=HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar1.set)
        scrollbar1.place(x=110, y=630,width=1170)

        # cleaning button
        # self.cleanBtn = Button(self.root, text='Data Cleaning', padx=20, pady=20, font=('Sans-serif', 20, 'bold'), command = self.clean)
        # self.cleanBtn.place(x = 360, y = 500)

        # self.visualBtn = Button(self.root, text='Visualization', padx=20, pady=20, font=('Sans-serif', 20, 'bold'))
        # self.visualBtn.place(x = 840, y = 500)

        #self.root.config(background= 'black')
        self.root.mainloop()

    
    def clean(self):
        self.root.destroy()
        #data_clean.DataClean()

    def back(self):
        self.root.destroy()
        intro_page1.intro()    

if __name__ == '__main__':
    DataShow()