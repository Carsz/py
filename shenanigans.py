import tkinter as ttk
UpDown = 250
LeftRight = 250
colorchoosing = 0  #this is used for changing your line colour
colors = ['black', 'green', 'red', 'pink', 'purple']

root = ttk.Tk() # fereastra
root.geometry('500x500')
root.title('Etch-a-Sketch')
canvas = ttk.Canvas(root, width=500, height=500, bg='white')

def Up(event):
    global UpDown
    UpDown -= 1
    canvas.create_line((LeftRight, UpDown), (LeftRight+1, UpDown+1), fill=colors[colorchoosing])
def Down(event):
    global UpDown
    UpDown += 1
    canvas.create_line((LeftRight, UpDown), (LeftRight+1, UpDown+1), fill=colors[colorchoosing])
def Left(event):
    global LeftRight
    LeftRight -= 1
    canvas.create_line((LeftRight, UpDown), (LeftRight+1, UpDown+1), fill=colors[colorchoosing])
def Right(event):
    global LeftRight
    LeftRight += 1
    canvas.create_line((LeftRight, UpDown), (LeftRight+1, UpDown+1), fill=colors[colorchoosing])
def minuscolor(event):
    global colorchoosing
    if colorchoosing == 4:
        colorchoosing = 0
    else:
        colorchoosing -= 1
    print(colors[colorchoosing])
def pluscolor(event):
    global colorchoosing
    if colorchoosing == 4:
        colorchoosing = 0
    else:
        colorchoosing += 1
    print(colors[colorchoosing])
root.bind('w', Up)
root.bind('s', Down)
root.bind('a', Left)
root.bind('d', Right)
root.bind('q', minuscolor)
root.bind('e', pluscolor)
canvas.pack()
root.mainloop()