from tkinter import *
root = Tk()
 
def click(event):
    print("클릭위치", event.x, event.y)

root.title("happy")

lbl = Label(root, text="Class Notice")
lbl.pack()

frame = Frame(root, width=300, height=300)

 #왼쪽 마우스 버튼 바인딩
frame.bind("<Button-1>", click) 
frame.bind("<Button-3>", click) 
 
frame.pack()
root.mainloop()