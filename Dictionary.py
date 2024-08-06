import tkinter as tk
from tkinter.constants import *

from pyglet import resource , font
from tkinter import messagebox as msg
resource.add_font('assets/font.ttf')
tf = font.load('Roboto Mono')

clrs = ['#ff3d8b',"#00002e",'#ffadad']
# FUNCTIONS

def clr(e):
    Word_input["background"] = f'{clrs[2]}'
def cclr(e):
    Word_input["background"] = f'{clrs[0]}'


def getWord(e = None):
    if Word.get() != "":
        import requests
        info = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{Word.get()}")
        if info.ok == True:
            response = info.json()
            Definition = f'{response[0]['meanings'][0]["partOfSpeech"]},\n{response[0]['meanings'][0]['definitions'][0]['definition']},\n{response[0]['meanings'][0]['definitions'][0]['synonyms'] if response[0]['meanings'][0]['definitions'][0]['synonyms'] != [] else '' }'

            
            text.config(state='normal')
            text.delete("1.0","end")
            text.config(state='disabled')
            text.config(state='normal')
            text.insert("end",Definition)
            text.config(state='disabled')
        else:
            msg.showerror("Word Invalid","Word Cannot be found , Please Type The Word Correctly!!")
        Word_input.delete(0,END)
    else:
        msg.showerror("Input Invalid!","Please Enter a Word")


def theme(w):
    global clrs
    if themes.get() == "NightCity":
        clrs = ['#ff3d8b',"#00002e",'#ffadad']
        root.configure(background=f"{clrs[0]}")
        frame['bg'] = f"{clrs[1]}"
        frame['highlightbackground'] = f"{clrs[1]}"
        head['background'] =  f"{clrs[1]}"
        head['fg'] = f"{clrs[0]}"
        Label['foreground'] = f"{clrs[2]}"
        Label['background'] = f"{clrs[1]}"
        Word_input['foreground'] = f"{clrs[1]}"
        Word_input['background'] =f"{clrs[0]}"
        Button['background'] = f"{clrs[1]}"
        Button['activebackground']=f"{clrs[1]}"
        text['foreground'] = f"{clrs[2]}"
        text['background'] = f"{clrs[1]}"
        settings['bg'] = f"{clrs[1]}"
        settings['activebackground'] =f"{clrs[1]}"
    elif themes.get() == "Phonk":
        clrs = ['#2ca89e','#002b36','#859900']
        root.configure(background=f"{clrs[0]}")
        frame['bg'] = f"{clrs[1]}"
        frame['highlightbackground'] = f"{clrs[1]}"
        head['background'] =  f"{clrs[1]}"
        head['fg'] = f"{clrs[0]}"
        Label['foreground'] = f"{clrs[2]}"
        Label['background'] = f"{clrs[1]}"
        Word_input['foreground'] = f"{clrs[1]}"
        Word_input['background'] =f"{clrs[0]}"
        Button['background'] = f"{clrs[1]}"
        Button['activebackground']=f"{clrs[1]}"
        text['foreground'] = f"{clrs[2]}"
        text['background'] = f"{clrs[1]}"
        settings['bg'] = f"{clrs[1]}"
        settings['activebackground'] =f"{clrs[1]}"
    else:
        clrs = ['#2aa198','#fdf6e3','#859900']
        root.configure(background=f"{clrs[0]}")
        frame['bg'] = f"{clrs[1]}"
        frame['highlightbackground'] = f"{clrs[1]}"
        head['background'] =  f"{clrs[1]}"
        head['fg'] = f"{clrs[0]}"
        Label['foreground'] = f"{clrs[2]}"
        Label['background'] = f"{clrs[1]}"
        Word_input['foreground'] = f"{clrs[1]}"
        Word_input['background'] =f"{clrs[0]}"
        Button['background'] = f"{clrs[1]}"
        Button['activebackground']=f"{clrs[1]}"
        text['foreground'] = f"{clrs[2]}"
        text['background'] = f"{clrs[1]}"
        settings['bg'] = f"{clrs[1]}"
        settings['activebackground'] =f"{clrs[1]}"
# GUI

root = tk.Tk()
root.geometry("577x544")
root.title("Dictionary Search")
root.iconbitmap("assets/icon.ico")

root.maxsize(577,544)
root.configure(background=f"{clrs[0]}")

frame = tk.Frame(root,bg=f"{clrs[1]}",relief="groove",border=3,highlightbackground=f"{clrs[1]}")
frame.pack(padx=20,ipadx=480,ipady=520,fill="both",pady=20)

head = tk.Label(root,text="Dictionary Search",font=('Roboto Mono',28),background=f"{clrs[1]}",fg=f"{clrs[0]}")
head.place(x=55,y=50)

#Label

Label = tk.Label(text="Word:",font=("Roboto Mono" ,30),foreground=f"{clrs[2]}",background=f"{clrs[1]}")
Label.place(x=65,y=145)


# Entry

Word = tk.StringVar()
Word_input = tk.Entry(textvariable=Word,foreground=f"{clrs[1]}",background=f"{clrs[0]}",font=("Roboto Mono",15))
Word_input.place(x=65,y=225,width = 350)
Word_input.bind("<Enter>",clr)
Word_input.bind("<Leave>",cclr)


#Button

img_btn = tk.PhotoImage(file="assets/button.png")
Button = tk.Button(image=img_btn,border=0,command=getWord,background=f"{clrs[1]}",activebackground=f"{clrs[1]}")
Button.place(x=425,y=215)


root.bind('<Return>',func=getWord)





# text



text = tk.Text(root,background=f"{clrs[1]}",foreground=f"{clrs[2]}",font=("Georgia",15),state='normal')
scrolly = tk.Scrollbar(text,background=f"{clrs[1]}",activebackground=f"{clrs[0]}",highlightbackground=f'{clrs[1]}',highlightcolor=f'{clrs[0]}',highlightthickness=2,command=text.yview)
text.place(x=55,y=280,width=450,height=150)
scrolly.pack(side="right",fill='y'   )










# Theme CHANGER
Waltheme = ["NightCity","Phonk","DayLight"]

themes = tk.StringVar()
settings = tk.OptionMenu(root,themes,*Waltheme,command=theme)
themes.set(Waltheme[0])
settings.place(x=30,y=440)

brush =  tk.PhotoImage(file="assets/brush.png")

settings.config(image=brush,bg=f"{clrs[1]}",activebackground=f"{clrs[1]}",borderwidth=0)

# Close
cross = tk.PhotoImage(file="assets/cross.png")

tk.Button(image=cross,command=root.destroy).place(x= 10,y=10)

root.mainloop()