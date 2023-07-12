from PIL import Image,ImageTk
from tkinter import *
import PIL.Image
import datashow_set_page2
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
        self.frame1=Frame(self.root,width=450,height=500,bg='white')
        self.frame1.place(x=65,y=110)

        #labels
        self.label1=Label(self.frame1,text='DATASCI MENTOR',height=3,font=('Cooper Black',25,'bold','underline'),bg='white',fg='#c62f42')
        self.label1.place(x=65,y=20)

        self.label2=Label(self.frame1,text='Highly reputable and sought-after platform for aspiring data scientists and those looking to advance their skills in the field of data science. It serves as a valuable resource for individuals at various stages of their data science journey.',height=1,font=('Cooper Black',14),wraplength=320,anchor=CENTER,justify=LEFT,bg='white',fg='#1b2d2d')
        self.label2.place(x=50,y=110,width=340,height=300)


        #self.label3=Label(self.frame1,text='1 INTRODUCTION',fg='#c62f42',bg='white',font=('Cooper Black',17))
        #self.label3.place(x=30,y=160)

        #button

        self.button=Button(self.root,text='NEXT',bg='#1b2d2d',fg='#c62f42',font=('Cooper Black',14),command=self.nextwind)
        self.button.place(x=240,y=530,width=90,height=40)

        self.root.mainloop()

    def nextwind(self):
      self.root.destroy()
      datashow_set_page2.DataShow()
    
if __name__ == '__main__':
    intro()