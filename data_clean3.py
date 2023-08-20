from tkinter import *
from tkinter import ttk
import pandas as pd
#import data_clean
import PIL.Image
from PIL import Image,ImageTk
from tkinter import messagebox
import column_datashow,FEATURE_eng

class lifecy:
    def __init__(self):
        self.root=Tk()
        self.root.state('zoomed')

#---------------------------------------------------------------------------------------------------------
        #image
        self.pic=PIL.Image.open('gk.jpg')
        self.pictk=ImageTk.PhotoImage(self.pic)
        self.imglb=Label(self.root,image=self.pictk)
        self.imglb.place(x=0,y=0)

#---------------------------------------------------------------------------------------------------------
        #label
        self.heading = Label(self.root, text = 'Population Data Country Wise',fg='#c62f42',bg='#1b2d2d', font = ('Sans-Serif', 25, 'bold','underline'))
        self.heading.place(x=480,y=20)
        #self.heading = Label(self.root, text = 'The population data from the United Nations is a dataset that contains information on the estimated population of each country in the world for various years between 1980 and 2050.',fg='#c62f42',bg='#1b2d2d', font = ('Sans-Serif', 10, 'bold'),wraplength=1000)
        #self.heading.place(x=180,y=49)
                

        self.heading2 = Label(self.root, text ='Step2- Cleaning Of Data',fg='#c62f42',bg='#1b2d2d', font = ('Sans-Serif', 23, 'bold'))
        self.heading2.place(x=45,y=330)
        
#--------------------------------------------------------------------------------------------------------
        self.df = pd.read_csv('2023_Countries by population.csv')

        columns = tuple(self.df.columns)
        tree = ttk.Treeview(self.root, columns=columns, show='headings')
    

        for col in columns:
            tree.heading(col, text=col) 
            tree.column(col, width=65)   
        
        
#--------------------------------------------------------------------------------------------------------    
        #column color
        style=ttk.Style()
        style.configure('Treeview',foreground='#1b2d2d',rowheight=25)#fieldbackground='')
    
#---------------------------------------------------------------------------------------------------------
        # add data to the treeview
        for index, row in self.df.iterrows():
            tree.insert('', END, values = tuple(row.values))

        tree.place(x=110, y=90,width=1170,height=200)
    
#---------------------------------------------------------------------------------------------------------
        # add a scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=1278, y=91,height=197)

        scrollbar1 = ttk.Scrollbar(self.root, orient=HORIZONTAL, command=tree.xview)
        tree.configure(xscroll=scrollbar1.set)
        scrollbar1.place(x=110, y=276,width=1173)
#---------------------------------------------------------------------------------------------------------
        #button
        self.button1=Button(self.root,text='Check For Null Values',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11), command = self.checknull)
        self.button1.place(x=530,y=385,width=220,height=40)


        self.button2=Button(self.root,text='Check For Duplicate Values',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11), command=self.checkDuplicate)
        self.button2.place(x=1000,y=385,width=220,height=40)

        
        #self.button3=Button(self.root,text='Check For Column Format',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),command=self.checkcolformat)
       # self.button3.place(x=1080,y=385,width=220,height=40)

        self.button3=Button(self.root,text='BACK',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),command=self.back)
        self.button3.place(x=40,y=25,width=100,height=40)

        self.button3=Button(self.root,text='NEXT',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),command=self.next)
        self.button3.place(x=1210,y=25,width=100,height=40)
       
       
#---------------------------------------------------------------------------------------------------------
        #frame
        self.frame1=Frame(self.root,width=220,height=200,bg='white')
        self.frame1.place(x=140,y=450)

        
        self.frame2=Frame(self.root,width=400,height=200,bg='white')
        self.frame2.place(x=420,y=450,width=200)

        
        self.frame3=Frame(self.root,width=400,height=200,bg='white')
        self.frame3.place(x=620,y=450,width=700)


        
        self.root.mainloop()

