from tkinter import *
root=Tk()
root.title("polymorphism")
root.geometry("600x600")

class grade3():
    def __init__(self,language,maths):
        self.lang=language
        self.ma=maths
    def percent(self):
        total_marks=self.lang+self.ma
        percentage_grade3=(total_marks/200)*100
        label_grade3_per["text"]=percentage_grade3
        
class grade5():
    def __init__(self,language,maths,science):
        self.lang=language
        self.math=maths
        self.sci=science
    def percent(self):
        total_marks=self.lang+self.math+self.sci
        percentage_grade5=(total_marks/300)*100
        label_grade5_per["text"]=percentage_grade5
        
class grade10():
    def __init__(self,maths,science,language,coding):
        self.lang=language
        self.math=maths
        self.sci=science
        self.code=coding
    def percent(self):
        total_marks=self.lang+self.math+self.sci+self.code
        percentage_grade10=(total_marks/400)*100
        label_grade10_per["text"]=percentage_grade10
        
obj_grade3=grade3(60,80)
obj_grade5=grade5(70,70,70)
obj_grade10=grade10(70,80,90,80)

        

btn_grade3=Button(root,text="grade 3",command=obj_grade3.percent)
btn_grade3.pack(padx=20,pady=20)
label_grade3_per=Label(root)
label_grade3_per.pack()
btn_grade5=Button(root,text="grade 5",command=obj_grade5.percent)
btn_grade5.pack(padx=20,pady=20)
label_grade5_per=Label(root)
label_grade5_per.pack()
btn_grade10=Button(root,text="grade 10",command=obj_grade10.percent)
btn_grade10.pack(padx=20,pady=20)
label_grade10_per=Label(root)
label_grade10_per.pack()


root.mainloop()
