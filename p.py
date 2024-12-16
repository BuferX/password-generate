import tkinter as tk
import turtle
from random import *
root=tk.Tk()
root.geometry("400x300")
root.title("Генератор паролей")
root.config(background="#218457")
t=tk.Canvas(root,width=600,height=100)
t.pack()
screen=turtle.TurtleScreen(t)
pen1=turtle.RawTurtle(screen)
pen1.color("#9370DB")
pen1.up()
pen1.speed(1000000000000000000000000000000000000000000)
pen1.goto(-300,25)
pen1.down()
pen1.begin_fill()
pen1.right(90)
pen1.forward(50)
pen1.left(90)
pen1.forward(15)
pen1.left(90)
pen1.forward(35)
pen1.right(90)
pen1.forward(20)
pen1.right(90)
pen1.forward(35)
pen1.left(90)
pen1.forward(15)
pen1.left(90)
pen1.forward(50)
pen1.left(90)
pen1.forward(55)
pen1.end_fill()
pen1.up()

pen1.goto(-200,25)
pen1.down()

pen1.begin_fill()
pen1.left(70)
pen1.forward(52)
pen1.left(110)
pen1.forward(10)
pen1.left(70)
pen1.forward(36)
pen1.right(140)
pen1.forward(36)
pen1.left(70)
pen1.forward(10)
pen1.left(110)
pen1.forward(52)
pen1.left(70)
pen1.forward(10)
pen1.end_fill()
pen1.up()
pen1.goto(-180,0)
pen1.down()
pen1.begin_fill()
pen1.forward(30)
pen1.left(90)
pen1.forward(10)
pen1.left(90)
pen1.forward(30)
pen1.left(90)
pen1.forward(10)
pen1.end_fill()
pen1.up()



pen1.goto(-150,25)
pen1.down()
pen1.begin_fill()
pen1.right(90)
pen1.right(90)
pen1.forward(52)
pen1.left(90)
pen1.forward(10)
pen1.left(90)
pen1.forward(22)
pen1.right(90)
pen1.circle(16,180)
pen1.forward(12)
pen1.end_fill()
pen1.up()
pen1.right(90)
pen1.right(90)
pen1.goto(-62,180)
pen1.down()
pen1.circle(7)

pen1.up()
pen1.goto(-70,-30)
pen1.down()
pen1.begin_fill()
pen1.circle(30)
pen1.up()
pen1.goto(50,190)
pen1.down()
pen1.circle(15)
pen1.up()
pen1.end_fill()

pen1.up()
pen1.goto(-20,25)
pen1.down()
pen1.begin_fill()
pen1.right(110)
pen1.forward(52)
pen1.left(110)
pen1.forward(10)
pen1.left(70)
pen1.forward(36)
pen1.right(140)
pen1.forward(36)
pen1.left(70)
pen1.forward(10)
pen1.left(110)
pen1.forward(52)
pen1.left(70)
pen1.forward(10)
pen1.end_fill()
pen1.up()



pen1.goto(25,20)
pen1.down()
pen1.begin_fill()
pen1.left(90)
pen1.forward(50)
pen1.left(90)
pen1.forward(15)
pen1.circle(16,180)
pen1.right(90)
pen1.forward(23)
pen1.left(90)
pen1.forward(17)
pen1.end_fill()





















def passowordgenerate():
    my_list="a b c d e g h k l m n  o p q r s t u w y z".split()*1000
    shuffle(my_list)
    # print(my_list)

    my_list1="a b c d e g h k l m n  o p q r s t u w y z".upper().split()*1000
    shuffle(my_list1)
    # print(my_list1)

    my_list2=list("@!&?$*%:№<>")*1000
    shuffle(my_list2)
    # print(my_list2)

    my_list3=list(range(0,10))*1000
    shuffle(my_list3)
    my_list3=list(map(str,my_list3))
    # print(my_list3)


    num=entry1.get()
    my_list4=[]
    for i in range(int(num)):
        # print(my_list[i])
        my_list4.append(my_list[i])
        my_list4.append(my_list2[i])
        my_list4.append(my_list3[i])
        my_list4.append(my_list1[i])
    # print(my_list4)
    shuffle(my_list4)
    shuffle(my_list4)
    shuffle(my_list4)
    shuffle(my_list4)
    print("".join(my_list4))
    res="".join(my_list4)
    res=res[0:int(num)]
    text1.delete("1.0",tk.END)
    text1.insert("1.0",res)
    
def file_save():
    with open("text.txt","w",encoding="utf-8") as file:
        n=text1.get("1.0",tk.END)
        file.write(f"Сгенирированный пароль:  {n}")
def file_delete():
    with open("text.txt","w",encoding="utf-8") as file:
        text1.delete("1.0",tk.END)
        file.write(" ")















bat1=tk.Button(root,command=passowordgenerate)
bat1.config(text="Сгенирировать")
bat1.config(background="#00733E")
bat1.config(width=15,height=2)
bat1.pack()


menu_bar =tk.Menu(root)
root.config(menu=menu_bar)
file_menu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Файл",menu=file_menu)
file_menu.add_command(label="Сохранить",command=file_save)
file_menu.add_command(label="Информация")
file_menu.add_command(label="Очистить",command=file_delete)


exit_menu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_command(label="Выход",command=root.quit)

























label1=tk.Label(root)
label1.config(text="Сгенирированный пароль: ")
label1.config(background="#61D8A2")
label1.pack()





text1=tk.Text(root)
text1.config(width=150,height=10)
text1.config(background="#61D8A2")
text1.pack()

label2=tk.Label(root)
label2.config(text="Укажите размер пароля: ")
label2.config(background="#61D8A2")
label2.pack()



entry1=tk.Entry(root)
entry1.config(width=30)
entry1.config(background="#61D8A2")
entry1.pack()






















































































root.mainloop()