#---------------------------------------------------------------------------------------------------------
    def checknull(self):
        for widget in self.frame1.winfo_children():
            widget.destroy()
        for widget in self.frame2.winfo_children():
            widget.destroy()
        for widget in self.frame3.winfo_children():
            widget.destroy()
        
        
        self.label1=Label(self.frame1,text='TOTAL NULL VALUES',height=5,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=11,y=13)

        
        self.label1=Label(self.frame1,text='15',font=('Cooper Black',20,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=70,y=70,height=50)


    

        self.button0=Button(self.frame2,text='Drop Null Values',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',9),command=self.checkdropnul)
        self.button0.place(x=30,y=55,width=120,height=30)
        
        self.button5=Button(self.frame2,text='Fill Values',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',9),command=self.checkfillvalu)
        self.button5.place(x=30,y=105,width=120,height=30)


    def checkDuplicate(self):
        for widget in self.frame1.winfo_children():
            widget.destroy()
        for widget in self.frame2.winfo_children():
            widget.destroy()
        for widget in self.frame3.winfo_children():
            widget.destroy()
        self.button6=Button(self.frame2,text=' DUPLICATE VALUES',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',9),command=self.checkdupli)
        self.button6.place(x=11,y=75,width=160,height=30)
        


        self.label1=Label(self.frame1,text='TOTAL DUPLICATE VALUES',height=5,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42',wraplength=200)
        self.label1.place(x=12,y=23)

        
        self.label1=Label(self.frame1,text='0',font=('Cooper Black',20,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=90,y=100,height=50)

    
    def checkcolformat(self):
        for widget in self.frame1.winfo_children():
            widget.destroy()

        for widget in self.frame2.winfo_children():
            widget.destroy()


        for widget in self.frame3.winfo_children():
            widget.destroy()




        self.button9=Button(self.frame2,text='COLUMNS',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',9),command=self.checkcolumn)
        self.button9.place(x=10,y=35,width=170,height=30)
        
#---------------------------------------------------------------------------------------------------------    
    def checkdropnul(self):
        for widget in self.frame3.winfo_children():
            widget.destroy()

        Label(self.frame3, text = 'It is simplest to handle the missing values.But we will we lsoing Data for countries  ',width=100,height=1,wraplength=600,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=55)

        a = self.df.columns[self.df.isna().any()]
        countryDeleted = " ".join([", ".join(self.df[self.df[i].isna()].country.tolist()) for i in a])
        Label(self.frame3, text = f'Country Names- {countryDeleted}',width=90,height=4,wraplength=700,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=75)

        a = self.df.columns[self.df.isna().any()]
        countryDeleted = " ".join([", ".join(self.df[self.df[i].isna()].country.tolist()) for i in a])
        
        Label(self.frame3, text = 'Drop Null Values',width=30,height=2,bg='white',font = ('Sans-Serif', 12, 'bold','underline'),fg='#c62f42').place(x=210,y=10)
    
    
        Button(self.frame3,text='DROP',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.dupli).place(x=330,y=150,width=100,height=30)
        
        
        
    def checkfillvalu(self):
        for widget in self.frame3.winfo_children():
            widget.destroy()


        Label(self.frame3, text = 'filling missing values allows you to retain and utilize as much information as possible',width=100,height=8,wraplength=600,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=25)

        Label(self.frame3, text = 'Fill Null Values',width=30,height=2,bg='white',font = ('Sans-Serif', 12, 'bold','underline'),fg='#c62f42').place(x=230,y=15)

        Button(self.frame3,text='Fill',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.dupli1).place(x=330,y=150,width=100,height=30)
        

    def checkcolumn(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()
        
        Label(self.frame3, text = '...',width=100,height=8,wraplength=700,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=25)

        Label(self.frame3, text = 'columns',width=30,height=2,bg='white',font = ('Sans-Serif', 12, 'bold','underline'),fg='#c62f42').place(x=230,y=15)
        
        #Button(self.root,text='Fill',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.dupli1).place(x=700,y=665,width=300,height=33)


    def checkdupli(self):
        for widget in self.frame3.winfo_children():
            widget.destroy()

        Label(self.frame3, text ='In data science, handling duplicate values in a dataset is an important step in data preprocessing. Duplicate values can arise due to various reasons, such as data entry errors, data merging, or data collection processes. Dealing with duplicate values ensures data integrity and prevents bias in analysis or modeling',width=80,height=8,wraplength=600,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=25)

        Label(self.frame3, text = 'Duplicates Values',width=30,height=2,bg='white',font = ('Sans-Serif', 12, 'bold','underline'),fg='#c62f42').place(x=200,y=15)
        

        #Button(self.root,text='DROP',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.dupli2).place(x=700,y=665,width=300,height=33)
        

    def dupli(self):
        if self.df.isna().sum().sum() != 0:
            res = messagebox.askyesno('Confirmation', 'Are you sure you want to drop the data ?')
            if res:
                # df=self.df.dropna()
                # df=df.isnull().sum().sum()
                for widget in self.frame1.winfo_children():
                    widget.destroy()

                self.df.dropna(inplace = True)
                self.label1=Label(self.frame1,text='TOTAL NULL VALUES',height=5,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
                self.label1.place(x=11,y=13)

            
                self.label1=Label(self.frame1,text=f'{self.df.isnull().sum().sum()}',font=('Cooper Black',20,'bold'),bg='white',fg='#c62f42')
                self.label1.place(x=82,y=70,height=50)
            

                messagebox.showinfo('Success', 'Data deleted successfully.')
        else:
            messagebox.showerror('Alert', 'There is no empty data.')

    def dupli1(self):
        if self.df.isnull().sum().sum() != 0:
            res = messagebox.askyesno('Confirmation', 'Are you sure you want to Fill the data ?')
            if res:

                for widget in self.frame1.winfo_children():
                    widget.destroy()
#fill values of prcentage column
            indx=self.df['worldPercentage'][self.df['worldPercentage'].isnull()].index

            o=[(self.df['pop2023'][228]//self.df['pop2023'].sum()),(self.df['pop2023'][229]//self.df['pop2023'].sum()),(self.df['pop2023'][230]//self.df['pop2023'].sum()),(self.df['pop2023'][231]//self.df['pop2023'].sum()),(self.df['pop2023'][232]//self.df['pop2023'].sum()),(self.df['pop2023'][233]//self.df['pop2023'].sum())]

            k=pd.DataFrame({"worldPercentage":o},index=indx)
            self.df.loc[indx,'worldPercentage']=k.loc[:,:]
#fill null values of cca2 column
            self.df=self.df.drop(144)
            
#fill null values of netchange column
            
            netchange_index=self.df['netChange'][self.df['netChange'].isnull()].index
            
            netchange_index
            b = [((self.df['pop2000'] - self.df['pop1980']) // 20), ((self.df['pop2010'] - self.df['pop2000']) // 10), ((self.df['pop2022'] - self.df['pop2010']) // 12), ((self.df['pop2023'] - self.df['pop2022']) // 1), ((self.df['pop2030'] - self.df['pop2023']) // 7), ((self.df['pop2050'] - self.df['pop2030']) // 20)]
            
            c = pd.DataFrame(b)
        
            c.loc[:, :] = c.loc[:, :] // 1000
            c.loc[:, :].mean()

            self.df.loc[netchange_index, 'netChange'] = c.loc[:, :].mean()       


            self.label1=Label(self.frame1,text='TOTAL NULL VALUES',height=5,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
            self.label1.place(x=11,y=13)

                
            self.label1=Label(self.frame1,text=f'{self.df.isnull().sum().sum()}',font=('Cooper Black',20,'bold'),bg='white',fg='#c62f42')
            self.label1.place(x=82,y=70,height=50)
                            
                    # delete the data
            messagebox.showinfo('Success', 'Data Fill successfully.')
        else:

           messagebox.showerror('Alert', 'There is no empty data.')
 

    def dupli2(self):
        res = messagebox.askokcancel('OOPS?', 'There No Duplicate value ')
        #if res:
            # delete the data
         #   messagebox.showinfo('Success', 'Data Fill successfully.')


    def back(self):
        self.root.destroy()
        column_datashow.intro()
    def next(self):
        self.root.destroy()
        FEATURE_eng.lifecy(self.df)
if __name__ == '__main__':
    lifecy()
