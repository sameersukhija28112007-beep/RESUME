import tkinter
import math

def click(value):
    e = entry.get()  
    answer = " "

    try:
        if value == "C":
            e = e[0:len(e) - 1]  
            entry.delete(0, "end")
            entry.insert(0, e)
            return  

        elif value == "CE":
            entry.delete(0, "end")

        elif value == "sqr":
            answer = math.sqrt(eval(e))

        elif value == "pi":
            answer = math.pi

        elif value == "cos":
            answer = math.cos(math.radians(eval(e)))

        elif value == "sin":
            answer = math.sin(math.radians(eval(e)))

        elif value == "tan":
            answer = math.tan(math.radians(eval(e)))

        elif value == "2π":
            answer = 2 * math.pi

        elif value == "cosh":
            answer = math.cosh(eval(e))

        elif value == "sinh":
            answer = math.sinh(eval(e))

        elif value == "tanh":
            answer = math.tanh(eval(e))

        elif value == chr(8731):
            answer = eval(e) ** (1 / 3)

        elif value == "x\u02b8":
            entry.insert("end", "**")
            return

        elif value == "x\u00B3":
            answer = eval(e) ** 3

        elif value == "x\u00B2":
            answer = eval(e) ** 2

        elif value == "ln":
            answer = math.log2(eval(e))

        elif value == "deg":
            answer = math.degrees(eval(e))

        elif value == "rad":
            answer = math.radians(eval(e))

        elif value == "e":
            answer = math.e
  
        elif value == "log10":
            answer = math.log10(eval(e))

        elif value == "x!":
            answer = math.factorial(eval(e))

        elif value == chr(247):
            entry.insert("end", "/")
            return

        elif value == "=":
            answer = eval(e)

        else:
            entry.insert("end", value)
            return

        entry.delete(0, "end")
        entry.insert(0, answer)

    except SyntaxError:
        pass



root = tkinter.Tk()
root.title("Scientific Calculator")
root.geometry("680x460+400+200")
root.config(bg="black")

entry = tkinter.Entry(root, font=("arial", 20, "bold"), bg="pink", fg="black", bd=10, width=30,justify="right")  
entry.grid(row=0, column=0, columnspan=8)

button_list = ["C", "CE", "√", "+", "π", "cos", "tan", "sin", "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh","4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg","rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]
r = 1
c = 0
for i in button_list:
    button = tkinter.Button(root, width=5, height=2, bd=2, text=i, bg="black", fg="pink",font=("arial", 18, "bold"), command=lambda button=i: click(button))
    button.grid(row=r, column=c,padx=0, pady=1)
    c += 1
    if c > 7:
        r += 1 
        c = 0
root.mainloop()