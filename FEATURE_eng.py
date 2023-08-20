from tkinter import *
from tkinter import ttk
import pandas as pd
#import data_clean
import PIL.Image
from PIL import Image,ImageTk
from tkinter import messagebox
import data_clean3,visulisation_page

class lifecy:
    def __init__(self, df):
        self.columns = []
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
        

        self.heading2 = Label(self.root, text ='Step3- Feature engineering',fg='#c62f42',bg='#1b2d2d', font = ('Sans-Serif', 23, 'bold'))
        self.heading2.place(x=45,y=320)
        
#--------------------------------------------------------------------------------------------------------
        self.df = df
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
        self.button1=Button(self.root,text='Feature Selection',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11), command = self.checkselection)
        self.button1.place(x=520,y=385,width=220,height=40)


#        self.button2=Checkbutton(self.root,text='Check For Duplicate Values',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11), command=self.checkDuplicate)
 #       self.button2.place(x=620,y=385,width=220,height=40)

        
        self.button3=Button(self.root,text='Feature Extration',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),command=self.checkdextraction)
        self.button3.place(x=1000,y=385,width=220,height=40)

        self.button3=Button(self.root,text='BACK',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),command=self.back)
        self.button3.place(x=40,y=25,width=100,height=40)

        self.button3=Button(self.root,text='NEXT',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),command=self.next)
        self.button3.place(x=1210,y=25,width=100,height=40)
       
       
#---------------------------------------------------------------------------------------------------------
        #frame
        self.frame1=Frame(self.root,width=220,height=200,bg='white')
        self.frame1.place(x=100,y=450)

        
        #self.frame2=Frame(self.root,width=400,height=200,bg='white')
        #self.frame2.place(x=420,y=450,width=200)

        
        self.frame3=Frame(self.root,width=400,height=220,bg='white')
        self.frame3.place(x=420,y=450,width=900)


        
        self.root.mainloop()

