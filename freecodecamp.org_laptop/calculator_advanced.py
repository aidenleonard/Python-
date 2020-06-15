from app import add
from app import sub
from app import mul
from app import div

import tkinter

def main():
    calc=tkinter.Tk()
    calc.title("Aiden Calculator")
    # Width, height in pixels
    f1=Frame(calc, height=50, width=50)
    f1.pack()
    calc.mainloop()

main()



num1 = float(input("first number: "))

operator = input("select operator: ")  # + - * /

num2 = float(input("second number: "))

if operator == "+":
    ans = add(num1, num2)
if operator == "-":
    ans = sub(num1, num2)
if operator == "*":
    ans = mul(num1, num2)
if operator == "/":
    ans = div(num1, num2)

print(round(ans, 10))
