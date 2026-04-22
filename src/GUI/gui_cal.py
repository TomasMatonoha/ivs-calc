import tkinter as tk
from tkinter import messagebox
from calc_library import add,sub,mul,div

class CalculatorGUI:

#Define colors and structure for calculator
    def __init__(self,root):
        self.COLOR_BG="#1c1c1e"
        self.COLOR_BTN_NUM="#3a3a3c"
        self.COLOR_BTN_NUM_ACT="#636366"
        self.COLOR_BTN_OP="#c084fc"
        self.COLOR_BTN_OP_ACT="#a855f7"
        self.COLOR_BTN_UTIL="#636366"
        self.COLOR_BTN_UTIL_ACT="#7c7c7e"
        self.COLOR_TEXT="white"
        self.root=root
        self.root.title("Calculator")
        self.root.geometry("320x500")
        self.root.configure(bg=self.COLOR_BG)
        self.root.resizable(False,False)
        self.display_var=tk.StringVar(value="")
        self.advanced_visible=False
        self._build_ui()

#Building GUI
    def _build_ui(self):
        
        self.tool_frame=tk.Frame(self.root,bg=self.COLOR_BG)
        self.tool_frame.pack(fill="x",padx=8,pady=(8,4))

        self.mode_btn=tk.Button(
            self.tool_frame,
            text="Advanced functions",
            command=self.toggle_advanced
        )
        self.mode_btn.pack(side="right")

        self.display = tk.Label(
            self.root,
            textvariable=self.display_var,
            justify="right",
            font=("Arial",42),
            anchor="e",
            bg=self.COLOR_BG,
            fg=self.COLOR_TEXT
        )
        self.display.pack(fill="both",expand=True,padx=8,pady=8,ipady=12)

        self.content_frame=tk.Frame(
            self.root,
            bg=self.COLOR_BG
        )
        self.content_frame.pack(fill="both",expand=True,padx=8,pady=8)

#Buttons with numbers

        self.buttons_frame=tk.Frame(self.content_frame,bg=self.COLOR_BG)
        self.buttons_frame.pack(fill="both",expand=True,side="left")
        for c in range(4):
            self.buttons_frame.grid_columnconfigure(c,weight=1,uniform="col")
        for r in range(1,6):
            self.buttons_frame.grid_rowconfigure(r,weight=1)


        btn0 =tk.Button(self.buttons_frame,text="0",font=("Arial",16),command=lambda:self.append_symbol("0"))
        btn0.grid(row=5,column=1,sticky="nsew",padx=2,pady=2)
        btn0.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT,relief="flat")

        btn1 =tk.Button(self.buttons_frame,text="1",font=("Arial",16),command=lambda:self.append_symbol("1"))
        btn1.grid(row=4,column=0,sticky="nsew",padx=2,pady=2)
        btn1.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

        btn2 =tk.Button(self.buttons_frame,text="2",font=("Arial",16),command=lambda:self.append_symbol("2"))
        btn2.grid(row=4,column=1,sticky="nsew",padx=2,pady=2)
        btn2.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

        btn3 =tk.Button(self.buttons_frame,text="3",font=("Arial",16),command=lambda:self.append_symbol("3"))
        btn3.grid(row=4,column=2,sticky="nsew",padx=2,pady=2)
        btn3.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

        btn4 =tk.Button(self.buttons_frame,text="4",font=("Arial",16),command=lambda:self.append_symbol("4"))
        btn4.grid(row=3,column=0,sticky="nsew",padx=2,pady=2)
        btn4.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

        btn5 =tk.Button(self.buttons_frame,text="5",font=("Arial",16),command=lambda:self.append_symbol("5"))
        btn5.grid(row=3,column=1,sticky="nsew",padx=2,pady=2)
        btn5.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

        btn6 =tk.Button(self.buttons_frame,text="6",font=("Arial",16),command=lambda:self.append_symbol("6"))
        btn6.grid(row=3,column=2,sticky="nsew",padx=2,pady=2) 
        btn6.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

        btn7 =tk.Button(self.buttons_frame,text="7",font=("Arial",16),command=lambda:self.append_symbol("7"))
        btn7.grid(row=2,column=0,sticky="nsew",padx=2,pady=2)
        btn7.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

        btn8 =tk.Button(self.buttons_frame,text="8",font=("Arial",16),command=lambda:self.append_symbol("8"))
        btn8.grid(row=2,column=1,sticky="nsew",padx=2,pady=2)
        btn8.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

        btn9 =tk.Button(self.buttons_frame,text="9",font=("Arial",16),command=lambda:self.append_symbol("9"))
        btn9.grid(row=2,column=2,sticky="nsew",padx=2,pady=2) 
        btn9.configure(bg=self.COLOR_BTN_NUM,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_NUM_ACT)

