from tkinter import *
from tkinter import messagebox
import nltk
from nltk.corpus import words
import time
from collections import Counter
nltk.download('words')
word_list = words.words()
Matrix_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
score = 0
window = Tk()
window.geometry("1000x750+0+0")
window.title("Group 23-Find word")
f1 = Frame(window, borderwidth=2)
f1.grid(row=0, column=0)
f2 = Frame(window, borderwidth=2)
f2.grid(row=1, column=0)
f3 = Frame(window, borderwidth=2)
f3.grid(row=0, column=1)
hscore = Label(f3, text="highest Score = 96", font=('Helvetica', '10'))
hscore.grid(row=2, column=6)
f4 = Frame(window, borderwidth=2)
f4.grid(row=1, column=1)
f5 = Frame(window, borderwidth=2)
f5.grid(row=1, column=4)
reset2 = Button(f5, text="Reset game", bg="white", fg="black", font=('Helvetica', '10'), command=lambda: click1(reset2))
reset2.grid(row=2, column=0)
exitgame = Button(f5, text="Exit game", bg="red", fg="black", font=('Helvetica', '10'), command=lambda: exit_game())
exitgame.grid(row=6, column=0)

def checkspells():
    global score
    global total
    word = word_check.get();
    if word in word_list:
        dict = Counter(word)
        flag = 1
        for key in dict.keys():
            if key not in Matrix_list:
                flag = 0
        if flag == 1 and len(word) > 3:
            score = score + len(word)
            total = "score = " + str(score)
            label.configure(text=total)
            print(word)
        else:
            messagebox.showinfo("Check", "No matching with above word OR word length should be greater than 3")
    else:
        print("No Word")
    word_check.delete(0, 'end')

def click1(reset2):
    global total
    global found
    global strg
    global count
    global l
    global score
    global w_found
    global l_found
    global word
    score == 0
    total = "score = " + str(0)
    label.configure(text=total)
    print(word)

btn1 = Button(f2, text="A", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn1))
btn1.grid(column=1, row=1)
btn2 = Button(f2, text="B", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn2))
btn2.grid(column=2, row=1)
btn3 = Button(f2, text="C", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn3))
btn3.grid(column=3, row=1)
btn4 = Button(f2, text="D", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn4))
btn4.grid(column=4, row=1)
btn5 = Button(f2, text="W", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn5))
btn5.grid(column=5, row=1)
btn6 = Button(f2, text="X", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn6))
btn6.grid(column=6, row=1)
btn7 = Button(f2, text="K", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn7))
btn7.grid(column=7, row=1)
btn8 = Button(f2, text="L", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn8))
btn8.grid(column=8, row=1)
btn9 = Button(f2, text="E", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
              command=lambda: click(btn9))
btn9.grid(column=9, row=1)
btn10 = Button(f2, text="A", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn10))
btn10.grid(column=10, row=1)
btn11 = Button(f2, text="V", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn11))
btn11.grid(column=11, row=1)
btn12 = Button(f2, text="E", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn12))
btn12.grid(column=12, row=1)

btn13 = Button(f2, text="A", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn13))
btn13.grid(column=1, row=2)
btn14 = Button(f2, text="E", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn14))
btn14.grid(column=2, row=2)
btn15 = Button(f2, text="I", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn15))
btn15.grid(column=3, row=2)
btn16 = Button(f2, text="J", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn16))
btn16.grid(column=4, row=2)
btn17 = Button(f2, text="H", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn17))
btn17.grid(column=5, row=2)
btn18 = Button(f2, text="T", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn18))
btn18.grid(column=6, row=2)
btn19 = Button(f2, text="Z", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn19))
btn19.grid(column=7, row=2)
btn20 = Button(f2, text="O", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn20))
btn20.grid(column=8, row=2)
btn21 = Button(f2, text="P", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn21))
btn21.grid(column=9, row=2)
btn22 = Button(f2, text="F", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn22))
btn22.grid(column=10, row=2)
btn23 = Button(f2, text="K", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn23))
btn23.grid(column=11, row=2)
btn24 = Button(f2, text="N", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn24))
btn24.grid(column=12, row=2)

