from PIL import Image,ImageTk
from tkinter import *
import PIL.Image
import datashow_set_page2,data_clean3

class intro:
    def __init__(self):
        self.root=Tk()
        #self.root.geometry("700x500")
        self.root.state('zoomed')
        
        #image
        self.pic=PIL.Image.open('k.jpg')
        self.pictk=ImageTk.PhotoImage(self.pic)
        self.imglb=Label(self.root,image=self.pictk)
        self.imglb.place(x=0,y=0)
        
        #frame
        self.frame1=Frame(self.root,width=630,height=650,bg='white')
        self.frame1.place(x=65,y=20)

        #labels
        self.label1=Label(self.frame1,text='The dataset includes the following columns:',height=2,font=('Cooper Black',18,'bold','underline'),bg='white',fg='#c62f42')
        self.label1.place(x=30,y=0)
        
        self.label1=Label(self.frame1,text='Place:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=16,y=80)
        self.label1=Label(self.frame1,text='Name of the country or region',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=100,y=80)

        self.label1=Label(self.frame1,text='POP1980:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=20,y=105,width=90)
        self.label1=Label(self.frame1,text='Estimated population for the year 1980',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=105)
        
        
        self.label1=Label(self.frame1,text='POP2000:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=20,y=130,width=90)
        self.label1=Label(self.frame1,text='Estimated population for the year 2000',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=130)
        
        
        self.label1=Label(self.frame1,text='POP2010:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=20,y=155,width=90)
        self.label1=Label(self.frame1,text='Estimated population for the year 2010',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=155)
        
        self.label1=Label(self.frame1,text='POP2022:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=20,y=180,width=90)
        self.label1=Label(self.frame1,text='Estimated population for the year 2022',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=180)
        
        self.label1=Label(self.frame1,text='POP2023:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=20,y=205,width=90)
        self.label1=Label(self.frame1,text='Estimated population for the year 2023',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=205)

        
        self.label1=Label(self.frame1,text='POP2030:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=20,y=230,width=90)
        self.label1=Label(self.frame1,text='Estimated population for the year 2030',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=230)
        

        self.label1=Label(self.frame1,text='POP2050:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=20,y=255,width=90)
        self.label1=Label(self.frame1,text='Estimated population for the year 2050',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=255)
        

        
        self.label1=Label(self.frame1,text='Country:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=17,y=280,width=90)
        self.label1=Label(self.frame1,text='ISO 3166-1 alpha-3 code of the country',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=280)
        

        self.label1=Label(self.frame1,text='Area:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=2,y=305,width=90)
        self.label1=Label(self.frame1,text='Total land and water area of the country (in square km)',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=305)
        

        self.label1=Label(self.frame1,text='landAreakm:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=20,y=330,width=120)
        self.label1=Label(self.frame1,text='Land area of the country (in square kilometers)',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=150,y=330)
        
        self.label1=Label(self.frame1,text='cca2:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=0,y=355,width=90)
        self.label1=Label(self.frame1,text='ISO 3166-1 alpha-2 code of the country',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=355)

        
        self.label1=Label(self.frame1,text='cca3:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=0,y=380,width=90)
        self.label1=Label(self.frame1,text='ISO 3166-1 alpha-3 code of the country',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=380)
        
        
        self.label1=Label(self.frame1,text='netchange:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=10,y=405,width=120)
        self.label1=Label(self.frame1,text='Annual net change in population (in thousands)',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=405)

            
        self.label1=Label(self.frame1,text='growthRate:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=7,y=430,width=140)
        self.label1=Label(self.frame1,text='Annual population growth rate (as a percentage)',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=140,y=430)

        
        self.label1=Label(self.frame1,text='worldPercentage:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=9,y=455,width=180)
        self.label1=Label(self.frame1,text='Percentage of world population',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=180,y=455)

        self.label1=Label(self.frame1,text='density:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=0,y=480,width=110)
        self.label1=Label(self.frame1,text='Population density (in persons per square kilometer)',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=480)

        self.label1=Label(self.frame1,text='densityMI:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=0,y=505,width=130)
        self.label1=Label(self.frame1,text='Population density (in persons per square mile)',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=505)

        
        self.label1=Label(self.frame1,text='rank:-',height=1,font=('Cooper Black',12,'bold'),bg='white',fg='#c62f42')
        self.label1.place(x=0,y=530,width=90)
        self.label1=Label(self.frame1,text='Rank of the country by population',height=1,font=('Cooper Black',12),bg='white',fg='#1b2d2d')
        self.label1.place(x=120,y=530)



        self.button=Button(self.root,text='NEXT',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',14),command=self.nextwind)
        self.button.place(x=400,y=610,width=90,height=30)


        self.button=Button(self.root,text='BACK',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',14),command=self.backwind)
        self.button.place(x=220,y=610,width=90,height=30)

        
        
    
        self.root.mainloop()

    def backwind(self):
      self.root.destroy()
      datashow_set_page2.DataShow()

    def nextwind(self):
      self.root.destroy()
      data_clean3.lifecy()

if __name__ == '__main__':
    intro()