from tkinter import *
root=Tk()
root.geometry("275x250")
root.title("Calculator")
root.iconbitmap("calc.ico")
root.configure(bg="black")

e = Entry(root, width=46, borderwidth=1,fg="blue")
e.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
def button_click (number):
    current = e.get()
    e.delete (0, END)
    e.insert(0, str (current) + str(number))
def button_clear():
    e.delete(0, END)
def button_add():
    first_number = e.get()
    global add_value
    global math
    add_value=float(first_number)
    math="add"
    e.delete(0, END)

def button_sub():
    second_number = e.get()
    global sub_value
    global math
    sub_value=float(second_number)
    math="sub"
    e.delete(0, END)
def button_mul():
    Third_number = e.get()
    global mul_value
    global math
    mul_value=float(Third_number)
    math="mult"
    e.delete(0, END)

def button_div():
    Fourth_number = e.get()
    global div_value
    global math
    div_value=float(Fourth_number)
    math="div"
    e.delete(0, END)


def button_equal():
    next_value=float(e.get())
    e.delete(0,END)
    global final_value
    global math
    if math=="add":
        final_value=add_value+next_value
        e.insert(0,final_value)
    elif math=="sub":
        final_value =sub_value-next_value
        e.insert(0, final_value)
    elif math=="mult":
        final_value = mul_value*next_value
        e.insert(0, final_value)
    elif math=="div":
        final_value = div_value/next_value
        e.insert(0, final_value)

mybutton_1 = Button(root, text="1", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(1))
mybutton_2 = Button(root, text="2", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(2))
mybutton_3 = Button(root, text="3", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(3))
mybutton_4 = Button(root, text="4", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(4))
mybutton_5 = Button(root, text="5", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(5))
mybutton_6 = Button(root, text="6", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(6))
mybutton_7 = Button(root, text="7", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(7))
mybutton_8 = Button(root, text="8", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(8))
mybutton_9 = Button(root, text="9", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(9))
mybutton_0 = Button(root, text="0", padx=16,pady=8,bd=8,fg="white",bg="grey",font=("ALGERIAN",10,"bold")
                    , command=lambda: button_click(0))
mybutton_add = Button(root, text="+", padx=16,pady=8,bd=8,fg="white",bg="red",font=("ALGERIAN",10,"bold")
                    , command=button_add)
mybutton_equal = Button(root, text="=", padx=16,pady=8,bd=8,fg="white",bg="red",font=("ALGERIAN",10,"bold")
                          , command=button_equal)
mybutton_clear = Button(root, text="C", padx=16,pady=8,bd=8,fg="white",bg="red",font=("ALGERIAN",10,"bold") ,
                         command=button_clear)
mybutton_sub = Button(root, text="-", padx=16,pady=8,bd=8,fg="white",bg="red",font=("ALGERIAN",10,"bold"),
                      command=button_sub)
mybutton_mul =Button(root, text="*", padx=16,pady=8,bd=8,fg="white",bg="red",font=("ALGERIAN",10,"bold") ,
                     command=button_mul)
mybutton_div = Button(root, text="/", padx=16,bd=8,pady=8,fg="white",bg="red",font=("ALGERIAN",10,"bold"),
                      command=button_div)

mybutton_1.grid (row=1, column=0)
mybutton_2.grid (row=1, column=1)
mybutton_3.grid (row=1, column=2)
mybutton_4.grid (row=2, column=0)
mybutton_5.grid (row=2, column=1)
mybutton_6.grid (row=2, column=2)
mybutton_7.grid (row=3, column=0)
mybutton_8.grid (row=3, column=1)
mybutton_9.grid (row=3, column=2)
mybutton_0.grid (row=4, column=1)
mybutton_clear.grid(row=4, column=0)
mybutton_add.grid (row=1, column=3)
mybutton_equal.grid (row=4, column=2)
mybutton_sub.grid (row=4, column=3)
mybutton_mul.grid (row=3, column=3)
mybutton_div.grid (row=2, column=3)
root.mainloop()