btn25 = Button(f2, text="M", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn25))
btn25.grid(column=1, row=3)
btn26 = Button(f2, text="A", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn26))
btn26.grid(column=2, row=3)
btn27 = Button(f2, text="D", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn27))
btn27.grid(column=3, row=3)
btn28 = Button(f2, text="J", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn28))
btn28.grid(column=4, row=3)
btn29 = Button(f2, text="A", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn29))
btn29.grid(column=5, row=3)
btn30 = Button(f2, text="C", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn30))
btn30.grid(column=6, row=3)
btn31 = Button(f2, text="E", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn31))
btn31.grid(column=7, row=3)
btn32 = Button(f2, text="N", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn32))
btn32.grid(column=8, row=3)
btn33 = Button(f2, text="T", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn33))
btn33.grid(column=9, row=3)
btn34 = Button(f2, text="L", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn34))
btn34.grid(column=10, row=3)
btn35 = Button(f2, text="Y", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn35))
btn35.grid(column=11, row=3)
btn36 = Button(f2, text="G", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn36))
btn36.grid(column=12, row=3)

btn37 = Button(f2, text="D", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn37))
btn37.grid(column=1, row=4)
btn38 = Button(f2, text="U", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn38))
btn38.grid(column=2, row=4)
btn39 = Button(f2, text="N", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn39))
btn39.grid(column=3, row=4)
btn40 = Button(f2, text="O", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn40))
btn40.grid(column=4, row=4)
btn41 = Button(f2, text="K", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn41))
btn41.grid(column=5, row=4)
btn42 = Button(f2, text="V", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn42))
btn42.grid(column=6, row=4)
btn43 = Button(f2, text="S", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn43))
btn43.grid(column=7, row=4)
btn44 = Button(f2, text="M", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn44))
btn44.grid(column=8, row=4)
btn45 = Button(f2, text="V", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn45))
btn45.grid(column=9, row=4)
btn46 = Button(f2, text="K", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn46))
btn46.grid(column=10, row=4)
btn47 = Button(f2, text="P", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn47))
btn47.grid(column=11, row=4)
btn48 = Button(f2, text="I", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn48))
btn48.grid(column=12, row=4)

btn49 = Button(f2, text="N", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn49))
btn49.grid(column=1, row=5)
btn50 = Button(f2, text="T", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn50))
btn50.grid(column=2, row=5)
btn51 = Button(f2, text="E", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn51))
btn51.grid(column=3, row=5)
btn52 = Button(f2, text="C", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn52))
btn52.grid(column=4, row=5)
btn53 = Button(f2, text="H", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn53))
btn53.grid(column=5, row=5)
btn54 = Button(f2, text="N", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn54))
btn54.grid(column=6, row=5)
btn55 = Button(f2, text="O", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn55))
btn55.grid(column=7, row=5)
btn56 = Button(f2, text="L", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn56))
btn56.grid(column=8, row=5)
btn57 = Button(f2, text="O", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn57))
btn57.grid(column=9, row=5)
btn58 = Button(f2, text="G", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn58))
btn58.grid(column=10, row=5)
btn59 = Button(f2, text="Y", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn59))
btn59.grid(column=11, row=5)
btn60 = Button(f2, text="N", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn60))
btn60.grid(column=12, row=5)

btn61 = Button(f2, text="A", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn61))
btn61.grid(column=1, row=6)
btn62 = Button(f2, text="I", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn62))
btn62.grid(column=2, row=6)
btn63 = Button(f2, text="X", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn63))
btn63.grid(column=3, row=6)
btn64 = Button(f2, text="H", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn64))
btn64.grid(column=4, row=6)
btn65 = Button(f2, text="K", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn65))
btn65.grid(column=5, row=6)
btn66 = Button(f2, text="T", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn66))
btn66.grid(column=6, row=6)
btn67 = Button(f2, text="P", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn67))
btn67.grid(column=7, row=6)
btn68 = Button(f2, text="J", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn68))
btn68.grid(column=8, row=6)
btn69 = Button(f2, text="B", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn69))
btn69.grid(column=9, row=6)
btn70 = Button(f2, text="I", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn70))
btn70.grid(column=10, row=6)
btn71 = Button(f2, text="J", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn71))
btn71.grid(column=11, row=6)
btn72 = Button(f2, text="E", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn72))
btn72.grid(column=12, row=6)

