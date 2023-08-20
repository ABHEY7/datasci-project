from tkinter import *
from tkinter import ttk
import pandas as pd
#import data_clean
import PIL.Image
from PIL import Image,ImageTk
from tkinter import messagebox
import FEATURE_eng
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class lifecy:
    def __init__(self, df):
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
        

        self.heading2 = Label(self.root, text ='Step4- Visualisation',fg='#c62f42',bg='#1b2d2d', font = ('Sans-Serif', 24, 'bold'))
        self.heading2.place(x=160,y=305)
        
#--------------------------------------------------------------------------------------------------------
        self.df = df

        columns = tuple(df.columns)
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
        for index, row in df.iterrows():
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
        self.button3=Button(self.root,text='BACK',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',12),command=self.back)
        self.button3.place(x=40,y=25,width=100,height=40)

        #self.button3=Button(self.root,text='NEXT',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11))
        #self.button3.place(x=1210,y=25,width=100,height=40)

        self.button3=Button(self.root,text='Q1- Top 10 countries Estimated population for the year 1980',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),anchor='w',command=lambda: self.q1('pop1980'))
        self.button3.place(x=60,y=370,width=500,height=28)
              
        self.button3=Button(self.root,text='Q2- Top 5 countries Estimated population for the year 2023',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),anchor='w',command=lambda: self.q1('pop2023'))
        self.button3.place(x=60,y=410,width=500,height=28)
    
        self.button3=Button(self.root,text='Q3- Top 10 countries Estimated population for the year 2050',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),anchor='w',command=lambda: self.q1('pop2050'))
        self.button3.place(x=60,y=450,width=500,height=28)
       
        
        self.button3=Button(self.root,text='Q4- TOP 10 countries Area-wise',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),anchor='w',command=lambda: self.q1('area'))
        self.button3.place(x=60,y=490,width=500,height=28)
        self.button3=Button(self.root,text='Q5- TOP 10 countries with Highest growthRate',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),anchor='w',command=lambda: self.q1('growthRate'))
        self.button3.place(x=60,y=530,width=500,height=28)
        self.button3=Button(self.root,text='Q6- The Growth rates of the population Of the Growing china', bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),anchor='w',command=lambda: self.q1('china'))
        self.button3.place(x=60,y=570,width=500,height=28)
                
        #self.button3=Button(self.root,text='Q7- Compression Between Waterarea and Landarea  ',#bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',11),anchor='w',command=lambda: self.q1('landAreaKm'))
        #self.button3.place(x=60,y=655,width=500,height=28)
         

         
#---------------------------------------------------------------------------------------------------------
        #frame
        #self.frame1=Frame(self.root,width=220,height=200,bg='white')
        #self.frame1.place(x=100,y=450)

        
        #self.frame2=Frame(self.root,width=400,height=200,bg='white')
        #self.frame2.place(x=420,y=450,width=200)

        
        self.frame3=Frame(self.root,width=350,height=390,bg='white')
        self.frame3.place(x=600,y=320,width=700)


        
        self.root.mainloop()

