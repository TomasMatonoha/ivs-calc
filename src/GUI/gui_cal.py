import tkinter as tk
from tkinter import messagebox
from calc_library import add,sub,mul,div

class CalculatorGUI:

    def __init__(self,root):
        self.root=root
        self.root.title("Kalkulacka")
        self.root.geometry("320x500")
        self.root.resizable(False,False)
        self.display_var=tk.StringVar(value="")
        self._build_ui()
        
    def _build_ui(self):
        self.display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            justify="right",
            font=("Arial",20)
        )
        self.display.grid(row=0,column=0,columnspan=4,sticky="nsew",padx=8,pady=8)

#tlacitka s cisly
        btn0 =tk.Button(self.root,text="0",font=("Arial",16),command=lambda:self.append_symbol("0"))
        btn0.grid(row=5,column=1,sticky="nsew",padx=4,pady=4)

        btn1 =tk.Button(self.root,text="1",font=("Arial",16),command=lambda:self.append_symbol("1"))
        btn1.grid(row=4,column=0,sticky="nsew",padx=4,pady=4)

        btn2 =tk.Button(self.root,text="2",font=("Arial",16),command=lambda:self.append_symbol("2"))
        btn2.grid(row=4,column=1,sticky="nsew",padx=4,pady=4)

        btn3 =tk.Button(self.root,text="3",font=("Arial",16),command=lambda:self.append_symbol("3"))
        btn3.grid(row=4,column=2,sticky="nsew",padx=4,pady=4)

        btn4 =tk.Button(self.root,text="4",font=("Arial",16),command=lambda:self.append_symbol("4"))
        btn4.grid(row=3,column=0,sticky="nsew",padx=4,pady=4)

        btn5 =tk.Button(self.root,text="5",font=("Arial",16),command=lambda:self.append_symbol("5"))
        btn5.grid(row=3,column=1,sticky="nsew",padx=4,pady=4)

        btn6 =tk.Button(self.root,text="6",font=("Arial",16),command=lambda:self.append_symbol("6"))
        btn6.grid(row=3,column=2,sticky="nsew",padx=4,pady=4) 

        btn7 =tk.Button(self.root,text="7",font=("Arial",16),command=lambda:self.append_symbol("7"))
        btn7.grid(row=2,column=0,sticky="nsew",padx=4,pady=4)

        btn8 =tk.Button(self.root,text="8",font=("Arial",16),command=lambda:self.append_symbol("8"))
        btn8.grid(row=2,column=1,sticky="nsew",padx=4,pady=4)

        btn9 =tk.Button(self.root,text="9",font=("Arial",16),command=lambda:self.append_symbol("9"))
        btn9.grid(row=2,column=2,sticky="nsew",padx=4,pady=4) 

#dalsi symboly
        btnC=tk.Button(self.root,text="C",font=("Arial",16),command=self.clear_display)
        btnC.grid(row=1,column=2,sticky="nsew",padx=4,pady=4)

#tlacitka s operacemi
        btnAddicion=tk.Button(self.root,text="+",font=("Arial",16),command=lambda:self.append_symbol("+"))
        btnAddicion.grid(row=4,column=3,sticky="nsew",padx=4,pady=4)

        btnMultipli=tk.Button(self.root,text="*",font=("Arial",16),command=lambda:self.append_symbol("*"))
        btnMultipli.grid(row=2,column=3,sticky="nsew",padx=4,pady=4)

        btnSub=tk.Button(self.root,text="-",font=("Arial",16),command=lambda:self.append_symbol("-"))
        btnSub.grid(row=3,column=3,sticky="nsew",padx=4,pady=4)

        btnDivision=tk.Button(self.root,text="/",font=("Arial",16),command=lambda:self.append_symbol("/"))
        btnDivision.grid(row=1,column=3,sticky="nsew",padx=4,pady=4)

        btnEqual=tk.Button(self.root,text="=",font=("Arial",16),command=self.evaluate_expression)
        btnEqual.grid(row=5,column=3,sticky="nsew",padx=4,pady=4)

        

    def append_symbol(self,symbol):
        current_text = self.display_var.get()
        new_text = current_text+symbol
        self.display_var.set(new_text)

    def clear_display(self):
        self.display_var.set("")  

    def evaluate_expression(self):
        expr=self.display_var.get()
        count=0
        opIndex=0

        for op in expr[1]:
            if op in ["+","-","*","/"]:
                opIndex=count
                opT=op
                break
        count=count+1
        #else:


        left_text=expr[:opIndex]
        right_text=expr[opIndex+1:]

        try:
            left=float(left_text)
            right=float(right_text)
        except ValueError:
            messagebox.showerror("Error","Unnown number")



     
        
    

def main():
    root=tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
if __name__=="__main__":
    main()

