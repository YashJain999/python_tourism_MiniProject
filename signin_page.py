from tkinter import *
import tkinter as tk
from tkinter import ttk

top = Tk()
top.geometry("800x700")
top.configure(bg='white')
top.grid_rowconfigure(2, weight=2)
# top.grid_columnconfigure(5, weight=1)

bgimage_path = "D:\\Yash\\python\\FirstProject\\images\\bigblue.png"


def photo(image_file_path):
    return PhotoImage(file=image_file_path)


img = PhotoImage(file=bgimage_path)

# photo=PhotoImage(file="D:\\Yash\\python\\FirstProject\\images\\blue.png")
# label1=Label(top,image=img,anchor="ne")
# label1.place(x=0,y=0)


fr = Frame(top, pady=100, bg="white", width=100,padx=100)
label = Label(fr, image=img,width=1200,pady=0,height=1000)
label.place(x=-400, y=-100)
fr.pack()


# canvas=Canvas(top,width=800,height=500)
# canvas.pack(fill="both",expand=True)
#
# # image
# canvas.create_image(0,0,image=photo,anchor="nw")
#
# canvas.create_text(400, 250, text="welcome", font="Helvetica",50)


def submit_val():
    print("your form has been submitted successfully")


Label(fr, text="Registration form", font="times 20 bold", bg="white", anchor="s").grid(row=0, column=0, rowspan=1,
                                                                                       columnspan=2, pady=50,
                                                                                       sticky="s")

name = Label(fr, text="Name:", font="times 14", anchor="e", bg="white")
name.grid(row=1, column=0, sticky="e")
email = Label(fr, text="Email I'd:", font="times 14", anchor="e", bg="white")
email.grid(row=2, column=0, sticky="e")
dob = Label(fr, text="Date Of Birth:", font="times 14", anchor="e", bg="white")
dob.grid(row=3, column=0, sticky="e")
gender = Label(fr, text="Gender:", font="times 14", anchor="e", bg="white")
gender.grid(row=4, column=0, sticky="e")
phone = Label(fr, text="Phone No:", font="times 14", anchor="e", bg="white")
phone.grid(row=5, column=0, sticky="e")
password = Label(fr, text="Password: ", font="times 14", anchor="e", bg="white")
password.grid(row=6, column=0, sticky="e")

name_val = StringVar
email_val = StringVar
dob_val = StringVar
gender_val = StringVar
phone_val = StringVar
password_val = StringVar

# image = PhotoImage(file='D:\\Yash\\python\\FirstProject\\images\\bgimg.png')
# label1=Label(top,image=image)
# label1.pack()
# border=Frame(fr,background="blue")
n_entry = Entry(fr, textvariable=name_val, width="40", highlightthickness=2)
n_entry.grid(row=1, column=1, padx=20, pady=20)
e_entry = Entry(fr, textvariable=email_val, width="40", highlightthickness=2)
e_entry.grid(row=2, column=1, padx=20, pady=20)
dob_entry = Entry(fr, textvariable=dob_val, width="40", highlightthickness=2)
dob_entry.grid(row=3, column=1, padx=20, pady=20)
g_entry = Entry(fr, textvariable=gender_val, width="40", highlightthickness=2)
g_entry.grid(row=4, column=1, padx=20, pady=20)
ph_entry = Entry(fr, textvariable=phone_val, width="40", highlightthickness=2)
ph_entry.grid(row=5, column=1, padx=20, pady=20)
p_entry = Entry(fr, textvariable=password_val, width="40", highlightthickness=2)
p_entry.grid(row=6, column=1, padx=20, pady=20)

# n_entry.grid(padx=1,pady=1)
# border.grid(padx=40,pady=40)

Button(fr, text="Submit", font="times 14", command=submit_val, bg="#6200EA", foreground="white", width=20,
       height=2).grid(row=7, column=0,
                      columnspan=2,
                      pady=50)

# photo=PhotoImage(file="D:\\Yash\\python\\FirstProject\\images\\backimgg.png")
# label1=Label(top,image=photo)
# label1.place(x=0,y=1,anchor="nw")
top.mainloop()