btn73 = Button(f2, text="T", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn73))
btn73.grid(column=1, row=7)
btn74 = Button(f2, text="F", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn74))
btn74.grid(column=2, row=7)
btn75 = Button(f2, text="T", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn75))
btn75.grid(column=3, row=7)
btn76 = Button(f2, text="R", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn76))
btn76.grid(column=4, row=7)
btn77 = Button(f2, text="A", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn77))
btn77.grid(column=5, row=7)
btn78 = Button(f2, text="I", bg="yellow",fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn78))
btn78.grid(column=6, row=7)
btn79 = Button(f2, text="N", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn79))
btn79.grid(column=7, row=7)
btn80 = Button(f2, text="F", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn80))
btn80.grid(column=8, row=7)
btn81 = Button(f2, text="A", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn81))
btn81.grid(column=9, row=7)
btn82 = Button(f2, text="S", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn82))
btn82.grid(column=10, row=7)
btn83 = Button(f2, text="N", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn83))
btn83.grid(column=11, row=7)
btn84 = Button(f2, text="E", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn84))
btn84.grid(column=12, row=7)

btn85 = Button(f2, text="F", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn85))
btn85.grid(column=1, row=8)
btn86 = Button(f2, text="U", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn86))
btn86.grid(column=2, row=8)
btn87 = Button(f2, text="L", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn87))
btn87.grid(column=3, row=8)
btn88 = Button(f2, text="F", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn88))
btn88.grid(column=4, row=8)
btn89 = Button(f2, text="I", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn89))
btn89.grid(column=5, row=8)
btn90 = Button(f2, text="L", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn90))
btn90.grid(column=6, row=8)
btn91 = Button(f2, text="L", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn91))
btn91.grid(column=7, row=8)
btn92 = Button(f2, text="H", bg="purple", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn92))
btn92.grid(column=8, row=8)
btn93 = Button(f2, text="E", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn93))
btn93.grid(column=9, row=8)
btn94 = Button(f2, text="V", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn94))
btn94.grid(column=10, row=8)
btn95 = Button(f2, text="T", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn95))
btn95.grid(column=11, row=8)
btn96 = Button(f2, text="R", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn96))
btn96.grid(column=12, row=8)

btn97 = Button(f2, text="I", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn97))
btn97.grid(column=1, row=9)
btn98 = Button(f2, text="L", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn98))
btn98.grid(column=2, row=9)
btn99 = Button(f2, text="I", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
               command=lambda: click(btn99))
btn99.grid(column=3, row=9)
btn100 = Button(f2, text="B", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn100))
btn100.grid(column=4, row=9)
btn101 = Button(f2, text="R", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn101))
btn101.grid(column=5, row=9)
btn102 = Button(f2, text="A", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn102))
btn102.grid(column=6, row=9)
btn103 = Button(f2, text="R", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn103))
btn103.grid(column=7, row=9)
btn104 = Button(f2, text="Y", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn104))
btn104.grid(column=8, row=9)
btn105 = Button(f2, text="L", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn105))
btn105.grid(column=9, row=9)
btn106 = Button(f2, text="H", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn106))
btn106.grid(column=10, row=9)
btn107 = Button(f2, text="A", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn107))
btn107.grid(column=11, row=9)
btn108 = Button(f2, text="P", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn108))
btn108.grid(column=12, row=9)

