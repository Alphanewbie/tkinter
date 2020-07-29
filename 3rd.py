from tkinter import *

# 클래스에 tkinter의 Frame을 상속한다.
class MyFrame(Frame):
    def __init__(self, master):
        # tkinter의 PhotoImage 클래스
        img = PhotoImage(file='./alpha.gif')
        # 이미지에 이름을 붙히고, 이미지의 위치를 저장하는 과정
        lbl = Label(image=img)
        # 가비지 컬렉션으로 삭제 되는 것을 막기 위해 레퍼렌스를 추가
        lbl.image = img
        lbl.place(x=0, y=0)


def main():
    root = Tk()
    root.title('이미지 보기')
    root.geometry('600x400+0+0')
    myframe = MyFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()
