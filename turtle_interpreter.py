try:
    import turtle
except turtle:
    print("Failed to load Turtle")

def convert(command_type,command_value,command_stat):
    if (int(command_type)==0):
        turtle.clearscreen()
    elif (int(command_type)==1):
        turtle.forward(int(command_value))
    elif (int(command_type)==2):
        turtle.backward(int(command_value))
    elif (int(command_type)==3):
        turtle.left(int(command_value))
    elif (int(command_type)==4):
        turtle.right(int(command_value))
    elif (int(command_type)==5):
        turtle.up()
    elif (int(command_type)==6):
        turtle.down()
    elif (int(command_type)==7):
        turtle.setx(int(command_value))
    elif (int(command_type)==8):
        turtle.sety(int(command_value))
    elif (int(command_type)==9):
        turtle.pensize(int(command_value))
    elif (int(command_type)==10):
        r=(command_value[0]+command_value[1]+command_value[2])
        g=(command_value[3]+command_value[4]+command_value[5])
        b=(command_value[6]+command_value[7]+command_value[8])
        turtle.pencolor((int(r),int(g),int(b)))
    else:
        print("Error on command ",command_stat)

a=input("File to load: ")
f1=open(a,"r")
b=f1.read()
i=0
b=b.split(" ")
print(b)
turtle.hideturtle()
turtle.colormode(255)
turtle.speed(500)
print("length ",len(b))
while i< len(b):
    print(b[i],b[i+1])
    convert(b[i],b[i+1],i)
    i=i+2
f1.close()
