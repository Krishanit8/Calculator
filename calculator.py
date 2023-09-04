import customtkinter as ctk
from PIL import Image
import tkinter as tk
from tkinter import messagebox
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Calculator(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Calculator')
        self.resizable(0,0)
        self.config(bg='black')

        self.input_limit = 15
        ####################FRAME#####################
        self.fram = ctk.CTkFrame(self,width=330,height=540,fg_color='black',border_color='white').pack()

        self.result_var = tk.StringVar()
        self.result_var.set('0')
        self.label = tk.Label(master=self,width=18,textvariable=self.result_var,height=0,text='0',justify='right',anchor='e',font=('Microsoft YaHei Light',58),fg='white',bg='black')
        self.label.place(x=10,y=80, anchor='n')

        #All-Clear_Button#######################################################################

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg/ac.png')),size=(60, 60))
        ctk.CTkButton(self,image=self.imglb,border_spacing=0,text='',width=0,fg_color='black',bg_color='black',hover_color=('black'),command=self.clear).place(x=5,y=150)

        # Numbers_Btn#######################################################################

        #Column-1st###############################
        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn7.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('7')).place(x=5, y=225)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn4.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('4')).place(x=5, y=300)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn1.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('1')).place(x=5, y=375)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn0.png')),size=(140, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=130, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('0')).place(x=5, y=450)

        # Column-2st###############################
        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn8.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('8')).place(x=85, y=225)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn5.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('5')).place(x=85, y=300)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn2.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('2')).place(x=85, y=375)

        # Column-3st###############################
        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn9.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('9')).place(x=165, y=225)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn6.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('6')).place(x=165, y=300)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\btn3.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('3')).place(x=165, y=375)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\dotbtn.png')),size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='.',text_color='black', width=0, fg_color='black',hover_color=('black'),bg_color='black',command=lambda :self.get_digit('.')).place(x=165, y=450)

        # Function_button#######################################################################
        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\chngbtn.png')), size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='', width=0, fg_color='black',hover_color=('black'),
                      bg_color='black',command=self.change_sign).place(x=85, y=150)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\prcntge.png')), size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='', width=0, fg_color='black',hover_color=('black'),
                      bg_color='black',command=lambda :self.get_digit('%')).place(x=165, y=150)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\divid.png')), size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='', width=0, fg_color='black',hover_color=('black'),
                      bg_color='black',command=lambda :self.get_digit('/')).place(x=245, y=150)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\multiply.png')), size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='', width=0, fg_color='black',hover_color=('black'),
                      bg_color='black',command=lambda :self.get_digit('*')).place(x=245, y=225)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\minus.png')), size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='', width=0, fg_color='black',hover_color=('black'),
                      bg_color='black',command=lambda :self.get_digit('-')).place(x=245, y=300)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\plus.png')), size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='', width=0, fg_color='black',hover_color=('black'),
                      bg_color='black',command=lambda :self.get_digit('+')).place(x=245, y=375)

        self.imglb = ctk.CTkImage(Image.open(resource_path('calimg\\equal.png')), size=(60, 60))
        ctk.CTkButton(self, image=self.imglb, border_spacing=0, text='', width=0, fg_color='black',hover_color=('black'),
                      bg_color='black',command=lambda :self.get_digit('=')).place(x=245, y=450)

#############################---------FUNCTION----------------------#####################################################

    def clear(self):
        self.result_var.set('0')

    def get_digit(self, text):
        if text == "=" :
            try:
                result = eval(self.result_var.get())
                rslt = round(result,2)
                self.result_var.set(rslt)
            except ZeroDivisionError:
                messagebox.showerror('Calculator','Cannot be divided by 0!',parent=self)
                self.result_var.set('')
            except SyntaxError:
                self.result_var.set('')
            except Exception:
                self.result_var.set('')

        elif text in '+-*/':
            current_text = self.result_var.get()
            if len(current_text) == 0:
                return
            elif current_text[-1] in "+-*/":
                return
            else:
                self.result_var.set(current_text + str(text))

        elif text == '%':
            current_text = self.result_var.get()
            try:
                percentage = float(current_text) / 100
                self.result_var.set(str(percentage))
            except Exception:
                self.result_var.set('')

        else:
            if len(self.result_var.get()) < self.input_limit:
                if text == '.' and '.' in self.result_var.get():
                    return  # Only allow one dot
                if self.result_var.get() == '0' and text != '.':
                    self.result_var.set(text)
                else:
                    self.result_var.set(self.result_var.get() + text)

    def change_sign(self):
        current_value = self.result_var.get()
        if current_value and current_value[0] == "-":
            self.new_value = current_value[1:]
            self.result_var.set(self.new_value)

        else:
            self.new_value = "-" + current_value
            self.result_var.set(self.new_value)

if __name__=='__main__':
    root = Calculator()
    root.mainloop()