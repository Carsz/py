import tkinter as ttk
UpDown = 250
LeftRight = 250
colorchoosing = 0
colors = ['black', 'green', 'red', 'pink', 'purple']
brushsize = 3

root = ttk.Tk()
root.geometry('500x500')
root.title('Etch-a-Sketch')
canvas = ttk.Canvas(root, width=500, height=500, bg='white')

def Up(event):
    global UpDown
    UpDown -= 3
    canvas.create_line((LeftRight, UpDown), (LeftRight+brushsize, UpDown+brushsize+1), fill=colors[colorchoosing])
def Down(event):
    global UpDown
    UpDown += 3
    canvas.create_line((LeftRight, UpDown), (LeftRight+brushsize, UpDown+brushsize+1), fill=colors[colorchoosing])
def Left(event):
    global LeftRight
    LeftRight -= 3
    canvas.create_line((LeftRight, UpDown), (LeftRight+brushsize, UpDown+brushsize+1), fill=colors[colorchoosing])
def Right(event):
    global LeftRight
    LeftRight += 3
    canvas.create_line((LeftRight, UpDown), (LeftRight+brushsize, UpDown+brushsize+1), fill=colors[colorchoosing])
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
def clear(event):
    global UpDown
    global LeftRight
    canvas.delete('all')
    UpDown = 250
    LeftRight = 250
def showcoords(event):
    global UpDown
    global LeftRight
    print(f'X = {LeftRight} \nY = {UpDown}')
def plussize(event):
    global brushsize
    brushsize += 1
    print(f'brush size: {brushsize}')
def minussize(event):
    global brushsize
    brushsize -= 1
    print(f'brush size: {brushsize}')
root.bind('w', Up)
root.bind('s', Down)
root.bind('a', Left)
root.bind('d', Right)
root.bind('q', minuscolor)
root.bind('e', pluscolor)
root.bind('<space>', clear)
root.bind('c', showcoords)
root.bind('z', minussize)
root.bind('x', plussize)
canvas.pack()
root.mainloop()
