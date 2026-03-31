import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:

    def __init__(self,root):
        self.root=root
        self.root.title("Kalkulacka")
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

        btn7 =tk.Button(self.root,text="7",font=("Arial",16),command=lambda:self.append_symbol("7"))
        btn7.grid(row=1,column=0,sticky="nsew",padx=4,pady=4)

        btnC=tk.Button(self.root,text="C",font=("Arial",16),command=self.clear_display())
        btnC.grid(row=1,column=1,sticky="nsew",padx=4,pady=4) 
        

    def append_symbol(self,symbol):
        current_text = self.display_var.get()
        new_text = current_text+symbol
        self.display_var.set(new_text)

    def clear_display(self):
        self.display_var.set("")    

     
        
    

def main():
    root=tk.Tk()
    CalculatorGUI(root)
    root.mainloop()
if __name__=="__main__":
    main()

