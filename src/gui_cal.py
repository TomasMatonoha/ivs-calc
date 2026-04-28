"""!
@file gui_cal.py
@brief GUI implementation for calculator
@author Jeremy Subrt (xsubrtj00)
@date 2026-04-24
@version x.x
@details This module implements a graphical user interface for a calculator using the Tkinter library. It provides basic arithmetic operations, as well as advanced functions such as factorial, power, square root, and permutations.
"""

import tkinter as tk
from tkinter import messagebox
from calc_library import comp_input


class CalculatorGUI:
    """!
    @brief CalculatorGUI class
    @details This class defines the structure and functionality of the calculator GUI. It includes methods for building the user interface, handling button clicks and evaluating expressions.
    """
    def __init__(self,root):
        """!
        @brief __init__ method
        @details This method initializes the calculator GUI, setting up the main window, defining colors, and calling the method to build the user interface.
        """
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

    
    def _build_ui(self):
        """!
        @brief _build_ui method
        @details This method constructs the user interface of the calculator, including the display area, number buttons, operation buttons, and advanced function buttons.
        """
        #focus on keyboard input handling
        self.root.focus_set()
        self.root.bind_all("<Key>",self.on_key)
        
        self.tool_frame=tk.Frame(self.root,bg=self.COLOR_BG)
        self.tool_frame.pack(fill="x",padx=8,pady=(8,4))

        #mode button
        self.mode_btn=tk.Button(
            self.tool_frame,
            text="Advanced functions",
            command=self.toggle_advanced
        )
        self.mode_btn.pack(side="right")

        #display
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


        """
        The following code creates buttons for digits 0-9 and arranges them in a grid layout. Each button is configured with a command to append the corresponding digit to the display when clicked.
        """
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

        """
        The following code creates buttons for utility functions such as clear (C) and backspace (<-). Each button is configured with a command to perform the corresponding action when clicked.
        """
        btnC=tk.Button(self.buttons_frame,text="C",font=("Arial",16),command=self.clear_display)
        btnC.grid(row=1,column=2,sticky="nsew",padx=2,pady=2)
        btnC.configure(bg=self.COLOR_BTN_UTIL,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_UTIL_ACT)

        btnBackspace=tk.Button(self.buttons_frame,text="<-",font=("Arial",16),command=self.backspace)
        btnBackspace.grid(row=1,column=1,sticky="nsew",padx=2,pady=2)
        btnBackspace.configure(bg=self.COLOR_BTN_UTIL,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_UTIL_ACT)

        """
        The following code creates buttons for basic arithmetic operations (addition, subtraction, multiplication, division) and the equals button. Each button is configured with a command to append the corresponding symbol to the display or evaluate the expression when clicked.
        """
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

        """
        The following code creates the frame for advanced functions and configures its grid layout. It includes buttons for factorial (!), power (^), square root (√), and permutations (P). Each button is configured with a command to append the corresponding symbol to the display when clicked.
        """
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

        btnCombNum=tk.Button(self.advanced_frame,text="nCr",font=("Arial",16),command=lambda:self.append_symbol("C"))
        btnCombNum.grid(row=0,sticky="nsew",padx=2,pady=2)
        btnCombNum.configure(bg=self.COLOR_BTN_OP,fg=self.COLOR_TEXT,activebackground=self.COLOR_BTN_OP_ACT)


    def on_key(self,event):
        """!
        @brief on_key method
        @details This method enables you to use the keyboard.
        """
        ch=event.char
        key=event.keysym
        #debug code:
        #print(ch,key)

        if ch.isdigit():
            self.append_symbol(ch)
        elif ch and ch in "+-*/!^C":
            self.append_symbol(ch)
        elif key in ("Return","KP_Enter"):
            self.evaluate_expression()
        elif key in ("BackSpace","Delete"):
            self.backspace()
        elif key=="Escape":
            self.clear_display()

    
    def toggle_advanced(self):
        """!
        @brief toggle_advanced method
        @details This method toggles the visibility of the advanced function buttons.
        """
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
        
    
    def append_symbol(self,symbol):
        """!
        @brief append_symbol method
        @details This method appends a given symbol (number or operator) to the current expression displayed on the calculator.
        @param symbol The symbol to be appended to the display.
        """
        
        current_text = self.display_var.get()
       

        operands=["+","-","/","*","!","C","^"]

        
        if symbol in operands:
            #if the frst symbol the user enters is an operator (exept `-`),ifnore it
            if current_text == "" and symbol != "-":
                return
            #if the previos character is olready an operator, ignor the new one
            elif current_text != "" and current_text[-1] in operands:
                return

        new_text = current_text+symbol
        self.display_var.set(new_text)
        #debug code:
        #print("symbol",symbol)

    
    def clear_display(self):
        """!
        @brief clear_display method
        @details This method clears the current expression displayed on the calculator, resetting it to an empty string.
        """
        self.display_var.set("")  

    
    def evaluate_expression(self):
        """!
        @brief evaluate_expression method
        @details This method evaluates the current expression displayed on the calculator.
        """
        expr=self.display_var.get().strip()
        
        #catch errors raised by cal_library
        try:
            result=comp_input(expr)
            self.display_var.set(str(result))
        except (AssertionError,TypeError,ValueError) as e:
            err_type=type(e).__name__
            messagebox.showerror("Calculation error",f"{err_type}: {e}")

        

    def backspace(self):
        """!
        @brief backspace method
        @details This method removes the last character from the current expression displayed on the calculator.
        """
        expr=self.display_var.get()
        if expr!="":
            new_text=expr[:-1]
            self.display_var.set(new_text)
        else:
            self.display_var.set(expr)


def main():
    """!
    @brief main function
    @details This function initializes the main application window and starts the Tkinter event loop to run the calculator GUI.
    """
    root=tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
if __name__=="__main__":
    main()