#---------------------------------------------------------------------------------------------------------
    def q1(self, froms):
        print('froms ', froms)
        for widget in self.frame3.winfo_children():
            widget.destroy()
        
        fig = Figure(figsize = (7, 3.8),
                 dpi = 100)
        ax = fig.subplots()

        if froms == 'pop2050':
            if 'pop2050' in self.df.columns:
                o=self.df.sort_values(by='pop2050',ascending=False).head(10)
                print(o.head(10))
                sns.barplot(data=o,x='cca3',y='pop2050', ax = ax).set_title('Expected population for 2050')
                ax.set(xlabel='country',ylabel='population')
                
            else:
                messagebox.showerror('Alert', 'Not sufficient data.')
        if froms == 'pop1980':
            pass
            if 'pop1980' in self.df.columns:
                o=self.df.sort_values(by='pop1980',ascending=False).head(10)
                print(o.head(10))
                sns.barplot(data=o,x='cca3',y='pop1980', ax = ax).set_title('Expected population for 1980')
                ax.set(xlabel='country',ylabel='population ')
                
            else:
                messagebox.showerror('Alert', 'Not sufficient data.')


        if froms == 'area':
            pass
            if 'area' in self.df.columns:
                t=self.df.sort_values(by='area',axis=0,ascending=False).head(10)
                sns.barplot(data=t,x='cca3',y='area',ax=ax).set_title(' countries area wise')
            else:
                messagebox.showerror('Alert', 'Not sufficient data.' )
        #if froms == 'landAreaKm':
            #pass
            #if 'landAreaKm' in self.df.columns:
               # w=(self.df.Waterarea.sum(),self.df.area.sum())
              #  l='landarea','waterarea'
              #  print(w)
             #   ax.pie(w,labels=l,autopct='%1.2f%%')
            #else:
                #messagebox.showerror('Alert', 'Not sufficient data.' )
        
        if froms == 'growthRate':
            pass
            if 'growthRate' in self.df.columns:
                r=self.df.sort_values(by='growthRate',ascending=False).head(10)
                sns.barplot(data=r,x='cca3',y='growthRate',ax=ax).set_title(' countries with growthRate')
                ax.set(xlabel='country',ylabel='growthrate')           
            else:
                messagebox.showerror('Alert', 'Not sufficient data.' )
        if froms == 'china':
            pass
            if 'growthRate' in self.df.columns:
                self.df1 = self.df.set_index('country')  
                print('data frame is ', self.df)          
                country = 'China'
                # Extract the relevant columns for the population data from 1980 to 2050
                pop_data= self.df1.loc[country, 'pop1980':'pop2050']
                ax.plot(pop_data)
                ax.set_title('Population of China over time')
                #ax.title("Population Over Time")
                ax.set_xlabel("Year (1980-2050)")
                ax.set_ylabel("Population Growth Rate")
                ax.set_xticks(range(len(pop_data)), pop_data.index.str[3:])
            else:
                messagebox.showerror('Alert', 'Not sufficient data.' )
          
        if froms == 'pop2023':
            print('countries are ', self.df.columns)
            if 'pop2023' in self.df.columns:
                #i=self.df[self.df['area']==self.df['landAreaKm']]
                l=list(self.df.cca3.values[:5])
                o=list(self.df.pop2023.values[:5])
                print(o)
                ax.pie(o,labels=l, autopct='%.2f%%')
                
                ax.set_title('Estimated population for the year 2023')
                #ax.title("Population Over Time")
  #              ax.set_xlabel("")
 #               ax.set_ylabel("Population Growth Rate")
            else:
                messagebox.showerror('Alert', 'Not sufficient data.' )
            
        canvas = FigureCanvasTkAgg(fig,
                               master = self.frame3)  
        canvas.draw()    
        canvas.get_tk_widget().place(x = 0, y = 0)
        #for widget in self.frame2.winfo_children():
         #   widget.destroy()
        
        

    #def checkDuplicate(self):
     #   for widget in self.frame1.winfo_children():
      #      widget.destroy()
       # for widget in self.frame2.winfo_children():
        #    widget.destroy()
        #for widget in self.frame3.winfo_children():
         #   widget.destroy()
        #self.button6=Checkbutton(self.frame2,text=' DUPLICATE VALUES',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',9),command=self.checkdupli)
        #self.button6.place(x=11,y=35,width=170,height=30)
        


#        self.label1=Label(self.frame1,text='TOTAL DUPLICATE VALUES',height=5,font=('Cooper Black',10,'bold'),bg='white',fg='#c62f42')
 #       self.label1.place(x=0,y=23)

        
  #      self.label1=Label(self.frame1,text='0',font=('Cooper Black',20,'bold'),bg='white',fg='#c62f42')
   #     self.label1.place(x=90,y=70,height=50)
 
    def checkcolformat(self):
        for widget in self.frame1.winfo_children():
            widget.destroy()
        
        #for widget in self.frame2.winfo_children():
        #    widget.destroy()


        #for widget in self.frame3.winfo_children():
         #   widget.destroy()



        self.button9=Checkbutton(self.frame3,text='Place',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',9),command=self.checkcolumn)
        self.button9.place(x=10,y=35,width=170,height=30)
        
        self.button9=Checkbutton(self.frame3,text='Place',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',9),command=self.checkcolumn)
        self.button9.place(x=10,y=35,width=170,height=30)
        
        
#---------------------------------------------------------------------------------------------------------    
    def checkdropnul(self):
        for widget in self.frame3.winfo_children():
            widget.destroy()

        Label(self.frame3, text = 'we use dropna() method to removes the rows that contains NULL values. The dropna() method returns a new DataFrame object unless the inplace parameter is set to True , in that case the dropna() method does the removing in the original DataFrame instea-d.',width=100,height=8,wraplength=600,font = ('Sans-Serif', 10, 'bold'),bg='white').place(x=0,y=25)

        
        Label(self.frame3, text = 'Drop Null Values',width=30,height=2,bg='white',font = ('Sans-Serif', 12, 'bold','underline'),fg='#c62f42').place(x=230,y=15)
    
    
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
        

    def dupli(self):
        res = messagebox.askyesno('Confirmation', 'Are you sure you want to drop the data ?')
        if res:
            # delete the data
            messagebox.showinfo('Success', 'Data deleted successfully.')

    def dupli1(self):
        res = messagebox.askyesno('Confirmation', 'Are you sure you want to Fill the data ?')
        if res:
            # delete the data
            messagebox.showinfo('Success', 'Data Fill successfully.')


    def dupli2(self):
        res = messagebox.askokcancel('OOPS?', 'There No Duplicate value ')
        #if res:
            # delete the data
         #   messagebox.showinfo('Success', 'Data Fill successfully.')


    def back(self):
        self.root.destroy()
        FEATURE_eng.lifecy(self.df)

if __name__ == '__main__':
    lifecy(pd.read_csv('2023_Countries by Population.csv'))