btn109 = Button(f2, text="R", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn109))
btn109.grid(column=1, row=10)
btn110 = Button(f2, text="E", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn110))
btn110.grid(column=2, row=10)
btn111 = Button(f2, text="V", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn111))
btn111.grid(column=3, row=10)
btn112 = Button(f2, text="E", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn112))
btn112.grid(column=4, row=10)
btn113 = Button(f2, text="R", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn113))
btn113.grid(column=5, row=10)
btn114 = Button(f2, text="S", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn114))
btn114.grid(column=6, row=10)
btn115 = Button(f2, text="E", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn115))
btn115.grid(column=7, row=10)
btn116 = Button(f2, text="L", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn116))
btn116.grid(column=8, row=10)
btn117 = Button(f2, text="E", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn117))
btn117.grid(column=9, row=10)
btn118 = Button(f2, text="A", bg="yellow", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn118))
btn118.grid(column=10, row=10)
btn119 = Button(f2, text="R", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn119))
btn119.grid(column=11, row=10)
btn120 = Button(f2, text="N", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn120))
btn120.grid(column=12, row=10)

btn121 = Button(f2, text="S", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn121))
btn121.grid(column=1, row=11)
btn122 = Button(f2, text="A", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn122))
btn122.grid(column=2, row=11)
btn123 = Button(f2, text="C", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn123))
btn123.grid(column=3, row=11)
btn124 = Button(f2, text="R", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn124))
btn124.grid(column=4, row=11)
btn125 = Button(f2, text="I", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn125))
btn125.grid(column=5, row=11)
btn126 = Button(f2, text="F", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn126))
btn126.grid(column=6, row=11)
btn127 = Button(f2, text="I", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn127))
btn127.grid(column=7, row=11)
btn128 = Button(f2, text="C", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn128))
btn128.grid(column=8, row=11)
btn129 = Button(f2, text="E", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn129))
btn129.grid(column=9, row=11)
btn130 = Button(f2, text="N", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn130))
btn130.grid(column=10, row=11)
btn131 = Button(f2, text="P", bg="orange", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn131))
btn131.grid(column=11, row=11)
btn132 = Button(f2, text="T", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn132))
btn132.grid(column=12, row=11)

btn133 = Button(f2, text="T", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn133))
btn133.grid(column=1, row=12)
btn134 = Button(f2, text="A", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn134))
btn134.grid(column=2, row=12)
btn135 = Button(f2, text="C", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn135))
btn135.grid(column=3, row=12)
btn136 = Button(f2, text="H", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn136))
btn136.grid(column=4, row=12)
btn137 = Button(f2, text="J", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn137))
btn137.grid(column=5, row=12)
btn138 = Button(f2, text="K", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn138))
btn138.grid(column=6, row=12)
btn139 = Button(f2, text="K", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn139))
btn139.grid(column=7, row=12)
btn140 = Button(f2, text="N", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn140))
btn140.grid(column=8, row=12)
btn141 = Button(f2, text="T", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn141))
btn141.grid(column=9, row=12)
btn142 = Button(f2, text="M", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn142))
btn142.grid(column=10, row=12)
btn143 = Button(f2, text="S", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn143))
btn143.grid(column=11, row=12)
btn144 = Button(f2, text="F", bg="cyan", fg="Black", width=3, height=1, font=('Helvetica', '20'),
                command=lambda: click(btn144))
btn144.grid(column=12, row=12)

def click(b, word=None):
    global found
    global total
    global strg
    global count
    global l
    global score
    global w_found
    global l_found
    global c
    global conn
    if (b["text"] == ""):
        found = 1
        messagebox.showinfo("OOPS!!!!!!!!", "wrong!!!! button")

def tick(time1=''):
    time2 = time.strftime("%M:%S")
    if time2 != time1:
        time1 = time2;
        timer.config(text="After 1 minute it will be closed automatically " + time2)
    timer.after(200, tick)

def quit_pro():
    messagebox.showinfo("Oops!!", "Time Up!")
    window.destroy()

def exit_game():
    window.destroy()

word_check = Entry(window, width=30, bd=0)
word_check.configure(highlightbackground="red", highlightcolor="red")
word_check.place(x=750, y=200)
word_check.focus()
btncheck = Button(window, text="Submit", bg="purple", fg="white", width=5, font=('Helvetica', '10'),
                  command=checkspells)
btncheck.place(x=820, y=250)
label = Label(window, text="Score = 0")
label.place(x=810, y=160)
timer = Label(window, text="You have 1 minute")
timer.place(x=790, y=300)
tick()
window.after(60000, quit_pro)
window.mainloop()
window.destroy()