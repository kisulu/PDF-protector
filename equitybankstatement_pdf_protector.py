from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader # pip install PyPDF2
import os

root =Tk()
root.title("PDF Protector")
root.geometry("480x430+300+100")
root.resizable(False, False)

def browse():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select PDF file",
                                        filetype=(('PDF file','*.pdf'),('All files','*.*')))
    entry1.insert(END, filename)


def Protect():
    mainfile=source.get()
    protectedfile=target.get()
    code=password.get()

 #   print(mainfile)
 #   print(protectedfile)
  #  print(code)

    if mainfile=="" and protectedfile=="" and password.get()=="":
        messagebox.showerror("error", "Browse pdf file, new name to save and Enter password!!")

    elif mainfile=="":
        messagebox.showerror("Invalid", "Please type SOURCE pdf filename!")

    elif protectedfile=="":
        messagebox.showerror("Invalid", "Please type TARGET pdf filename!")

    elif code=="":
        messagebox.showerror("Invalid", "Please type Your PASSWORD to protect pdf file!")

    else:
        try:
            out=PdfWriter()
            file=PdfReader(filename)
            number_of_pages = len(file.pages)

            for idx in range(number_of_pages):
                # page=file.getPage(idx)
                page = file.pages[0]
                out.add_page(page)

                # password
            out.encrypt(code)

            with open(protectedfile, "wb") as f:
                out.write(f)

            source.set("")
            target.set("")
            password.set("")
            messagebox.showinfo("Saved", "Protected Pdf saved successfully!")

        except:
            messagebox.showerror("Invalid", "Invalid Entry!")
            

#icon
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

#main
top_image=PhotoImage(file="Images/top.png")
label=Label(root, image=top_image).pack()

frame=Frame(root, width=460, height=310,bd=5, relief=GROOVE)
frame.place(x=10,y=110)

#####################333
source=StringVar()
Label(frame, text="Source PDF file:", font="arial 10 bold", fg="#4c4542").place(x=10,y=42)
entry1=Entry(frame, width=20, textvariable=source, font="arial 15", bd=1)
entry1.place(x=130,y=40)

button_icon =PhotoImage(file="Images/button image.png")
Button(frame, image=button_icon, width=35,height=24, bg="#d3cdcd", command=browse).place(x=370, y=38)


#####################333
target=StringVar()
Label(frame, text="Target PDF file:", font="arial 10 bold", fg="#4c4542").place(x=10,y=84)
entry2=Entry(frame, width=20, textvariable=target, font="arial 15", bd=1)
entry2.place(x=130,y=84)

#####################333
password=StringVar()
Label(frame, text="Set User Password", font="arial 10 bold", fg="#4c4542").place(x=5,y=126)
entry3=Entry(frame, width=20, textvariable=password, font="arial 15", bd=1)
entry3.place(x=130,y=124)

button_icon2 =PhotoImage(file="Images/button.png")
Protect=Button(root, text="Protect PDF file", compound=LEFT, image=button_icon2, width=200,height=40, bg="#bfb9b9", font="arial 14 bold", command=Protect)
Protect.place(x=150, y=320)


root.mainloop()