#---------------------------------------------------------------------------------------------------------
    
        
    def checkselection(self):
        for widget in self.frame3.winfo_children():
            widget.destroy()
        for widget in self.frame1.winfo_children():
            widget.destroy()
        
    
    
        self.label1=Label(self.frame1,text='Recommended Columns To Drop',height=3,font=('Sans-Serif', 13, 'bold'),bg='white',fg='#1b2d2d',wraplength=200)
        self.label1.place(x=16,y=5)


        self.label1=Label(self.frame1,text='- cca3',font=('Sans-Serif', 13, 'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=30,y=70,height=50)
        
        self.label1=Label(self.frame1,text='- cca2',font=('Sans-Serif', 13, 'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=30,y=110,height=50)

    
        self.label1=Label(self.frame1,text='- density',font=('Sans-Serif', 13, 'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=30,y=150,height=50)


        self.label1=Label(self.frame3,text=' It involves selecting a subset of relevant features (also referred to as variables or attributes) from a larger set of available features. ',height=2,font=('Sans-Serif', 11, 'bold'),wraplength=900,bg='white',fg='#1b2d2d')
        self.label1.place(x=11,y=0)

        self.button0=Checkbutton(self.frame3,text='         place',bg='white',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('place'))
        self.button0.place(x=20,y=50,width=110,height=22)
        
        self.button5=Checkbutton(self.frame3,text='  POP1980',bg='white',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('pop1980'))
        self.button5.place(x=20,y=85,width=110,height=22)

        
        self.button5=Checkbutton(self.frame3,text='  POP2000',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('pop2000'))
        self.button5.place(x=20,y=120,width=110,height=22)


        self.button5=Checkbutton(self.frame3,text='  POP2010',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('pop2010'))
        self.button5.place(x=20,y=155,width=110,height=22)

        self.button5=Checkbutton(self.frame3,text='  POP2022',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('pop2022'))
        self.button5.place(x=20,y=190,width=110,height=20)


        self.button5=Checkbutton(self.frame3,text='  POP2023',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('pop2023'))
        self.button5.place(x=250,y=50,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text='  POP2030',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('pop2030'))
        self.button5.place(x=250,y=85,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text='  POP2050',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('pop2050'))
        self.button5.place(x=250,y=120,width=110,height=20)


        
        self.button5=Checkbutton(self.frame3,text='   Country',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('country'))
        self.button5.place(x=250,y=155,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text='         Area',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('area'))
        self.button5.place(x=250,y=190,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text=' landAreaKM',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('landAreaKm'))
        self.button5.place(x=480,y=50,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text='               cca2',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('cca2'))
        self.button5.place(x=480,y=85,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text='               cca3',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('cca3'))
        self.button5.place(x=480,y=120,width=110,height=20)


        self.button5=Checkbutton(self.frame3,text='   netChange',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('netChange'))
        self.button5.place(x=480,y=155,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text=' growthRate',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('growthRate'))
        self.button5.place(x=480,y=190,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text=' worldPer',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('worldPercentage'))
        self.button5.place(x=700,y=50,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text='   density',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 11, 'bold'), command= lambda : self.getSelect('density'))
        self.button5.place(x=700,y=85,width=110,height=20)

        self.button5=Checkbutton(self.frame3,text='     densityMi',bg='WHITE',fg='#c62f42',font=('Sans-Serif', 10, 'bold'),onvalue=0,offvalue=1, command= lambda : self.getSelect('densityMi'))
        self.button5.place(x=700,y=120,width=130,height=20)

        self.button5=Button(self.frame3,text='SUBMIT',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.submitCol)
        self.button5.place(x=700,y=170,width=130,height=40)

        
#---------------------------------------------------------------------------------------------------------    
    def checkdextraction(self):
        for widget in self.frame3.winfo_children():
            widget.destroy()
        for widget in self.frame1.winfo_children():
            widget.destroy()

        Label(self.frame3, text = ' The process of transforming raw data into numerical features that can be processed while preserving the information in the original data set',width=100,height=2,wraplength=600,font = ('Sans-Serif', 10, 'bold'),bg='white',fg='#1b2d2d').place(x=10,y=25)

        self.water=self.df['area']-self.df['landAreaKm']
        w=list(self.water.values)
        self.df['Waterarea']=w
        print(self.df)
        
        
        self.label1=Label(self.frame3,text='- Add Column',font=('Sans-Serif', 13, 'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=350,y=80)
        
        Checkbutton(self.frame3, text = ' Waterarea  ',width=50,height=1,font = ('Sans-Serif', 10, 'bold'),bg='white',fg='#1b2d2d').place(x=200,y=120)
        
        Button(self.frame3, text = 'SUBMIT ',width=10,height=1,font = ('Sans-Serif', 13, 'bold'),bg='#1b2d2d',fg='#c62f42',command=self.getSelect).place(x=350,y=170)


    
        self.label1=Label(self.frame1,text='Recommended Columns To Drop',height=3,font=('Sans-Serif', 15, 'bold'),bg='white',fg='#1b2d2d',wraplength=200)
        self.label1.place(x=16,y=5)


        self.label1=Label(self.frame1,text='- Waterarea',font=('Sans-Serif', 13, 'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=30,y=90,height=50)
        
    
        #Checkbutton(self.root,text='DROP',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.dupli).place(x=700,y=665,width=300,height=33)
        
    def checkfillvalu(self):
        for widget in self.frame3.winfo_children():
            widget.destroy()


        Label(self.frame3, text = 'The fillna() method replaces the NULL values with a specified value.The fillna() method returns a new DataFrame object unless the inplace parameter is set to True, in that case the fillna() method does the replacing in the original DataFrame instead',width=100,height=8,wraplength=600,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=25)

        Label(self.frame3, text = 'Fill Null Values',width=30,height=2,bg='white',font = ('Sans-Serif', 12, 'bold','underline'),fg='#c62f42').place(x=230,y=15)

        #Checkbutton(self.root,text='Fill',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.dupli1).place(x=700,y=665,width=300,height=33)
        

    def checkcolumn(self):
        for widget in self.frame3.winfo_children():
            widget.destroy()
        
        Label(self.frame3, text = '...',width=100,height=8,wraplength=700,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=25)

        Label(self.frame3, text = 'columns',width=30,height=2,bg='white',font = ('Sans-Serif', 12, 'bold','underline'),fg='#c62f42').place(x=230,y=15)
        
        #Checkbutton(self.root,text='Fill',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.dupli1).place(x=700,y=665,width=300,height=33)


    def checkdupli(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

        Label(self.frame3, text ='The duplicated() method returns a Series with True and False values that describe which rows in the DataFrame are duplicated and not.',width=100,height=8,wraplength=700,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=25)

        Label(self.frame3, text = 'Duplicates Values',width=30,height=2,bg='white',font = ('Sans-Serif', 12, 'bold','underline'),fg='#c62f42').place(x=230,y=15)
        

        #Checkbutton(self.root,text='DROP',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',13),command=self.dupli2).place(x=700,y=665,width=300,height=33)
        

#    def submit(self):
 #       res = messagebox.askyesno('Confirmation', 'Are you sure you want to Submit the data ?')
  #      if res:
   #      def submitCol(self):
    #       self.df = self.df.loc[:, self.columns]

            # delete the data
     #   messagebox.showinfo('Success', 'Data Submit successfully.')

    #def sub(self):
     #   res = messagebox.askyesno('Confirmation', 'Are you sure you want to Fill the data ?')
      #  if res:
            # delete the data
       #     messagebox.showinfo('Success', 'Data Fill successfully.')


    def back(self):
        self.root.destroy()
        data_clean3.lifecy()
    def next(self):
        self.root.destroy()
        visulisation_page.lifecy(self.df)

    def getSelect(self, froms):
        # columns = []
        print(froms)
        self.columns.append(froms)

    def submitCol(self):
      self.df = self.df.loc[:, self.columns]

    #def submit(self):
     #   messagebox.showinfo('sucess', 'The Data submit sucessfully ?')
        #if res:
               
            # delete the data
         #messagebox.showinfo('Su
if __name__ == '__main__':
    lifecy(pd.read_csv('2023_Countries by Population.csv'))