#Special buttons
        btnC=tk.Button(self.buttons_frame,text="C",font=("Arial",16),command=self.clear_display)
        btnC.grid(row=1,column=2,sticky="nsew",padx=2,pady=2)
        btnC.configure(bg=self.COLOR_BTN_UTIL,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_UTIL_ACT)

        btnBackspace=tk.Button(self.buttons_frame,text="<-",font=("Arial",16),command=self.backspace)
        btnBackspace.grid(row=1,column=1,sticky="nsew",padx=2,pady=2)
        btnBackspace.configure(bg=self.COLOR_BTN_UTIL,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_UTIL_ACT)

#Buttons with operations
        btnAddicion=tk.Button(self.buttons_frame,text="+",font=("Arial",16),command=lambda:self.append_symbol("+"))
        btnAddicion.grid(row=4,column=3,sticky="nsew",padx=2,pady=2)
        btnAddicion.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

        btnMultipli=tk.Button(self.buttons_frame,text="*",font=("Arial",16),command=lambda:self.append_symbol("*"))
        btnMultipli.grid(row=2,column=3,sticky="nsew",padx=2,pady=2)
        btnMultipli.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

        btnSub=tk.Button(self.buttons_frame,text="-",font=("Arial",16),command=lambda:self.append_symbol("-"))
        btnSub.grid(row=3,column=3,sticky="nsew",padx=2,pady=2)
        btnSub.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

        btnDivision=tk.Button(self.buttons_frame,text="/",font=("Arial",16),command=lambda:self.append_symbol("/"))
        btnDivision.grid(row=1,column=3,sticky="nsew",padx=2,pady=2)
        btnDivision.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

        btnEqual=tk.Button(self.buttons_frame,text="=",font=("Arial",16),command=self.evaluate_expression)
        btnEqual.grid(row=5,column=3,sticky="nsew",padx=2,pady=2)
        btnEqual.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

#advanced buttons
        self.advanced_frame=tk.Frame(self.content_frame,bg=self.COLOR_BG)
        self.advanced_frame.grid_columnconfigure(0,weight=1)
        for r in range(4):
            self.advanced_frame.grid_rowconfigure(r,weight=1)

        btnFactorial=tk.Button(self.advanced_frame,text="!",font=("Arial",16),command=lambda:self.append_symbol("!"))
        btnFactorial.grid(row=3,sticky="nsew",padx=2,pady=2)
        btnFactorial.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

        btnPower=tk.Button(self.advanced_frame,text="^",font=("Arial",16),command=lambda:self.append_symbol("^"))
        btnPower.grid(row=1,sticky="nsew",padx=2,pady=2)
        btnPower.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

        btnSqr=tk.Button(self.advanced_frame,text="√",font=("Arial",16),command=lambda:self.append_symbol("√"))
        btnSqr.grid(row=2,sticky="nsew",padx=2,pady=2)
        btnSqr.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

        btnCombNum=tk.Button(self.advanced_frame,text="P",font=("Arial",16),command=lambda:self.append_symbol("P"))
        btnCombNum.grid(row=0,sticky="nsew",padx=2,pady=2)
        btnCombNum.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)

    #changing modes
    def toggle_advanced(self):
        if self.advanced_visible==False:
            self.advanced_visible=True
            self.root.geometry("420x500")
            self.mode_btn.configure(text="Basic functions")
            self.advanced_frame.pack(side="right",expand=True,fill="y") 
        else:
            self.advanced_visible=False
            self.root.geometry("320x500")
            self.mode_btn.configure(text="Advanced functions")
            self.advanced_frame.pack_forget()
        
    #adding symbols
    def append_symbol(self,symbol):
        
        current_text = self.display_var.get()
       

        operands=["+","-","/","*","!"]

        
        if symbol in operands:
            #if frst thing what is user going to add is operand then nothing happents
            if current_text == "" and symbol != "-":
                return
            #if user going to add 2 operands right behind then nothing hapents
            elif current_text != "" and current_text[-1] in operands:
                return

        new_text = current_text+symbol
        self.display_var.set(new_text)
        print("symbol",symbol)

    #clearing display
    def clear_display(self):
        self.display_var.set("")  

    #
    def evaluate_expression(self):
        expr=self.display_var.get()
        
    
    #backspace
    def backspace(self):
        expr=self.display_var.get()
        if expr!="":
            new_text=expr[:-1]
            self.display_var.set(new_text)
        else:
            self.display_var.set(expr)



     
        
    

def main():
    root=tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
if __name__=="__main__":
    main()

