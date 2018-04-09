import re

previous = 0
run = True

def calc():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation  = input ("Enter Equation:")
    else:
        equation = input(str(previous))

    if equation == 'exit':
        print ("Bye!!")
        run = False
    else:
        equation = re.sub ('a-zA-Z,#:()""','',equation)

    if previous==0:
        previous = eval(equation)
    else:
        previous = eval(str(previous)+equation)

while run:
    calc()