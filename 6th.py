from tkinter import *
root = Tk()
 
def click(event):
    print("클릭위치", event.x, event.y)
 
lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)
frame = Frame(root, width=300, height=300)
 
 #왼쪽 마우스 버튼 바인딩
frame.bind("<Button-1>", click) 
frame.bind("<Button-3>", click) 
 
frame.pack()
root.mainloop()